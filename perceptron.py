class Perceptron(object):
    def __init__(self, no_of_inputs, threshold = 100, learnig_rate = 0.01):
        self.threshold = threshold
        self.learning_rate = learnig_rate
        self.weights = [0 for i in range(no_of_inputs+1)]
 
    def predict(self, inputs):
	# Adding the bias
        activation = self.weights[0]
	# Adding the weights 
        for i in range(1,len(self.weights)):
            activation += self.weights[i]*inputs[i-1]
      
        if activation > 0:
            return 1
        return 0
    
    def train(self, training_inputs, labels):
        for _ in range(self.threshold):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                for i in range(1,len(self.weights)):
                	self.weights[i] += self.learning_rate * (label - prediction) * inputs[i-1]
                self.weights[0] += self.learning_rate * (label - prediction)
                
"""               
import numpy as np

class Perceptron(object):

    def __init__(self, no_of_inputs, threshold=100, learning_rate=0.01):
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.weights = np.zeros(no_of_inputs + 1)
           
    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        if summation > 0:
          activation = 1
        else:
          activation = 0            
        return activation

    def train(self, training_inputs, labels):
        for _ in range(self.threshold):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs
                self.weights[0] += self.learning_rate * (label - prediction)
"""