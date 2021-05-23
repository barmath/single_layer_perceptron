from perceptron import Perceptron

class Network_manager(object):
    def __init__(self, number_of_inputs = 63, number_of_neorons = 7):
        self.number_of_inputs = number_of_inputs
        self.number_of_neorons = number_of_neorons
        self.neurons_instantiation()

    def neurons_instantiation(self):
        self.array_of_neurons = []
        for index in range(self.number_of_neorons):
            self.array_of_neurons.append(Perceptron(self.number_of_inputs))

    def partitione_by_letter(self, labels):
        result = [[labels[j][i] for j in range(len(labels))] for i in range(len(labels[0]))]
        return result

    def directioner_of_trainning_data(self, training_inputs, labels):

        labels_transposed = self.partitione_by_letter(labels)

        index = 0
        for row in labels_transposed:
            self.array_of_neurons[index].train(training_inputs, row)
            index += 1
        print('Done with training')

    def results_temp(self,prediction_tests, test_labels):
        result = []
        final_answer = []
        index = 0
        has_answer = False

        for test_row in prediction_tests:
            temp = []
            for index_neoron in range(self.number_of_neorons):
                result = self.array_of_neurons[index_neoron].predict(test_row)
                if result == 1 :
                    temp.append(index_neoron)
            final_answer.append(temp)

        return final_answer