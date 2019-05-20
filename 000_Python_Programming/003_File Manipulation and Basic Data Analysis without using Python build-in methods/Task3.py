
# coding: utf-8

# In[3]:

from new_stringclass import StringClass #Importing String Class
from new_stringlistclass import StringListClass #Importing String Class

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
  
print ("The programe will show the impletmentation of the methods inside the classess:")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Task 1, StringClass--
print ("\n"+"Task 1, StringClass--")    


#----------1.1_Initial the StringClass:----------------------------------------------
#User type in,
a = StringClass(str(input("Task 1.1 __init__: Please enter a string: ")))

#----------1.2_1.3_"linearsearch" and "frequency":-----------------------------------


#User type in, type in value shall be a character,
#if no reture Error and ask for type in again till suitable value get
b = str(input("Please enter a character: "))   
while not len(b) == 1:
    b = str(input("Error! It has to be a character, please enter again: "))
    
#assign user type in value to linearSearch method in StringClass    
c = a.linearSearch(b)  

#print out the result for linearsearch and character frequency         
if c == True:                                            
    print ("\n"+"Task 1.2 linearSearch-"+"\n"+"Character",b, "you enter is in String",str(a),"you enter.")
    d = a.frequency(b)
    print ("\n"+"Task 1.3 frequency-"+"\n"+"The number of occurrences for Character",b, "in String", str(a), "is:",d)
     
else:                                          
    print ("\n"+"Task 1.2 linearSearch-"+"\n"+"Character",b, "is not in String", str(a),".")
    d = a.frequency(b)
    print ("\n"+"Task 1.3 frequency-"+"\n"+"So the number of occurrences for Character",b,"in String",str(a),"is:",d)
                                        
        
#-------1.4_1.5_1.6_1.9_ "replace", "lowercase", "uppercase" and "__str__"---------- 


#Uesr type in, type in value shall be a character
#and in the Python string list for the replace, 
#if no returen Error and ask for type in again till suitable value get
e = str(input("Please enter a character you want to replace: "))
while not len(e) == 1:
    e = str(input("Error! It has to be a character, please enter again: "))   
while a.linearSearch(e) == False:
    e = str(input("The character you entre is not in the string you type in, please type another: "))

#Uesr type in, type in value shall be a character
#if no returen Error and ask for type in again till suitable value get   
f = str(input("Please enter a character for the replacement: "))
while not len(f) == 1:
    f = str(input("Error! It has to be a character, please enter again: "))

#assign two type in value to the replace method in StringClass (one for the replace character, the other for character change to
g = a.replace(e,f)

#print result for replacement 
print ("\n"+"Task 1.4 replace and 1.9 __str__-"+"\n"+"The string has been replaced to:", str(a))

#call uppercase method
#print result for uppercase 
i = a.uppercase()
print ("\n"+"Task 1.6 uppercase and 1.9 __str__-"+"\n"+"The string has been tansfered to all uppercase:", str(a))

#call lowercase method
#print result for lowercase 
h = a.lowercase()
print ("\n"+"Task 1.5 lowercase and 1,9 __str__-"+"\n"+"The string has been tansfered to all lowercase:", str(a))


#-------1.7_"tokenise", ------------------------------------------------------------- 


#Uesr type in, type in value shall be a character
#if no returen Error and ask for type in again till suitable value get   
j = str(input("Please enter a delimiter that will be used to splits the string: "))
while not len(j) == 1:
    j = str(input("Error! delimiter has to be a character, please enter again: "))

#assign type in value as delimiter to tokenise method in StringClass
j1 = a.tokenise(j)

#print result for tokenise
print ("\n"+"Task 1.7 tokenise-"+"\n"+"The result as", j1)


#-------1.8_"__eq__", ---------------------------------------------------------------- 


#User type in (initial another StringClass Object
a2 = StringClass(str(input("Please enter a string, the program will check if it is equal to string " + str(a)+" :")))

#call __eq__ method
#print result if StringClass Object 1 is equal to StringClass Object 2 or not
if a == a2:
    print ("\n"+"Task 1.8 __eq__-"+"\n"+ str(a), "is the same as "+ str(a2))
else:
    print ("\n"+"Task 1.8 __eq__-"+"\n"+ str(a), "is not the same as "+ str(a2))
    

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


#Task 2, StringListClass--
print ("\n"+"Task 2, StringListClass--") 

