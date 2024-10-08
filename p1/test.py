from numpy import *
from pylab import *
import util
import datasets
import binary
import dumbClassifiers
import dt
import runClassifier
import knn
import perceptron
h = dt.DT({'maxDepth': 2})
h.train(datasets.SentimentData.X, datasets.SentimentData.Y)
print(h)
