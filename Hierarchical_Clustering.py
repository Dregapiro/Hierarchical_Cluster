import numpy as np
import matplotlib.pyplot as plt
import math

X = np.array([[5,3],
    [10,15],
    [15,12],
    [24,10],
    [30,30],
    [85,70],
    [71,80],
    [60,78],
    [70,55],
    [80,91],])

# print("lala")
# labels = range(1, 11)
# plt.figure(figsize=(10, 7))
# plt.subplots_adjust(bottom=0.1)
# plt.scatter(X[:,0],X[:,1], label='True Position')
#
# # for label, x, y in zip(labels, X[:, 0], X[:, 1]):
# #     plt.annotate(
# #         label,
# #         xy=(x, y), xytext=(-3, 3),
# #         textcoords='offset points', ha='right', va='bottom')
# # plt.show()
#
#
# a = X.__len__()
# Y = np.zeros((a,a));
# #print(Y)
#
# for i in range(a) :
#     #print(X[i,0],",", X[i,1])
#     for j in range(a):
#         print(((X[i,0]-X[j,0])**2+(X[i,1]-X[j,1])**2)**0.5)
#         Y[i,j] = ((X[i,0]-X[j,0])**2+(X[i,1]-X[j,1])**2)**0.5
#     #print(Y[i,j])
# print(Y)

from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt

linked = linkage(X, 'single')
print(linked)

labelList = range(1, 11)

plt.figure(figsize=(10, 7))
dendrogram(linked,
            orientation='top',
            labels=labelList,
            distance_sort='descending',
            show_leaf_counts=True)
plt.show()
#cluster 1 cluster 2

class Cluster:

    def __init__(self):
        self.name = []
        self.x_axis=[]
        self.y_axis=[]

    def giveAtributes(self, name, x_axis, y_axis):
        self.name.append(name)
        self.x_axis.append(x_axis)
        self.y_axis.append(y_axis)

    def mergeClusters(self, newCluster):
        self.giveName(newCluster.name)
        self.giveXaxis(newCluster.x_axis)
        self.giveYaxis(newCluster.y_axis)

    # Add name to list
    def giveName(self, givenName):
        for i in range(givenName.__len__()):
            self.name.append(givenName[i])

    # Add distance to list
    def giveXaxis(self, givenX):
        for i in range(givenX.__len__()):
            self.x_axis.append(givenX[i])

    def giveYaxis(self, givenY):
        for i in range(givenY.__len__()):
            self.y_axis.append(givenY[i])

    # Find minimun distance
    #def findMinDistance(self):



# punktA = Cluster()
# punktC = Cluster()
# punktA.giveAtributes("A", 0, 1)
# print(str(punktA.name) + str(punktA.x_axis) + str(punktA.y_axis))
# punktB = Cluster()
# punktB.giveAtributes("B", 2, 3)
#
# print(str(punktA.name) + str(punktA.x_axis) + str(punktA.y_axis))
# punktA.mergeClusters(punktB)
# print(str(punktA.name) + str(punktA.x_axis) + str(punktA.y_axis))
# punktC.giveAtributes("C", 1, 2)
# print(str(punktC.name) + str(punktC.x_axis) + str(punktC.y_axis))


