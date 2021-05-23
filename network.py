from perceptron import Perceptron

class Network_manager(object):
    def __init__(self, number_of_inputs = 63, number_of_neurons = 7):
        self.number_of_inputs = number_of_inputs
        self.number_of_neorons = number_of_neurons
        self.neurons_instantiation()

    def neurons_instantiation(self):
        self.array_of_neurons = []
        for index in range(self.number_of_neorons):
            self.array_of_neurons.append(Perceptron(self.number_of_inputs))

    def partitione_by_letter(self, labels):
        result = [[labels[j][i] for j in range(len(labels))] for i in range(len(labels[0]))]
        return result

    def directioner_of_trainning_data(self, training_inputs, labels):
        #self.perceptron.train(training_inputs, labels)
        '''
        for label in labels:
            for index in range(len(label)):
                if label[index] == 1 : 
                    print(index, end=", ")
            print()
        '''
        labels_transposed = self.partitione_by_letter(labels)

        index = 0
        for row in labels_transposed:
            self.array_of_neurons[index].train(training_inputs, row)
            index += 1
        print('Done with training')
        ''''''
        #self.array_of_neurons[index].train(training_inputs[index], labels[index])
        #print(mappend)

        '''
        for label in labels:
            column_labels = []
            for index in range(len(label)):
                if label[index] == 1 : 

                    print(labels[index])
                    column_labels.append(1)
                else:
                    column_labels.append(0)
            print()
        '''   
    def results_temp(self,prediction_tests):
        """
        """

        '''
        inputs = [0,0]
        result =  []
        for i in range(1,len(prediction_tests)):
            inputs[0] = int(prediction_tests[i][0])
            inputs[1] = int(prediction_tests[i][1])
            result = self.perceptron.predict(inputs)
            print(f'The result for {prediction_tests[i][0]}, {prediction_tests[i][1]} = {result} the true is {prediction_tests[i][2]}.')
        '''