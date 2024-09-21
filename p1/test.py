from numpy import *
from pylab import *
import util
import datasets
import binary
import dumbClassifiers
import dt
import runClassifier

curve = runClassifier.hyperparamCurveSet(dt.DT({}), 'maxDepth', [1,2,4,6,8,12,16], datasets.SentimentData)
runClassifier.plotCurve('DT on Sentiment Data (hyperparameter)', curve)