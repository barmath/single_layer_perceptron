from perceptron import Perceptron
from reader import CSV_reader 
from network import Network_manager

class Usage(object):
	"""Usage contains methods that are used to organize, and display data.

    This class contains methods to format data from a csv file, also format 
	the results to be printed in a easy way to understand.
    """

	def data_organizer(self, name_of_file):
		"""Divides data from inputs to labels.
    
        It opens the file using a csv reader and then split it into training data and
		labels 

        Args:
            String with the name of file 

        Returns:
            Two list of integers, one with the training_inputs and other with the labels.
        """
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
		"""Format results from predictions and print it.
    
		It basically go over all the inputs and put side by side the correct label 
		with the predictions :

		Example of output :

		a) One prediction result :
		correct answer is : 6, the predictions are :  p0 : 6,

		b) Two prediction results :
		correct answer is : 1, the predictions are :  p0 : 1,  p1 : 4, 

		c) No prediction results :
		correct answer is : 3, the predictions are : 

        Args:
            List of integers of all the labels numered
			List of lists of integers, containing all the prediction results  

        Prints:
            The results with the right answers 
        """
		for index in range(len(numered_labels)):
			print(f'correct answer is : {numered_labels[index]}',end=', the predictions are : ')
			for j in range(len(results[index])):
				print(f' p{j} : {results[index][j]}',end=', ')
			print()
	
	def labels_numerator(self,labels):
		"""Convert the labels from 0 and 1 to a number of index.
    
        Its used to determine witch is the caracters that hold the index 1 
		so it can be conpared to the predictions based on the neorons that were fired 

        Args:
            List of integer of labels  

        Returns:
        	List of integers numerating labels by its represented index.
        """
		numered_labels = []
		for label in labels:
			for index in range(len(label)):
				if label[index] == 1 :
					numered_labels.append(index)

		return numered_labels
	
	def data_training(self, name_of_file):
		"""Receive training file and train all neorons.
    
        First it organizes all the data;
		Then instantiate the Network manager so neorons can be instantiated;
		in the end train the neorons based on the training_inputs and labels.

        Args:
            String representing the name of the file used for training  
        """
		self.training_inputs = []
		self.labels = []
		self.training_inputs, self.labels = self.data_organizer(name_of_file)
		self.network = Network_manager()
		self.network.directioner_of_trainning_data(self.training_inputs,self.labels)

	def predict(self, name_of_file):
		"""Make all the predictions.
    
        First organize all the data;
		Then numerate correnct labels so it can be conpared with predictions;
		Finally predict the answer passing the test data to all neorons

        Args:
            Name of the test file  
        """
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

















