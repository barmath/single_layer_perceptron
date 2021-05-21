from reader import CSV_reader 

training_data = CSV_reader.read_csv('caracteres-limpo2.csv')

training_inputs = [ [] for _ in range(len(training_data))]
labels = [ [] for i in range(len(training_data))]

for i in range(len(training_data)):
	training_inputs[i] = training_data[i][0:-8] 
	labels[i] = training_data[i][-7:-1]

print(training_inputs)
print(labels)
print(len(training_data))