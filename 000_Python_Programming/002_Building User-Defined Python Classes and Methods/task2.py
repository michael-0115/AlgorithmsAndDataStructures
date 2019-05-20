from task1 import StringClass         #Importing StringClass

class StringListClass:                #Create StringListClass
    
    def __init__(self, size):
        self.str_list = [None]*size   #Get the size from user input and initial a empty list with fixed size.
        self.count2 = int()           #Define a integer for counting the items in Python list
        self.size = size              #Get the size the user type in for the list
    
    def getListSize (self):
        return self.size              #Return the size for the fixed size list
    
    def add (self, new_item):
        self.new_item = StringClass(new_item) #Add a new_item to the list, and the new_item will go to the StringClass first
        self.str_list[self.count2]= self.new_item  #to become a StringClass object before been added to Python List.
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
    
    def binarySearch (self, target_item):  
        low = int()                      #Define a integer used to present the low place for binarySearch  
        high = self.count2 -1            #Define a integer used to present the high place for binarySearch  
        self.target_item = StringClass(target_item) #target_item will go to the StringClass first to become a StringClass object
        while not low-1 == high:                        #compare target_item with the centre item in the sorted Python list
            mid = (low + high) //2
            if self.str_list[mid] == self.target_item:  #Return True for item same as target_item
                return True                             #If item is greater than target_item, move to the right part of items 
            elif self.str_list[mid]>self.target_item:   #If item is not greater or equal to target_item, move to the left part 
                high = mid -1                           #Continute to found the items if any equal to target_item 
            else:                                       #till the first item or the last item in Python list
                low = mid +1
        return False                                    #Return False when search process end with no item been found qual to 
                                                        #target_item
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