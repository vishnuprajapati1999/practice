start=open("E:\\parul\\old\\vishnu.txt","w") #open a file in write mode
start.write("hello mohit \n i am vishnu \n how are you") #write content in file which we want reverse in other file
start.close() #file closed
cout=0 #declare counter

start=open("E:\\parul\\old\\vishnu.txt","r") #for count number of lines open file in read mode 
red=start.read() #read file as string
lis=red.split("\n") #spilting string by new line
print(lis)
for i in lis: #list in for loop for count number of line
    cout=cout+1 #count lines
print(cout)
lis.reverse() #reverse the list
print(lis)

start.close() #file closed
start1=open("E:\\parul\\old\\output.txt","w") #open a new file in a write mode for save output

for i in lis: #iterate loop for reverse list 
    start1.write(i) #write reverse string in file
    start1.write("\n") #new line
start1.close() #file closed
