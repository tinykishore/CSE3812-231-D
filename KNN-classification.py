# Importing the libraries
import numpy as np
from sklearn import datasets
import random

# define the value of K
K = 20

# Importing the dataset from sklearn library
iris = datasets.load_iris()

# Splitting columns into dependent (Y) and independent (X) variables
# Dependent variable is the last column
# Independent variables are the first 4 columns, in this case we are taking the first 2 columns
X = iris.data[:, :2]
Y = (iris.target != 0) * 1

# Shuffling the dataset, so that the training and test set are not biased
random.shuffle(X)
random.shuffle(Y)

# Splitting the dataset into training and validation set
# generate a random variable from 0 to 1, if it is less than 0.7, then it is a training sample
# if it is greater than 0.7 but less than 0.85, then it is a validation sample
# if it is greater than 0.85, then it is a test sample
X_train = []
Y_train = []
X_validation = []
Y_validation = []
X_test = []
Y_test = []

for v in range(len(X)):
    rnd = np.random.random()
    if 0 <= rnd <= 0.70:
        X_train.append(X[v])
        Y_train.append(Y[v])
    elif 0.70 < rnd <= 0.85:
        X_validation.append(X[v])
        Y_validation.append(Y[v])
    else:
        X_test.append(X[v])
        Y_test.append(Y[v])

# KNN classification with validation set and test set
total_correct = 0
for v in range(len(X_validation)):
    distances = []

    # calculate the distance between the validation sample and each training sample
    for t in range(len(X_train)):
        r = np.sqrt(np.sum(np.square(X_validation[v] - X_train[t])))
        distances.append((X_train[t], Y_train[t], r))
    # sort the distances in ascending order
    distances.sort(key=lambda tup: tup[2])

    # take the first K samples
    neighbors = distances[:K]

    # determine the majority class
    classes = [neighbor[1] for neighbor in neighbors]
    predicted_class = max(classes, key=classes.count)

    # Test Print
    print(neighbors)
    print(classes)
    print(predicted_class)
    print("\n\n\n\n\n\n")

    # check if the prediction is correct
    if predicted_class == Y_validation[v]:
        total_correct += 1

# calculate the validation accuracy
accuracy = (total_correct / len(X_validation)) * 100
print("Validation accuracy:", accuracy)
