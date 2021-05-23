from perceptron import Perceptron
from reader import CSV_reader 
from network import Network_manager

# Imput of training data
training_data = []
training_inputs = []
labels = []

def conversor(name_of_file):

	training_data = []
	training_inputs = []

	training_data = CSV_reader.read_csv('td_lorry.csv')
	training_inputs = [ [] for _ in range(len(training_data))]

	labels = [ 0 for i in range(len(training_data))]

	for i in range(len(training_data)):
		training_inputs[i].append(int(training_data[i][0]))
		training_inputs[i].append(int(training_data[i][1]))
		labels[i] = int(training_data[i][2])
	
	return training_inputs, labels

def data_organizer(name_of_file):
	training_data = CSV_reader.read_csv(name_of_file)

	training_inputs = [ [] for _ in range(len(training_data))]
	labels = [ [] for i in range(len(training_data))]

	for i in range(len(training_data)):
		training_inputs[i] = training_data[i][0:-7] 
		labels[i] = training_data[i][-7:]

	training_inputs = [ [ int(training_inputs[i][j]) for j in range(len(training_inputs[0])) ] for i in range(len(training_inputs)) ]
	labels = [ [ int(labels[i][j]) for j in range(len(labels[0])) ] for i in range(len(labels)) ]
	return training_inputs, labels

#training_inputs, labels =conversor('td_lorry.csv')
training_inputs, labels = data_organizer('caracteres-limpo2.csv')

#print(training_inputs)
#print(labels)


#data_organizer('caracteres-limpo2.csv')

# Trainning step  

network = Network_manager()
network.directioner_of_trainning_data(training_inputs,labels)




#perceptron = Perceptron(2)
#perceptron.train(training_inputs, labels)

# Test of the prediction 
'''
inputs = [0,0]
result =  []

prediction_tests = CSV_reader.read_csv('lorryvan.csv')
network.results_temp(prediction_tests)
for i in range(1,len(prediction_tests)):
	inputs[0] = int(prediction_tests[i][0])
	inputs[1] = int(prediction_tests[i][1])
	result = perceptron.predict(inputs)
	print(f'The result for {prediction_tests[i][0]}, {prediction_tests[i][1]} = {result} the true is {prediction_tests[i][2]}.')
'''












