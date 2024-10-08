from math import *
import random
from numpy import *
import matplotlib.pyplot as plt
import numpy as np
import datasets

waitForEnter=False

def generateUniformExample(numDim):
    return [random.random() for d in range(numDim)]

def generateUniformDataset(numDim, numEx):
    return [generateUniformExample(numDim) for n in range(numEx)]

def computeExampleDistance(x1, x2):
    dist = 0.0
    for d in range(len(x1)):
        dist += (x1[d] - x2[d]) * (x1[d] - x2[d])
    return sqrt(dist)

def computeDistances(data):
    N = data.shape[0]
    D = data.shape[1]
    dist = []
    for n in range(N):
        for m in range(n):
            dist.append(np.sqrt(np.sum((data[n] - data[m])**2)) / np.sqrt(D))
    return dist

def computeDistancesSubdims(data, d):
    N = data.shape[0]
    indices = np.random.choice(data.shape[1], d, replace=False)
    subsampled_data = data[:, indices]
    return computeDistances(subsampled_data)

    
N    = 200                   # number of examples
Dims = [2, 8, 32, 128, 512]   # dimensionalities to try
Cols = ['#FF0000', '#880000', '#000000', '#000088', '#0000FF']
Bins = arange(0, 1, 0.02)

plt.xlabel('distance / sqrt(dimensionality)')
plt.ylabel('# of pairs of points at that distance')
plt.title('dimensionality versus uniform point distances')

for i,d in enumerate(Dims):
    distances = computeDistancesSubdims(datasets.DigitData.X, d)
    print("D=%d, average distance=%g" % (d, mean(distances) * sqrt(d)))
    plt.hist(distances,
             Bins,
             histtype='step',
             color=Cols[i])
    if waitForEnter:
        plt.legend(['%d dims' % d for d in Dims])
        plt.show(False)
        x = raw_input('Press enter to continue...')


plt.legend(['%d dims' % d for d in Dims])
plt.savefig('fig.pdf')
plt.show()

