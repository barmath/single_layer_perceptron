from perceptron import Perceptron
from reader import CSV_reader 
from network import Network_manager

class Usage(object):

	def conversor(self, name_of_file):
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

	def data_organizer(self, name_of_file):
		training_data = CSV_reader.read_csv(name_of_file)

		training_inputs = [ [] for _ in range(len(training_data))]
		labels = [ [] for i in range(len(training_data))]

		for i in range(len(training_data)):
			training_inputs[i] = training_data[i][0:-7] 
			labels[i] = training_data[i][-7:]

		training_inputs = [ [ int(training_inputs[i][j]) for j in range(len(training_inputs[0])) ] for i in range(len(training_inputs)) ]
		labels = [ [ int(labels[i][j]) for j in range(len(labels[0])) ] for i in range(len(labels)) ]
		return training_inputs, labels

	def result_formater(self,numered_labels, results):
		for index in range(len(numered_labels)):
			print(f'correct answer is : {numered_labels[index]}',end=', the predictions are : ')
			for j in range(len(results[index])):
				print(f' p{j} : {results[index][j]}',end=', ')
			print()
	
	def labels_numerator(self,labels):
		numered_labels = []
		for label in labels:
			for index in range(len(label)):
				if label[index] == 1 :
					numered_labels.append(index)

		return numered_labels
	
	def data_training(self, name_of_file):
		self.training_inputs = []
		self.labels = []
		self.training_inputs, self.labels = self.data_organizer(name_of_file)
		self.network = Network_manager()
		self.network.directioner_of_trainning_data(self.training_inputs,self.labels)

	def predict(self, name_of_file):
		test_data, test_labels = usage_utilities.data_organizer(name_of_file)
		numered_labels = usage_utilities.labels_numerator(test_labels)
		results = self.network.results_temp(test_data, numered_labels)
		usage_utilities.result_formater(numered_labels, results)



# Imput of training data


usage_utilities = Usage()
usage_utilities.data_training('caracteres-limpo2.csv')
print('First Test')
usage_utilities.predict('caracteres-ruido2.csv')
print('Second Test')
usage_utilities.predict('caracteres-ruido22.csv')

















