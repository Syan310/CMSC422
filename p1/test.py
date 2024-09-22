from numpy import *
from pylab import *
import util
import datasets
import binary
import dumbClassifiers
import dt
import runClassifier
import knn

runClassifier.trainTestSet(knn.KNN({'isKNN': False, 'eps': 8.0}), datasets.DigitData)