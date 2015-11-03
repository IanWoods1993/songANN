from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import FeedForwardNetwork, LinearLayer, SigmoidLayer, FullConnection
from pybrain.structure.connections.connection import Connection
from pybrain.structure.connections.shared import MotherConnection, SharedFullConnection
from pybrain.structure import TanhLayer
from pybrain.structure.moduleslice import ModuleSlice
import sys

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
	#print("inSliceFrom = ", i * subnetSize, ", inSliceTo = ", i * subnetSize + subnetSize, ", outSliceFrom = ", i, ", outSliceTo = ", i + 1)
	inputToHidden = FullConnection(inputLayer, hiddenLayer, inSliceFrom = i * subnetSize, inSliceTo = i * subnetSize + subnetSize, outSliceFrom = i, outSliceTo = i + 1)
	net.addConnection(inputToHidden)

net.addConnection(FullConnection(hiddenLayer, outputLayer))

net.sortModules()

print(net.activate([i for i in range(0,inputSize)]))
