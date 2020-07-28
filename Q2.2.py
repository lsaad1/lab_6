import binascii

def dehexify(hexfile):
	Input = open(hexfile, "r").read()
	dehex = binascii.hexlify(Input)
	print(dehex)

dehexify("Q2.2_hex.txt")

