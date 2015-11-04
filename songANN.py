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
	#spectrum = spectrogram[0].transpose()
	#plt.show()
	#print(spectrogram[0][0]) #i don't really understand what the numbers here mean
	# the ... are just a number representation issue
	return(spectrogram)


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

def initializeNeuralNet(subnetSize, hiddenSize):

	net = FeedForwardNetwork()

#	subnetSize = 129
#	hiddenSize = 486
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

#def getSamplesFromSpectrum(spectrum, 

def main():
	#song = open(getSong())
	#songPath = song.name
	songPath = "/home/ian/songANN/COTD.wav" #just to skip the box
	spectrum = getSpectrogram(songPath)[0].transpose() #[0] is the periodogram, .transpose() puts time in the x axis of the matrix and frequency on the y axis
	print(len(spectrum))
	print(len(spectrum[0]))
	#neuralNet = initializeNeuralNet(len(spectrum[0]), 486)
	
	#find out how to add shit into the neural net from the spectrogram
	return
main()

