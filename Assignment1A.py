import re
import logging
import datetime

def validate(password):
	flag=0
	reasons=""
	if re.findall('[a-z]',password)==[]:  #checking condition for presence of lowercase letter
		flag=1
		reasons+=" Lower case letter absent."
	if re.findall('[A-Z]',password)==[]:  #checking condition for  presence of uppercase letter
		flag=1
		reasons+=" Upper case letter absent."
	if re.findall('[0-9]',password)==[]:  #checking condition for presence of a digit
		flag=1
		reasons+=" Digit absent."
	if re.findall('[$#@]',password)==[]:  #checking condition for presence of a special character (@,# or $)
		flag=1
		reasons+=" Special character(#,@ or $) absent"
	if len(password)<5: #checking condition for length
		flag=1
		reasons+=" Length under the limit."
	if len(password)>13:
		flag=1
		reasons+=" Length over the limit."
	if flag==0:
		print("Valid ")
		return "Valid"
	else:
		mystring="Not Valid because: "+reasons
		print("Not Valid ")
		return mystring
		

if __name__=="__main__":
	password=input("Enter your password: ") #Compiled using python3, so used input instead of raw_input
	output=validate(password)
	#print(output)

	log_filename='Assignment1A.log'
	'''logging.basicConfig(filename=log_filename,filemode='w',level=logging.DEBUG)
	string=password+",  "+output+",  "+str(datetime.datetime.now())+"\n"
	
	logging.debug(string)'''
	logging.basicConfig(filename='example1.log',level=logging.DEBUG)
	string1="Input: "+password+","+"Output: "+output
	logging.info(string1)

