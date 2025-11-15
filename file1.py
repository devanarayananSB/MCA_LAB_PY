file1 = input("Enter the source file to be copied: ")
file2 = input("Enter the destination file name: ")
fr = open(file1, "r")
fw = open(file2, "w")
for line in fr.readlines():
    fw.write(line)
fr.close()
fw.close()
print("File copied successfully!")
