class Perceptron(object):
    """Definition of the perceptron neuron.

    Used to init predict and train information. 
    This class implements a prediction method that is a step using a step
    function in a linear way.
    Also the train function is using the traditional minimizing error in a traditional 
    manner.

    Attributes:
        no_of_inputs: A integer representing the total number of inputs that
        this Perceptron is going to have.
    """
    def __init__(self, no_of_inputs, threshold = 100, learnig_rate = 0.01):
        """Inits Perceptron with the given input, threshold used to count the epocs, and
        the learnig hate that determines how slow or fast it going to learn  ."""
        self.threshold = threshold
        self.learning_rate = learnig_rate
        self.weights = [0 for i in range(no_of_inputs+1)]

    
    def predict(self, inputs):
        """Predict if based on the inputs and the activation function.
    
        By multiplying with treined weights and the inputs it calculates the 
        activation result.

        Args:
            A list of integers that represent the inputs. 
            This list must to match the exact number of inputs previous declared. 

        Returns:
            A integer 1 if the neuron is activated and 0 if not.
        """
        activation = self.weights[0]
        for i in range(1,len(self.weights)):
            activation += self.weights[i]*inputs[i-1]
      
        if activation > 0:
            return 1
        return 0
    
    def train(self, training_inputs, labels):
        """Used to train the perceptron.
    
        Implements a minimizing error logic in wich follow the steps of :

        1 - While all the threshold is not in the end :
            1.a - For each pair(inputs, label) of training data :
                I   - Determine and compute the activation input based on the step function.
                II  - Update each weight based on the prediction output and learning rate.
                III - Update the bias based on the prediction output and learning rate.

        Args:
            A list of integers that represent the inputs to be trained. 
            This list must to match the exact number of inputs previous declared.
        """
        print('trainnig ... ')
        for _ in range(self.threshold):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                for i in range(1,len(self.weights)):
                	self.weights[i] += self.learning_rate * (label - prediction) * inputs[i-1]
                self.weights[0] += self.learning_rate * (label - prediction)
                