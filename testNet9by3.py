from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import FeedForwardNetwork, LinearLayer, SigmoidLayer, FullConnection
from pybrain.structure.connections.connection import Connection
from pybrain.structure.connections.shared import MotherConnection, SharedFullConnection
from pybrain.structure import TanhLayer
from pybrain.structure.moduleslice import ModuleSlice
import sys

net = FeedForwardNetwork()

inputLayer = LinearLayer(9)
hiddenLayer = SigmoidLayer(3)
outputLayer = LinearLayer(1)

net.addInputModule(inputLayer)
net.addModule(hiddenLayer)
net.addOutputModule(outputLayer)

inputToHidden1 = FullConnection(inputLayer, hiddenLayer, inSliceFrom = 0, inSliceTo = 3, outSliceFrom = 0, outSliceTo = 1)
inputToHidden2 = FullConnection(inputLayer, hiddenLayer, inSliceFrom = 3, inSliceTo = 6, outSliceFrom = 1, outSliceTo = 2)
inputToHidden3 = FullConnection(inputLayer, hiddenLayer, inSliceFrom = 6, inSliceTo = 9, outSliceFrom = 2, outSliceTo = 3)

print(inputToHidden1.params)

net.addConnection(inputToHidden1)
net.addConnection(inputToHidden2)
net.addConnection(inputToHidden3)
net.addConnection(FullConnection(hiddenLayer, outputLayer))

net.sortModules()

print(net.activate([i for i in range(0,9)]))
