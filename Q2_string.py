import binascii
Input = raw_input("Enter a string: \n")
def StringtoBinary(Input):
	Binary = []
	for b in Input:
		ascii_value = ord(b)
		Binary_value = bin(ascii_value)
		Binary.append(Binary_value[2:])
	return(' '.join(Binary))
print(StringtoBinary(Input))
