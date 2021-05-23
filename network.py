from perceptron import Perceptron

class Network_manager(object):
    """A Network manager to control multiple perceptrons functions.

    Used to instantiate, train, manage data to be inputed and receive
    results from perceptron class.

    Attributes:
        For the moment no atriibutes, but we could modify it to declare
        the number of inputs the perceptrons are going to have and the 
        numbers of neorons based on the number of outputs.
    """
    def __init__(self, number_of_inputs = 63, number_of_neorons = 7):
        """Inits the network of perceptrons witha a fixed value of 63 inputs and 7 nourons 
        for the context of reconize some alphabet caracters ."""
        self.number_of_inputs = number_of_inputs
        self.number_of_neorons = number_of_neorons
        self.neurons_instantiation()

    def neurons_instantiation(self):
        """Instantiate neorons needed to the network.
    
        Basically a global list of neorons is declared 
        """
        self.array_of_neurons = []
        for index in range(self.number_of_neorons):
            self.array_of_neurons.append(Perceptron(self.number_of_inputs))

    def partitione_by_letter(self, labels):
        """Used to to separate the labels by all the given inputs.
    
        This is necessary so each neoron train with its respective set of datas and 
        the correct labels is inputed.
        So all the data that represents the first caracter is trained first but all 
        data is inputed togheter and the distctinction is made by labels.
        To do it the matrix of labels is transposed so we have the colunm representing labels 
        for each caracter to be trained.

        Exemple :

        inputs = [ [1,2], [3,4], [5,6], [7,8] ]
        labels = [ [1,0], [0,1], [1,0], [1,0] ]

        with the given inputs we have two distinct labels represented by the inputs , 
        so we need to tranposed the labels and in that way we can train each neoron
        that hold the caracter independly trained.

        Transposed :

        inputs = [ [1,2], [3,4], [5,6], [7,8] ]
        transposed = [ [1,0,1,0], [0,1,0,1] ]

        Args:
            A list of list representing the labels.

        Returns:
            A transposed matrix dividing it by caracter.
        """
        result = [[labels[j][i] for j in range(len(labels))] for i in range(len(labels[0]))]
        return result

    def directioner_of_trainning_data(self, training_inputs, labels):
        """Direct data to its respective neoron.
    
        First it call the partitione_by_letter method that used the transposed version of
        the labels matrix.
        Then traverse all the neorons passing its all the data and its respective labels
        to execute the training.

        Args:
            A list of lists integer containig the training inputs 
            A list of lists integer containing the labels for the training inputs

        """
        labels_transposed = self.partitione_by_letter(labels)

        index = 0
        for row in labels_transposed:
            self.array_of_neurons[index].train(training_inputs, row)
            index += 1
        print('Done with training')

    def results_temp(self,prediction_tests, test_labels):
        """Fetch for the predicted results by the perceptrons.
    
        Traverse through all teh neorons chacking the ones that returns a 1 value
        so that way the possible predictions are stored in a list of the possible 
        results and the appended to a final answer result list.

        Args:
            List of integers containing all the test to be done.
            List of integers with all the right labels for the prediction_tests list

        Returns:
            List with all the answers of the predictions.
        """
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