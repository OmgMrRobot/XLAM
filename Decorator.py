from timeit import default_timer as timer
import math
import time


def measure_time(func):
	def inner(*args, **kwargs):
		start = timer()

		func(*args, **kwargs)

		end = timer()

		print(f'Func {func.__name__} took {end-start} for execution')
	return inner

@measure_time  #С помощью этого декоратора можем замерять время любой функции
def factorial(num):
	time.sleep(4)
	print(math.factorial(num))

factorial(3)