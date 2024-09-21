from numpy import *
from pylab import *
import util
import datasets
import binary
import dumbClassifiers
import dt
import runClassifier

h = dt.DT({'maxDepth': 2})
h.train(datasets.TennisData.X, datasets.TennisData.Y)
print(h)