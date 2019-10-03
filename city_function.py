
def city_function(city , country , population=''):
	city = city.capitalize()
	country = country.capitalize()
	population = str(population)
	if population:
		full =f'{city}, {country} {population}'
	else:
		full =  f'{city}, {country}'

	return full
