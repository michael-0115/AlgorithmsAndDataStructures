
# coding: utf-8

# In[ ]:

from new_stringclass import StringClass #Importing String Class


class StringListClass:                #Create StringListClass
    
    def __init__(self, size):
        self.str_list = [None]*size   #Get the size from user input and initial a empty list with fixed size.
        self.count2 = int()           #Define a integer for counting the items in Python list
        self.size = size              #Get the size the user type in for the list
        self.str_list_temp = []       #New_Add: 
                                      #Define a temporary list to store the same stringlistclass object to another object
                                      #for the purpose of using resursion in binarysearch as the method will desconstruct 
                                      #the object. So having this self.str_list_temp object can be used to reconstruct 
                                      #the original stringListClass object in the binarysearch method.
    def getListSize (self):           
        return self.size              #Return the size for the fixed size list
    
    def add (self, new_item):
        self.new_item = StringClass(new_item) #Add a new_item to the list, and the new_item will go to the StringClass first
        self.str_list[self.count2]= self.new_item         #to become a StringClass object before been added to Python List.
        self.str_list_temp.append (self.new_item)   #New_Add: 
                                                    #Add each value to the self.str_list_temp object as well 
                                                    #for the object reconstruct used.      
        self.count2 += 1                      #self.count2 add 1 when one object been added to the Python List.
        
    def remove (self, target_item): 
        number1 = int()                   #Number1 as index of item to be used to compare object in list from first to end. 
        number2 = int()                   #Number2 as index used to move items location in Python list.
        number21 = self.size -1           #Number21 for the loop not change the next index item when it is in the last item
        self.target_item = StringClass(target_item) #target_item will go to the StringClass first to become a StringClass object
        for items in range(self.size):  #Compare every item in Python list with target_item in for loop
                                                          #Items go to the StringClass to compare if are same as each other,
            if self.str_list[number1] == self.target_item:#If item same as target_item, all items after that item               
                number2 = number1                         #will be move one index to the left and the item ifself            
                for items in range(number21):             #will be moved to the end of list, Number21 applied in the range here
                    self.str_list[number2] = self.str_list[number2+1]
                    number2 +=1
                self.str_list[number2] = None             #and be replace by a None for removal.
                self.count2 -=1                           #self.count2 reduce 1 if one item been removed 
            else: 
                number1 +=1                          #number1 add 1 for the next item in Python list to process the above
                number21 -=1                        #compare and remove process in for loop
                                                     #when go to the next item in list, number21 minus 1 as the
                                                     #compare and check process for the next items reduce 1 time
    def bubbleSort(self):
        number3 = self.count2-1           #number3 to set how many sorting action need to be proceed, deceide by the number of
        for item in range(self.count2-1): #which is the total number of items in List minus 1 based on bubble sorting concept
            number4 = int()               #number4 as index control where the items to be move and stored for sorting process.
            for item in range(number3):   
                if self.str_list[number4] > self.str_list[number4+1]:  #following the bubble sorting method to sorting the items
                    temp = self.str_list[number4]                      #in an ascending order
                    self.str_list[number4] = self.str_list[number4+1]
                    self.str_list[number4+1] = temp
                number4 +=1
    
    def binarySearch (self, target_item):                   # Do the binary search by a recursive way. 
        self.target_item = StringClass(target_item)
        low = 0                                                 
        high = len(self.str_list) -1 
        if len(self.str_list) == 0:                         # Define a base case.
            self.str_list = self.str_list_temp      # Reconstruct str_data object to the original content for other method used by
            return False                                    # assigning self.str_list_temp to the self.str_list object.
                                                            # And return False when target_item not been found in the list. 
        else:           
            midpoint = (low + high) //2                          
            if self.str_list[midpoint] == self.target_item:
                self.str_list = self.str_list_temp  # Reconstruct str_data object to the original content for other method used by
                return True                                  # assigning self.str_list_temp to the self.str_list object.
                                                             # And return True when character found equal to the target_char.
            else:
                if self.str_list[midpoint]>self.target_item: #Go to the left part of the list if target_item 
                                                             #little than the list middle item.
                    self.str_list = self.str_list[:midpoint] #Change its state, call itself for next searching, recursively.
                    return self.binarySearch (target_item)       
                else:     
                    self.str_list = self.str_list[midpoint+1:]  #Go to the right part of the list if 
                                                                #target_item not little than the list middle item.
                    return self.binarySearch (target_item)      #Change its state, call itself for next searching, recursively. 
    def __len__ (self):
        return self.count2  #return self.count2 as the number of items in the Python list.
        
    def __str__ (self):
        string = str()      #Define a new string to store the items from Python list
        number6 = int()         #Define a integer to control the index in the list for adding them in order to a new string
                            #with a newline command between each list items, so the new string will have a output show strings
        for items in range(self.count2): #in different line.
            string += str(self.str_list[number6])  
            string += "\n"
            number6 += 1
        return string 


