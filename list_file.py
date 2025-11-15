filename = "copy.txt"    
lines_list = []             
with open(filename, "r") as file:
    for line in file:
        lines_list.append(line.strip())   
print("Lines in the list:")
print(lines_list)
