"""
Read from file A
write contents of file A to file B

"""
#a simple script that reads from one file and
#copies the contents to a new file, before printing the data.
in_file=open("/home/jason/Documents/simpletxt", "r")
cont=(in_file.read())
out_file=open("/home/jason/Documents/blanktxt", "w")
out_file.write(cont)
in_file.close()
out_file.close()
out_file=open("/home/jason/Documents/blanktxt", "r")
print(out_file.readlines())
