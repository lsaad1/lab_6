
from os import system
readfilename=raw_input("Enter the file name to read: ")
data=open("{0}".format(readfilename),"rb").read()#read mode
writefilename=raw_input("Enter the file name to write: ")
f=open("./{0}".format(writefilename),"wb")#write mode
f.write(data)
f.close()
print("exicuting the binary file..")
system("chmod 777 Q1.results.txt;")

