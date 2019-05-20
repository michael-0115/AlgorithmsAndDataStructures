
# coding: utf-8

# In[ ]:

class StringClass: #Create StringClass
    
    def __init__(self, str_value): 
        self.str_value = str_value
        self.str_data = list ()         #Define a empty Python List
        count = int()                   #Define a integer for counting the number of characters in Python String
        
        for character in str_value:     #Use for loop to count the characters in Python String 
            count +=1                   #self.count is a class variable stored the counted number of characters in Python String
            self.count = count           
        self.str_data = [None]*self.count   #Change Python List to the number get from self.count 
                                            #So the list have the size to store all the character from Python String
        
        index = int()                      #Define an integer as a index to add the characters from Python string to Python List
        for character in str_value:         #For loop use for adding the characters to Python List one by one
            self.str_data[index]= character #Add character from [0] to end sequantly to Python List in for loop
            index +=1                      
                                           
    def linearSearch (self, target_char):     # Do the linear search by a recursive way 
        if len(self.str_data) == 0 :          # Define a base case
            self.str_data = []                 
            for i in self.str_value:             
                self.str_data.append(i)           # Reconstruct str_data object to the original content for other method used.
            return False                          # And return False when target_char not been found in the string 
        elif self.str_data [0] == target_char:
            self.str_data = []                    
            for i in self.str_value:              
                self.str_data.append(i)            # Reconstruct str_data object to the original content for other method used.
            return True                            # And return True when character found equal to the target_char 
        else:   
            self.str_data = self.str_data[1:]      #Change its state, call itself for next searching, recursively 
            return self.linearSearch(target_char)  #toward base case.
        
    def frequency (self, target_char):
        occurrence = int()           #Define an integer for counting the occurence of target_char presented in Python List
        for items in self.str_data:  #For loop used to compare the items from the first item in the list with target_char
            if items == target_char: 
                occurrence += 1      #Occurrence add 1 when a character be found the same as target_char
        return occurrence            #Return the occurrence when all items been checked
    
    def replace(self, target_char, new_char):
        for i in range(self.count):            #Class variable self.count used so the for loop will check the items                                                            #sequently with target_char in for loop without over the range of the Python List
            if self.str_data[i]== target_char: #and i is the index for sequently check
                self.str_data[i]= new_char     #Replace item if it is the same as target_char and replaced by new_char
    
    def uppercase(self):
        for i in range(self.count):            #Class variable self.count used so the for loop will check the items  
                                               #sequently for items' case type
                                               #and i is the index for sequently check
            if ord(self.str_data[i]) in range (97,122):            #Use ord() to check items in Python List is lowercase 
                self.str_data[i] = chr(ord(self.str_data[i])-32)   #And use ord()to get the lowercase's uppercase value 
                                                                   #to replace it to uppercase to let items in Python List are 
                                                                   #all uppercase 
    def lowercase(self):
        for i in range(self.count):            #Class variable self.count used so the for loop will check the items  
                                               #sequently for items' case type
                                               #and i is the index for sequently check
            if ord(self.str_data[i]) in range (65,90):             #Use ord() to check items in Python List is uppercase
                self.str_data[i] = chr(ord(self.str_data[i])+32)   #And use ord()to get the uupercase's lowercase value 
                                                                   #to replace it to lowercase to let items in Python List are                                                                      #all lowercase 
    def tokenise(self, the_delimiter):
        index_2 = int()                          #Define a integer for the index for adding tokenised items to a new list.
        tokenList = list()                       #Define a new list for store the tokenised items.
        tokenList.append ("")                    #Append a empty item first in the new list.
        
        for i in range(self.count):          #Class variable self.count used so the for loop will check the items  
                                             #sequently with the_delimiter in for loop without over the range of the Python List
                
            if not self.str_data[i]== the_delimiter:  #If item not the same as the_delimiter, 
                tokenList[index_2]+= self.str_data[i] #add items alltogether to the some index of the new list to become a
                                                      #string item
                    
            else:                                     #If item the same as the_delimiter,
                if not tokenList[index_2]== "":       
                    #(Revised) To check if the current item not none before append a new "" item to the next for adding 
                    index_2 += 1                          #index2 add 1       
                    tokenList.append ("")                 #list add 1 
                                                      #So in next loops, items will be added together to the next location in                                                         #list till the next item same same as the_delimiter encountered                                     
        return tokenList                     #For loop will process all items in the Python list and get a new list                                                          #that store with strings seperated by the_delimiter. 
    
    def __eq__(self, other):     
        
        if self.count == other.count:     #If two Python Lists are holding the same unmber of items, return False for not equal,
            for i in range(self.count):                   #then compare each item with the same index by for loop
                if not self.str_data[i]== other.str_data[i]: 
                    return False                          #Return False once items found not same between two Python Lists
            return True                                   #Return True if all items found the same between two Python Lists
        
        else:                             #If two Python Lists are not holding the same unmber of items,
            return False                                  #Return False for not equal.
        
    def __gt__(self, other):                     
        if self.count > other.count:      #If Python List 1 has more items than Python List 2
            
            for i in range(other.count):            #Firt to check all items sequently with same index in the two Lists 
                                                    #to the last item List 2 have
                if self.str_data[i] > other.str_data[i]:  #Return True once a item in List 1 greater than the same index in
                    return True                           #List 2  
                
                else:                                     #If not: 
                    if not self.str_data[i] == other.str_data[i]: #return False if the item in List 1 is not same as the same   
                        return False                              #index in List 2      
                    
            return True                             #When no True or False return within the loop, the first items they                                                             #have are all same to each other in same index, return True                                                                     #because List 1 has more items than List 2. The List 1 is greater.           
        else:                            #If Python List 1 not has more items than Python List 2      
            
            for i in range(self.count):               #First to check all items sequently with same index in the two Lists 
                                                      #to the last item List 1 have
                if self.str_data[i] > other.str_data[i]:  #Return True once a item in List 1 greater than the same index in
                    return True                           #List 2  
                
                else:                                     #If not:
                    if not self.str_data[i] == other.str_data[i]: #return False if the item in List 1 is not same as the same       
                        return False                              #index in List 2    
            return False                            #When no True or False return within the loop, the first items they                                                             #have are all same to each other in same index, return False                                                                   #because List 1 doesn't has more items than List 2. List 1 is either little                                                     #or same as List 2. 
                
    def __str__(self):  
        string = str()             #Define a string for reconstruct the items in Python List as a new string.
        for items in self.str_data:#For loop to add items one by one to the new string.
            string += items        
        return string              #Return the new string.


