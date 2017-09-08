with open('sachintendulkar.txt') as f: #Reading the file
    data=f.read()
f.closed
print(data)
datalist = data.split()   #Splitting the words in the file into lists

datafreq = []
for w in datalist:                           #looping through the words in the file
    datafreq.append(datalist.count(w))

print("\nParagraph\n" + data +"\n")                 #Printing the output
print("List\n" + str(datalist) + "\n")
print("Frequencies\n" + str(datafreq) + "\n")
print("Words along with their frequency\n" + str(list(zip(datalist, datafreq))))
