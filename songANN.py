#!/usr/bin/env python
import tkinter as tk
from tkinter import filedialog
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
from pybrain.structure import FeedForwardNetwork

def getSong():
	root = tk.Tk()
	root.withdraw()
	file_path = filedialog.askopenfilename()
	return(file_path)

def getSpectrogram(songPath):
	input_data = read(songPath)
	audio = input_data[1]
	spectrogram = plt.specgram(audio)
	print(spectrogram[0]) #i don't really understand what the numbers here mean
	return(spectrogram)

def initializeNeuralNet():
	return(neuralNet)

def main():
	#song = open(getSong())
	#songPath = song.name
	songPath = "/home/ian/songANN/COTD.wav" #just to skip the box
	spectrogram = getSpectrogram(songPath)
	neuralNet = initializeNeuralNet()
	#spectrogram = input for the neural network
	return[0]
main()

#current task - get Pybrain working
