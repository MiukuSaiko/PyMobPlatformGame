import random



class Neuralnetwork():
	def __init__(self):
		
		#self.synaptic_weights=random.randint(0,1)/ random.randint(1,10)
		print('Hello word')
		
	def sigmoid(self,neuron_input):
		return 1/(1+2.72 ** -neuron_input)
	
	def neuron(self,input):
		return self.sigmoid(input)
	
	def input(self,input_data,input_data1,weight,weight2):
		self.synaptic_weights=random.randint(0,1)/ random.randint(1,10)
		self.synaptic_weights1=random.randint(0,1)/ random.randint(1,10)
		return (input_data*weight)+(input_data1*weight2)

AI=Neuralnetwork()
w1=0.45
w2=0.78
w3=-0.12
w4=0.13
w5=1.5
w6=-2.3

Input_data=float(input("Первые входные данные: "))
Input_data1=float(input("Вторые входные данные: "))

H1=AI.neuron(AI.input(Input_data,Input_data1,w1,w3))
print(H1)
H2=AI.neuron(AI.input(Input_data,Input_data1,w2,w4))
print(H2)

b3=1*(random.randint(0,3)/random.randint(1,10))
O1=AI.neuron(AI.input(H1,H2,w5,w6))

O1ideal = 1
Error = ((1-O1)**2)/1

print(f'Результат :{O1} . Ошибка : {Error}')