# File-based-key-value-data-store-CRUD
[![Python Version](https://img.shields.io/badge/python-3.8.2-brightgreen.svg)](https://python.org)  [![Dev](https://img.shields.io/badge/Ayushman's-Build-yellowgreen)](https://github.com/Ayushman09)<br>

### Note: The task was to do just CRD but I have added Update for complete CRUD
This is a file which can be exposed as a library that supports the basic CRUD(Create, Read, Update, Delete) operations.
Data store is meant to local storage for one single process on single laptop

<b>The data store will support the following :</b>
<b>Functional Requiurements:</b> 
1. It can be initialized using an optional file path. If one is not provided, it will reliably create itself in a reasonable location on the laptop.
2. A new key-value pair can be added to the data store using the Create operation. The key is always a string - capped at 32chars. The value is always a JSON object - capped at 16KB.
3. If Create is invoked for an existing key, an appropriate error must be returned.
4. A Read operation on a key can be performed by providing the key, and receiving the 
value in response, as a JSON object.
5. A Delete operation can be performed by providing the key.
6. Every key supports setting a Time-To-Live property when it is created. This property is optional. If provided, it will be evaluated as an integer defining the number of seconds the key must be retained in the data store. Once the Time-To-Live for a key has expired, the key will no longer be available for Read or Delete operations.
7. Appropriate error responses must always be returned to a client if it uses the data store in unexpected ways or breaches any limits
<b>Non Functional requirements:</b>
1. The file size never exceeds 1GB
2. The file is accessed by multi-threading
3. Returns "invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,
4. Returns "key doesnot exist" if key_name was mis-spelt or deleted earlier or never existed

Go through the task.py file and screenshots in "sample" directory. These are attached here in order to understand clearly how 
the code works and how to perform operations in this. 


# Demo Output
<img src = 'https://github.com/Ayushman09/file-based-key-value-data-store-CRD/blob/main/Sample/sample1.jpg' width=''/> </br>
<img src = 'https://github.com/Ayushman09/file-based-key-value-data-store-CRD/blob/main/Sample/sample2.jpg' width=''/> </br>
<img src = 'https://github.com/Ayushman09/file-based-key-value-data-store-CRD/blob/main/Sample/sample3.jpg' width=''/> </br>


## Credits
[Ayushman09](https://www.github.com/Ayushman09)
