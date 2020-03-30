import sklearn.model_selection as model_selection
import numpy as np
from matplotlib import pyplot as plt
from sklearn.preprocessing import OneHotEncoder
#Imported Everything
from keras import models
from keras import layers


def standardize(x):
    mean = np.mean(x, axis=0)
    std = np.std(x, axis=0)
    xStd = (x-mean)/std
    return xStd


def createData(skiprowNum, usecolArr):

    #if not binomial, then normalize 
    #if not sure normalize

    data  = np.loadtxt("tempFinaldata.csv", delimiter=',', skiprows=skiprowNum, usecols = usecolArr, dtype=np.str)
    
    yRaw = data[:,-1]
    x = data[:,0:-1]
    x = x.astype(np.float)
   
    x = standardize(x)
    Y = yRaw.astype(np.float)
    train_data, test_data, train_targets, test_targets = model_selection.train_test_split(x, Y, 
                                            train_size=0.75,test_size=0.25, random_state=101)
    
    return train_data, test_data, train_targets, test_targets


train_data, test_data, train_targets, test_targets = createData(0,list(range(0,36)))

#CREATE THE NETWORK
model = models.Sequential()

#ADD THE LAYERS - 1. Output, activation, input
model.add(layers.Dense(46, activation='relu',input_shape=(len(train_data[0]), ) ) )
model.add(layers.Dense(25, activation='relu'))
#ADD THE SECOND AND LAST LAYER
model.add(layers.Dense(1))

#COMPILE THE NETWORK
model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

history = model.fit(train_data, train_targets,
                        epochs=100, batch_size=1)

mae_history = history.history['mean_absolute_error']        

test_mse_score, test_mae_score = model.evaluate(test_data, test_targets)

predicted_prices = model.predict(test_data)
error_list = np.abs(predicted_prices.flatten()-test_targets)
mae_sum = np.sum(error_list)
mae_temp=mae_sum/len(test_targets)

print("Keras MAE: ", test_mae_score, "   My MAE: ", mae_temp)

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])# [left, bottom, width, height]
ax.plot(np.arange(len(mae_history)), mae_history, "ro", label = "cost")
ax.set_title("Shoe! MSE per Epoch")
ax.set_xlabel("Epoch")
ax.set_ylabel("Costs")
ax.legend()  

