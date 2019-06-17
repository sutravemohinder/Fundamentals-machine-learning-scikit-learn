from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt
import warnings

from sklearn.datasets import make_moons
from sklearn.cluster import SpectralClustering


# For reproducibility
np.random.seed(1000)

nb_samples = 1000


def show_dataset(X, Y):
    fig, ax = plt.subplots(1, 1, figsize=(30, 25))

    ax.grid()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    for i in range(nb_samples):
        if Y[i] == 0:
            ax.scatter(X[i, 0], X[i, 1], marker='o', color='r')
        else:
            ax.scatter(X[i, 0], X[i, 1], marker='^', color='b')

    plt.show()


def show_clustered_dataset(X, Y):
    fig, ax = plt.subplots(1, 1, figsize=(30, 25))

    ax.grid()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    for i in range(nb_samples):
        if Y[i] == 0:
            ax.scatter(X[i, 0], X[i, 1], marker='o', color='r')
        else:
            ax.scatter(X[i, 0], X[i, 1], marker='^', color='b')

    plt.show()


if __name__ == '__main__':
    warnings.simplefilter("ignore")

    # Create dataset
    X, Y = make_moons(n_samples=nb_samples, noise=0.05)

    # Show dataset
    show_dataset(X, Y)

    # Create and train Spectral Clustering
    sc = SpectralClustering(n_clusters=2, affinity='nearest_neighbors')
    Y = sc.fit_predict(X)

    # Show clustered dataset
    show_clustered_dataset(X, Y)