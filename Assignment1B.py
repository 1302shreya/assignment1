#Regex used to remove or strip off special characters like , . etc. attached with the word
import re 

#Function for removing special characters from each element(string) in the given list
def remove_special_characters(a): 
	b=[]
	for i in a:
		i=i.lower()
		i=re.sub('\W+','',i)
		b.append(i)
	return b
			


f_in=open('input.txt','r') #Read input file using file object
line=f_in.readline() #Take input line by line from the input file
master=[] #List for maintaining the distinct words
while line!='':
	temp=line.split(" ") #List used for temporarily storing the words in a line
	temp=remove_special_characters(temp) #Special characters removed from the words/elements in temp
	master=master+temp #After special characters are removed, add the temp list to master list
	line=f_in.readline() #Read new line

f_in.close()

counter=list(set(master)) #Remove repetitions to yield distinct words by converting into set 
Count={} #Dictionary used for maintaining distinct words and their respective counts

for i in counter:
	num=master.count(i)
	Count[i]=num

#print(Count)
f_out=open('output.txt','w') #File object for writing into file output.txt
for i in sorted(Count):
	if i!='':
		string=i+","+str(Count[i])+"\n" #The format specified in the question
		f_out.write(string) #Writing to the file

f_out.close()
