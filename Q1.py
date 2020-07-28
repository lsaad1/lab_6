from os import system
readfile = raw_input("Enter the file name you want to read: ")
Input = open("{0}".format(readfile),"rb").read()
writefile = raw_input("Enter the file name you want to write: ")
f = open("./{0}".format(writefile),"wb")
f.write(Input)
f.close()
print("Processing Binary File...")
system("chmod 777 Q1.results.txt;")

