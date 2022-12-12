import random
import string


# Get random Name Generator
def get_random_generator():
    random_source = string.ascii_letters + string.digits
    return ''.join(random.choice(random_source) for _ in range(10))
    
 

#user should enter the department name
departments = input( "Please can you enter the Department name to which you belong : Finance, Production, Operation: ")

#listing the choice of the department name
for _ in departments :

    if departments == "Finance" or departments.lower() == "finance" :
        break

    elif departments == "Production" or departments.lower() == "production" :
         break

    elif departments == "Operation" or departments.lower() == "operation" :
         break

    else:
        print(" ")
        print("the writting departments name is incorrect, please enter the following Department name describe below: ")
        departments = input("Finance, Production, Operation: ")
	    

#The number of EC2 instances that the Operateur can enter and print the unique name of the EC2 instance
print(" ")
EC2_number = int(input("Please enter the number of EC2 instances that you need: "))
print(" ")

if EC2_number > 0:
	   print("Bellow the following EC2 Instance: ")
	   print(" ")
	    
for _ in range(1, EC2_number + 1):  
	    
    		string_name = departments  
    		
    		EC2_name = string_name + "-" + get_random_generator()
    		
    		print(EC2_name)
    		
# c'est parfait	!