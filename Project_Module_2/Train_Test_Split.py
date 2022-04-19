import pandas as pd
import numpy as np



model_data = pd.read_csv('model_data_scaled.csv').iloc[:, 1:]
# print(model_data.head())

###################################Split
split_date='2020-01-01'
training_set, test_set = model_data[model_data['date']<split_date], model_data[model_data['date']>=split_date]
training_set = training_set.drop('date', 1)
test_set = test_set.drop('date', 1)

# print("Length of Model Data : " + str(len(model_data)))
# print("Length of Training Data : " + str(len(training_set)))
# print("Length of Testing Data : " + str(len(test_set)))



####################################Setting Window Length
window_len=32
pred_range=30

training_inputs = []
for i in range(len(training_set)-window_len):
    temp_set = training_set[i:(i+window_len)].copy()
    training_inputs.append(temp_set)

####################################Filling Training and Testing data
test_inputs = []
for i in range(len(test_set)-window_len):
    temp_set = test_set[i:(i+window_len)].copy()
    test_inputs.append(temp_set)

#print(test_inputs[0])
test_outputs = test_set['btc_close'][window_len:].values
#print(len(test_outputs))

training_inputs = [np.array(training_inputs) for training_inputs in training_inputs]
training_inputs = np.array(training_inputs)

test_inputs = [np.array(test_inputs) for test_inputs in test_inputs]
test_inputs = np.array(test_inputs)

training_outputs = []
for i in range(window_len, len(training_set['btc_close']) - pred_range):
    training_outputs.append(training_set['btc_close'][i:i + pred_range].values)

training_outputs = np.array(training_outputs)

# testing outputs, which is needed to evaluate/predict the model
test_outputs = []
for i in range(window_len, len(test_set['btc_close']) - pred_range):
    test_outputs.append(test_set['btc_close'][i:i + pred_range].values)

test_outputs = np.array(test_outputs)



