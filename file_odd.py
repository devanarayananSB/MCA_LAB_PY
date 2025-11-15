source = "meow.txt"
destination = "oddlines.txt"
f1 = open(source, "r")
f2 = open(destination, "w")
line = f1.readlines()        

for i in range(0, len(line)):
    if i % 2 == 0:        
        f2.write(line[i])
f1.close()
f2.close()
print("Odd lines copied successfully!")
