from abc import ABC
from abc import abstractmethod

class Shape(ABC):
	def __init__(self):
		super().__init__()


	@abstractmethod
	def draw(self):
		pass
	
	
	@abstractmethod
	def area(self):
		pass

	@abstractmethod
	def perimeter(self):
		print('calc perimeter')

	def drag(self):
		print('Basic dragging functionality')

class Triangle(Shape):
	def __init__(self, a,b,c):
		self.a=a
		self.b=b
		self.c=c
	
	def draw(self):
		print(f'Drawing Triangle with sides {self.a},{self.b}, {self.c}')

	def perimeter(self):
		return self.a+self.b+self.c

	def drag(self):
		super().drag()#обращение к базовуму классу !!! 
		print('Additional actions')

	def area(self):
		return self.a+self.b




s = Triangle(10,10,10)

print(s.drag ())