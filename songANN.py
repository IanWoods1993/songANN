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
	#plt.show()
	#print(spectrogram[0][0]) #i don't really understand what the numbers here mean
	# the ... are just a number representation issue
	return(spectrogram)

#spectrogram is 812 x 612 pixels = 496944 pixels
#a node for every pixel is a shitty idea -> too big

def getAudioFromSpectrogram(spectrogram):
	try:
    #change the file's name and format
		image_file = 'image.png'
		fin = open(image_file, "rb") #binary read
		data = fin.read()
		fin.close()
	except IOError:
		print("Image file %s not found" % imageFile)
		raise SystemExit

	return(audio)

def initializeNeuralNet():
	neuralNet = FeedForwardNetwork()
	inLayer = LinearLayer(812*20) #812 time slices, 20 frequency nodes
	hiddenLayer = SigmoidLayer(812) #determine for each time slice
	outLayer =  LinearLayer(1)
	neuralNet.addInputModule(inLayer)
	neuralNet.addModule(hiddenLayer)
	neuralNet.addOutputModule(outLayer)
	return(neuralNet)

def main():
	song = open(getSong())
	songPath = song.name
	#songPath = "/home/ian/songANN/COTD.wav" #just to skip the box
	spectrogram = getSpectrogram(songPath)
	#here, call getAudioFromSpectrogram with the right args, etc.
	neuralNet = initializeNeuralNet()
	#spectrogram = input for the neural network
	return[0]
main()

#current task - get Pybrain working
