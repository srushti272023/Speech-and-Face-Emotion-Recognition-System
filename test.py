import pyaudio
import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time
import detection_emotion_practice as validate
#import video_capture as value
#import lecture_details as detail_data
#import video_second as video1

#import lecture_video  as video

import os
import wave
import pickle
from sys import byteorder
from array import array
from struct import pack
from tkinter.filedialog import askopenfilename
from sklearn.neural_network import MLPClassifier #frwd and bckwrd propogation

from utils import extract_feature

root = tk.Tk()
root.configure(background="white")



w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.state("zoomed")
root.title("test")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('dep.jpg')
image2 = image2.resize((w, h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
#
label_l1 = tk.Label(root, text="SPEECH RECOGNITION SYSTEM",font=("Georgia", 25, 'bold'),
                    background="#113F67", fg="#F3F9FB", width=85, height=2)
label_l1.place(x=-150, y=0)


THRESHOLD = 500
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
RATE = 16000

SILENCE = 30

def is_silent(snd_data):
    "Returns 'True' if below the 'silent' threshold"
    return max(snd_data) < THRESHOLD

def normalize(snd_data):
    "Average the volume out"
    MAXIMUM = 16384
    times = float(MAXIMUM)/max(abs(i) for i in snd_data)

    r = array('h')
    for i in snd_data:
        r.append(int(i*times))
    return r

def trim(snd_data):
    "Trim the blank spots at the start and end"
    def _trim(snd_data):
        snd_started = False
        r = array('h')

        for i in snd_data:
            if not snd_started and abs(i)>THRESHOLD:
                snd_started = True
                r.append(i)

            elif snd_started:
                r.append(i)
        return r

    # Trim to the left
    snd_data = _trim(snd_data)

    # Trim to the right
    snd_data.reverse()
    snd_data = _trim(snd_data)
    snd_data.reverse()
    return snd_data

def add_silence(snd_data, seconds):
    "Add silence to the start and end of 'snd_data' of length 'seconds' (float)"
    r = array('h', [0 for i in range(int(seconds*RATE))])
    r.extend(snd_data)
    r.extend([0 for i in range(int(seconds*RATE))])
    return r

def record():
    """
    Record a word or words from the microphone and 
    return the data as an array of signed shorts.

    Normalizes the audio, trims silence from the 
    start and end, and pads with 0.5 seconds of 
    blank sound to make sure VLC et al can play 
    it without getting chopped off.
    """
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=1, rate=RATE,
        input=True, output=True,
        frames_per_buffer=CHUNK_SIZE)

    num_silent = 0
    snd_started = False

    r = array('h')

    while 1:
        # little endian, signed short
        snd_data = array('h', stream.read(CHUNK_SIZE))
        if byteorder == 'big':
            snd_data.byteswap()
        r.extend(snd_data)

        silent = is_silent(snd_data)

        if silent and snd_started:
            num_silent += 1
        elif not silent and not snd_started:
            snd_started = True

        if snd_started and num_silent > SILENCE:
            break

    sample_width = p.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    p.terminate()

    r = normalize(r)
    r = trim(r)
    r = add_silence(r, 0.5)
    return sample_width, r

# def record_to_file(path):
#     "Records from the microphone and outputs the resulting data to 'path'"
#     sample_width, data = record()
#     data = pack('<' + ('h'*len(data)), *data)

#     wf = wave.open(path, 'wb')
#     wf.setnchannels(1)
#     wf.setsampwidth(sample_width)
#     wf.setframerate(RATE)
#     wf.writeframes(data)
#     wf.close()
def upload():
    # load the saved model (after training)
    model = pickle.load(open("mlp_classifier.model", "rb"))
    print("Please talk")
    fileName = askopenfilename(initialdir='/dataset', title='Select image',
                                  filetypes=[("all files", "*.*")])
    filename = fileName    # record the file (start talking)
        #record_to_file(filename)
        # extract features and reshape it
    features = extract_feature(filename, mfcc=True, chroma=True, mel=True,tonnetz=True,contrast=True).reshape(1, -1)
        # predict
    result = model.predict(features)[0]
    result = str(result)
        # show the result !
    print("result:", str(result))
    print(result)
    print(type(result))
    if result == "sad":
        label_l2 = tk.Label(root, text="Person is Sad",font=("Georgia", 20, 'bold'),
                            background="#00315C", fg="white", width=20, height=2)
        label_l2.place(x=450, y=290)
    elif result == "happy":
        label_l2 = tk.Label(root, text="Person is Happy",font=("Georgia", 20, 'bold'),
                            background="#00315C", fg="white", width=20, height=2)
        label_l2.place(x=450, y=290)
    elif result == "neutral":
        label_l2 = tk.Label(root, text="Person is Neutral",font=("Georgia", 20, 'bold'),
                            background="#00315C", fg="white", width=20, height=2)
        label_l2.place(x=450, y=290)
    elif result == "calm":
        label_l2 = tk.Label(root, text="Person is Calm",font=("Georgia", 20, 'bold'),
                            background="#00315C", fg="white", width=20, height=2)
        label_l2.place(x=450, y=290)
    elif result == "angry":
        label_l2 = tk.Label(root, text="Person is Angry",font=("Georgia", 20, 'bold'),
                            background="#00315C", fg="white", width=20, height=2)
        label_l2.place(x=450, y=290)
    elif result == "fearful":
        label_l2 = tk.Label(root, text="Person is Fearful ",font=("Georgia", 20, 'bold'),
                            background="#00315C", fg="white", width=20, height=2)
        label_l2.place(x=450, y=290)
    elif result == "disgust":
        label_l2 = tk.Label(root, text="Person is Disgusted",font=("Georgia", 20, 'bold'),
                            background="#00315C", fg="white", width=20, height=2)
        label_l2.place(x=450, y=290)
    elif result == "surprised":
        label_l2 = tk.Label(root, text="Person is Surprised",font=("Georgia", 20, 'bold'),
                            background="#00315C", fg="white", width=20, height=2)
        label_l2.place(x=450, y=290)

button1 = tk.Button(root, text="UPLOAD AUDIO FILE", command=upload, width=18, height=1,font=('Georgia', 20, ' bold '), bg="#226597", fg="#F3F9FB")
button1.place(x=100, y=200)

def window():
  root.destroy()



button2 = tk.Button(root, text="EXIT",command=window,width=18, height=1,font=('Georgia', 20, ' bold '), bg="#226597", fg="#F3F9FB")
button2.place(x=100, y=400)

root.mainloop()    