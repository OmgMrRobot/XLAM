

rom_numbers = {}
rom_numbers["I"] = 1
rom_numbers["V"] = 5
rom_numbers["X"] = 10
rom_numbers["L"] = 50
rom_numbers["C"] = 100
rom_numbers["D"] = 500
rom_numbers["M"] = 1000

# for k,v in rom_numbers.items():
# 	print(f"{k}-->{v}")

def number(num):
	result = 0
	for i, c in enumerate(num):
		if i+1<len(num) and rom_numbers[num[i]] < rom_numbers[num[i+1]]:
			result= result- rom_numbers[num[i]]
		else:
			result=result+rom_numbers[num[i]]
	return result

print(number(input(">>>")))