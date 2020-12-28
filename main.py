from threading import *
import time

db={} #'db' is the database, dictionary in which we store data

#for create operation 
#use syntax "create(key_name,value,timeout_value)" timeout is optional you can continue by passing two arguments without timeout

def create(key,value,timeout=0):
    if key in db:
        print("error: this key already exists") #error message1
    else:
        if(key.isalpha()):
            if len(db)<(1024*1020*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    db[key]=l
                print("Key",key,"with value",value,"creation successful!")
            else:
                print("error: Memory limit exceeded!! ")#error message2
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")#error message3

#for read operation
#use syntax "read(key_name)"
            
def read(key):
    if key not in db:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        b=db[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the present time with expiry time
                stri=str(key)+":"+str(b[0]) #to return the value in the format of JasonObject i.e.,"key_name:value"
                return stri
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            stri=str(key)+":"+str(b[0])
            return stri

#for delete operation
#use syntax "delete(key_name)"

def delete(key):
    if key not in db:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        b=db[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del db[key]
                print("key is successfully deleted")
            else:
                print("Error: time-to-live of",key,"has expired") #error message5
        else:
            del db[key]
            print("key",key,"is successfully deleted")


#I have an additional operation of update in order to change the value of key before its expiry time if provided 
#use syntax "modify(key_name,new_value)"

def update(key,value):
    b=db[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in db:
                print("Error: given key does not exist in database. Please enter a valid key") #error message6
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                db[key]=l
        else:
            print("Error: time-to-live of",key,"has expired") #error message5
    else:
        if key not in db:
            print("Error: Key does not exist in database. Please enter a valid key") #error message6
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            db[key]=l
            print("Value for",key,"updated to",value)
