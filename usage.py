from perceptron import Perceptron
from reader import CSV_reader 

# Imput of training data

training_data = CSV_reader.read_csv('td_lorry.csv')
training_inputs = [ [] for _ in range(len(training_data))]

labels = [ 0 for i in range(len(training_data))]

for i in range(len(training_data)):
	training_inputs[i].append(int(training_data[i][0]))
	training_inputs[i].append(int(training_data[i][1]))
	labels[i] = int(training_data[i][2])

print(training_inputs)
print(labels)

# Trainning step  

perceptron = Perceptron(2)
perceptron.train(training_inputs, labels)

# Test of the prediction 

inputs = [0,0]
result =  []

prediction_tests = CSV_reader.read_csv('lorryvan.csv')

for i in range(1,len(prediction_tests)):
	inputs[0] = int(prediction_tests[i][0])
	inputs[1] = int(prediction_tests[i][1])
	result = perceptron.predict(inputs)
	print(f'The result for {prediction_tests[i][0]}, {prediction_tests[i][1]} = {result} the true is {prediction_tests[i][2]}.')













