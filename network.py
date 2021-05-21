from perceptron import Perceptron

class Network_manager:
    def __init__(self, number_of_inputs = 21, number_of_neurons = 7):
        self.number_of_inputs = number_of_inputs
        self.number_of_neorons = number_of_neurons

    def neurons_instantiation(self):
        array_of_neurons = []
        for index in range(self.number_of_neorons):
            array_of_neurons[index] = Perceptron(self.number_of_inputs)

    def directioner_of_trainning_data(self, training_data, labels):
        for label in labels:
            for index in range(len(label)):
                if index == 1 :
                    print(index)

            
        