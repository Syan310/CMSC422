from numpy import *
from pylab import *
import util
import datasets
import binary
import dumbClassifiers
import runClassifier

h = dumbClassifiers.FirstFeatureClassifier({})
runClassifier.trainTestSet(h, datasets.TennisData)
print(h)