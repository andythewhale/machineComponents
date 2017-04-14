#This is a basic component for 2 dimensional linear regression.

###comp block start

import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

#import your data
data = pd.read('file')


#label variables
x = data[['x']]
y = data[['y']]

#training model
reg = linear_model.LinearRegression()
reg.fit(x,y)

#visualization
plt. scatter(x,y)
plt.plot(x,reg.predict(x))
plt.show()

###comp block end