#----------2.1_Initial the StringClass:--------------------------------------------


#User type in, type in value shall be a numebr from 1 to 9,
#if no reture Error and ask for type in again till suitable value get
size = str(input("Create a list by entre a number with a fixed size. Please key in a number"))
while not len(size) == 1 or ord(size) not in range(49,57) :
    size = str(input("Error, size shall be number 1 ~ 9, please type again: "))
    if len(size) == 1:
        if ord(size) in range(49,57):
            break
    else:
        size = str(input("Error, size shall be number 1 ~ 9, please type again: "))
        
#assign type in number to the StringListClass to initial a empty list with fiexd size        
StringListObject =StringListClass(int(size))

#print result for empty list been created
print ("\n"+"Task 2.1 __init__-"+"\n"+"Eempty list has been created with its lenth =",(len(StringListObject)),".",
       "Please add",str(StringListObject.getListSize()),"strings to the list:")



#----------2.2_2.4_2.6_"add","bubbleSort" and "__len__"--------------------------------------------


#Uesr type in string and add to the StringListClass
#while loop for collect uesr type in strings for adding to the Python list in StringListClass
#number of string to be type in depend on the size of list user type in earlier
addString = StringListObject.add(str(input("\n"+"please enter a string: "))) 
while len(StringListObject) < StringListObject.getListSize():
     addString = StringListObject.add(str(input("please enter another string: ")))    
print ("\n"+"Task 2.2 add-"+ str(len(StringListObject)),"strings added in to the list.") 
    
#Call bubbleSort method in StringListClass
StringListObject.bubbleSort()

#print result for bubbleSort and __len__ method
print ("\n"+"Task 2.4 bubbleSort, __gt__ in stringClass and 2.7 __str__-"+"\n"+"Items you type in sorted, and output as below:","\n"+
       str(StringListObject))
print ("Task 2.6 __len__-"+"\n"+"The total number of items in list now is:",len(StringListObject))

 
    
#----------2.3_2.5_"remove","binarySearch"--------------------------------------------

#Uesr type in for binarySearch and remove test
targetItem = str(input("\n"+"Enter a string as a target item to test binary search with the sorted list and remove it from the list: "))

#aasign type in value to binarySearch in StringListClass
binarySearch = StringListObject.binarySearch(targetItem)

#if value found in StringListObject after searching, remove it from the 
#StringListObjectby assigning it to remove method in StringListClass
#and print the result for binarysearh and remove
if binarySearch == True:                     
    StringListObject.remove(targetItem)
    print ("\n"+"Task 2.5 binarySearch and 2.3 remove-"+"\n"+"The string you type in is in the list and now has been removed. List items been changed to:",
           "\n"+ str(StringListObject))  
    
#if value not found in StringListObject after searching,
#print the result for binarysearh and remove without call remove method in StringListClass as no item need to be removed
else:                      
    print ("\n"+"Task 2.5 binarySearch and 2.3 remove-"+"\n"+"The string you type in is not in the list. List items remain no changed as below:",
           "\n"+ str(StringListObject))      


#-------------end---------------------






# In[2]:

#Unittest----
import unittest                      # Import unittest

#test_linaerSearch method in StringClass
class Test_StringClass_linearSearch(unittest.TestCase): 
    
    def setUp(self):                                    #Set up a class object
        self.a = StringClass("michael")
    def test_True(self):
        self.assertTrue (self.a.linearSearch ("a"))     #True for a value in class object
    def test_False(self):
        self.assertFalse (self.a.linearSearch ("z"))    #False for a value not in class object
        
#test_BinarySearch method in StringListClass        
class Test_StringListClass_BinarySearch(unittest.TestCase):
    
    def setUp(self):                                     #Set up a class object
        self.b = StringListClass(3)                         
        self.b.add("michael") 
        self.b.add("Jordan") 
        self.b.add("No.23") 
    def test_True(self):
        self.assertTrue (self.b.binarySearch ("Jordan"))   #True for a value in class object
    def test_False(self):
        self.assertFalse (self.b.binarySearch ("No.29"))   #False for a value not in class object

suite = unittest.TestLoader().loadTestsFromTestCase(Test_StringClass_linearSearch)
unittest.TextTestRunner().run(suite)

suite = unittest.TestLoader().loadTestsFromTestCase(Test_StringListClass_BinarySearch)
unittest.TextTestRunner().run(suite)



# In[ ]:



