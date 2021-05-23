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
        print('trainnig ... ')
        for _ in range(self.threshold):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                for i in range(1,len(self.weights)):
                	self.weights[i] += self.learning_rate * (label - prediction) * inputs[i-1]
                self.weights[0] += self.learning_rate * (label - prediction)
                