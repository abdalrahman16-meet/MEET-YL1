class Animal:
	def __init__(self,name,color,age,size):
		self.name=name
		self.color=color
		self.age=age
		self.size=size
	
	def print_all(self):
		print(self.name)
		print(self.color)
		print(self.age)
		print(self.size)

	def sleeping():
		print(self.name + " is sleeping")
	
	def eating(self, food): # food here is a vaariable
		print(self.name + " is eating" ,food)



		
		

Dog=Animal(name="max",color="black",age=4,size="huge")
Cat=Animal(name="min",color="white",age=3,size="small")

Dog.print_all()
print("##########")
Cat.print_all()
print("###########")
Dog.eating("shit")
print("###########")

