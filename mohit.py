start=open("E:\\parul\\old\\vishnu.txt","w")
start.write("hello mohit \n i am vishnu \n how are you")
start.close()
cout=0
str1=""
start=open("E:\\parul\\old\\vishnu.txt","r")
red=start.read()
lis=red.split("\n")
print(lis)
for i in lis:
    cout=cout+1
print(cout)
lis.reverse()
print(lis)

start.close()
start1=open("E:\\parul\\old\\output.txt","w")

for i in lis:
    start1.write(i)
    start1.write("\n")
start1.close()
