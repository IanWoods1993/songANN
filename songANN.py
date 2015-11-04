#!/usr/bin/env python
import tkinter as tk
from tkinter import filedialog
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import FeedForwardNetwork, LinearLayer, SigmoidLayer, FullConnection, TanhLayer
from pybrain.structure.connections.connection import Connection
from pybrain.structure.moduleslice import ModuleSlice
from pybrain.structure.connections.shared import MotherConnection, SharedFullConnection

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

	net = FeedForwardNetwork()

	subnetSize = 20
	hiddenSize = 812
	inputSize = subnetSize * hiddenSize

	inputLayer = LinearLayer(inputSize)
	hiddenLayer = SigmoidLayer(hiddenSize)
	outputLayer = LinearLayer(1)

	net.addInputModule(inputLayer)
	net.addModule(hiddenLayer)
	net.addOutputModule(outputLayer)

	for i in range (0, hiddenSize):
		inputToHidden = FullConnection(inputLayer, hiddenLayer, inSliceFrom = i * subnetSize, inSliceTo = i * subnetSize + subnetSize, outSliceFrom = i, outSliceTo = i + 1)
		net.addConnection(inputToHidden)
	net.addConnection(FullConnection(hiddenLayer, outputLayer))
	net.sortModules()
	return net

def main():
	#song = open(getSong())
	#songPath = song.name
	songPath = "/home/ian/songANN/COTD.wav" #just to skip the box
	spectrogram = getSpectrogram(songPath)
	spectrum = spectrogram[0].transpose()
	print(len(spectrum))
	print(len(spectrum[0]))
	print("Freqs length: ", len(spectrogram[1]))
	print(len(spectrogram[2]))
	#for s in spectrogram:
	#	print(len(s))
	#print(len(spectrogram))
	#for i in spectrogram[0]:
	#	for j in i:
	#		counter = counter + 1
	#print(counter)
	#here, call getAudioFromSpectrogram with the right args, etc.
	neuralNet = initializeNeuralNet()
	#print(neuralNet)
	#spectrogram = input for the neural network
	#find out how to add shit into the neural net from the spectrogram
	return[0]
main()

