import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator , MonthLocator , DateFormatter
from datetime import timedelta
import pandas as pd
import numpy as np
import datetime
import time
from keras.models import Sequential
from keras.layers import Activation, Dense
from keras.layers import LSTM, GRU
from keras.layers import Dropout

from Train_Test_Split import training_set,training_inputs,training_outputs,test_set,test_inputs,test_outputs

###############################################Importing Data from Model.csv file

model_data = pd.read_csv('model_data.csv')

###############################################Printing the Training and Testing Datsets

print("Training Inputs and Outputs Shapes")
print(training_set)
print(training_inputs.shape)
print(training_outputs.shape)

print("Testing Inputs and Outputs Shapes")
print(training_set)
print(test_inputs.shape)
print(test_outputs.shape)

###############################################Plotting the Training and Testing Datsets

# plt.plot(training_set["btc_close"], color='blue', label='Training BTC Data')
# plt.plot(test_set["btc_close"], color = 'red', label = 'Test BTC Data')
#
# plt.title('BTC Price Prediction', fontsize = 18)
# plt.xlabel('Time', fontsize=18)
# plt.ylabel('BTC Price(USD)', fontsize = 18)
# plt.legend(loc = 'best')
#
# plt.show()

##################################################Build the LSTM Model

def lstm_model(inputs, output_size, neurons, activ_func="relu",
                dropout=0.25, loss="mae", optimizer="adam"):
    model = Sequential()
    model.add(LSTM(neurons, input_shape=(inputs.shape[1], inputs.shape[2])))
    model.add(Dropout(dropout))
    model.add(Dense(units=output_size))
    model.add(Activation("linear"))

    model.compile(loss=loss, optimizer=optimizer)
    return model

##################################################Training the LSTM Model



