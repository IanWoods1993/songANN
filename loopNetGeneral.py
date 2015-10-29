from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import FeedForwardNetwork, LinearLayer, SigmoidLayer, FullConnection
from pybrain.structure.connections.connection import Connection
from pybrain.structure.connections.shared import MotherConnection, SharedFullConnection
from pybrain.structure import TanhLayer
from pybrain.structure.moduleslice import ModuleSlice
net = FeedForwardNetwork()

inputSize = 6
hiddenSize = 3
sliceSize = inputSize / hiddenSize


inputLayer = LinearLayer(inputSize)
net.addInputModule(inputLayer)

hiddenLayer = SigmoidLayer(hiddenSize)
net.addModule(hiddenLayer)

outputLayer = LinearLayer(1)
net.addOutputModule(outputLayer)

inputToHidden = MotherConnection(1, name = "inputToHidden")
hiddenToOutput = MotherConnection(1, name = "hiddenToOutput")

for i in range(0,hiddenSize):
	inputSlice = ModuleSlice(inputLayer, outSliceFrom = i*sliceSize, outSliceTo = i*sliceSize+(sliceSize - 1))
	hiddenSlice = ModuleSlice(hiddenLayer, inSliceFrom = i*sliceSize, inSliceTo = i*sliceSize+(sliceSize - 1), outSliceFrom = i, outSliceTo = i+1)
	net.addConnection(SharedFullConnection(inputToHidden, inputSlice, hiddenSlice))
	net.addConnection(SharedFullConnection(hiddenToOutput, hiddenSlice, outputLayer))

net.sortModules()

print(net.activate([i for i in range (0, inputSize)]))
