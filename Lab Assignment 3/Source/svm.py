# In this program we are implementing support vector machine alsorithm to analyse social network ads data

# Importing the necessary libraries such as numpy, matplotlib and pandas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset where iv is the independent variable and dv is the dependent variable
dataset = pd.read_csv('SocialNetworkAds.csv')
iv = dataset.iloc[:, [2, 3]].values
dv = dataset.iloc[:, 4].values

# Split the dataset into the Training set and Test set using train_test_split class
from sklearn.cross_validation import train_test_split
iv_train, iv_test, dv_train, dv_test = train_test_split(iv, dv, test_size = 0.20, random_state = 0)

# Feature Scaling is done by using StandardScaler class. sc is the StandardScaler object
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
iv_train = sc.fit_transform(iv_train)
iv_test = sc.transform(iv_test)

# Fitting the Support vector machine model to the training data set. Kernel used is linear.
from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(iv_train, dv_train)

# Predict the test set results by using predict method of classifier.
dv_pred = classifier.predict(iv_test)

# Calculate the confusion matrix to determine the wrong predictions done. It also determines the accuracy.
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(dv_test, dv_pred)

# Visualization of the training set results
from matplotlib.colors import ListedColormap
iv_set, dv_set = iv_train, dv_train
X1, X2 = np.meshgrid(np.arange(start = iv_set[:, 0].min() - 1, stop = iv_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = iv_set[:, 1].min() - 1, stop = iv_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('blue', 'red')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(dv_set)):
    plt.scatter(iv_set[dv_set == j, 0], iv_set[dv_set == j, 1],
                c = ListedColormap(('blue', 'red'))(i), label = j)
plt.title('Support Vector Machine for Training set')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()

# Visualization of the test set results
from matplotlib.colors import ListedColormap
iv_set, dv_set = iv_test, dv_test
X1, X2 = np.meshgrid(np.arange(start = iv_set[:, 0].min() - 1, stop = iv_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = iv_set[:, 1].min() - 1, stop = iv_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('blue', 'red')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(dv_set)):
    plt.scatter(iv_set[dv_set == j, 0], iv_set[dv_set == j, 1],
                c = ListedColormap(('blue', 'red'))(i), label = j)
plt.title('Support Vector Machine for Test set')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()