'''
This file is to display the use of the script.
This is the file made of the sample interactive mode.
all outputs are declared as comments below each line of code respectively.
'''


import main as m
#imported the main file as a library

#creating key-value pair data to store in local system
m.create("Ayushman",20)
#Key Ayushman with value 20 creation successful!

res = m.read("Ayushman") #returns JSON object
print(res)
#Ayushman:20

#if entered duplicate key, shows error
m.create("Ayushman",25)
#error: this key already exists

#Using TIME-TO-LIVE property
m.create("Hyderabad",50,120) #time-120 seconds
#Key Hyderabad with value 50 creation successful!
res = m.read("Hyderabad")
print(res)
#Hyderabad:50


#after 120 seconds
res = m.read("Hyderabad")
#error: time-to-live of Hyderabad has expired

#lets UPDATE data
m.update("Ayushman",25)
#Value for Ayushman updated to 25
res = m.read("Ayushman")
print(res)
#Ayushman:25

#to delete data and free memory
m.delete("Ayushman")
## key Ayushman is successfully deleted
print(m.read("Ayushman"))
#error: given key does not exist in database. Please enter a valid key


#entering wrong key name
res = m.read("asdf")
#error: given key does not exist in database. Please enter a valid key

#wrong key name while creation
m.create("as@df",10)
#error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers

'''
#we can access these using multiple threads like
t1=Thread(target=(m.create or m.read or m.delete),args=(key_name,value,timeout)) #as per the operation
t1.start()
t1.sleep()
t2=Thread(target=(m.create or m.read or m.delete),args=(key_name,value,timeout)) #as per the operation
t2.start()
t2.sleep()
#add upto tn
'''
#This code also returns other errors:  
#"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,
#"key doesnot exist" if key_name was mis-spelt or deleted earlier
#"File memory limit reached" if file memory exceeds 1GB
