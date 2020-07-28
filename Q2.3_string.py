import binascii
Input = raw_input("Enter a string: \n")
binary=binascii.a2b_base64(Input.strip())
print("Convert to binary: " + binary)
string = binascii.b2a_base64(binary)
print("Binary to string" + string)
