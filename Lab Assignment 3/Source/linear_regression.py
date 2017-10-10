# Linear Regression

# Step 1: Importing the libraries required

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Step 2: Import the dataset
dataset = pd.read_csv('Salary_Data.csv')
iv = dataset.iloc[:, :-1].values
dv = dataset.iloc[:, 1].values

# Step 3: Split the dataset into the Training set and Test set
# Importing the train_test_split from the sklearn.cross_validation
from sklearn.cross_validation import train_test_split
iv_train, iv_test, dv_train, dv_test = train_test_split(iv, dv, test_size = 1/3, random_state = 0)

# Step 4: Fit the Simple Linear regression model to the Training set
# Importing the LinearRegression class from the sklearn.linear_model library
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(iv_train, dv_train)

# Step 5: Predict the results on Test set
dv_pred = reg.predict(iv_test)

# Step 6: Visualisation of the Training set results
# Using matplotlib.pyplot library to visualize the results
plt.scatter(iv_train, dv_train, color = 'red')
plt.plot(iv_train, reg.predict(iv_train), color = 'blue')
plt.title('Salary vs Experience fo the Training set')
plt.xlabel('Experience in years')
plt.ylabel('Salary')
plt.show()

# Step 7: Visualisation of the Test set results
# Using matplotlib.pyplot library to visualize the results
plt.scatter(iv_test, dv_test, color = 'red')
plt.plot(iv_train, reg.predict(iv_train), color = 'blue')
plt.title('Salary vs Experience for the Test set')
plt.xlabel('Experience in years')
plt.ylabel('Salary')
plt.show()
