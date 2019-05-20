
# coding: utf-8

# In[1]:

#Define a function for tect clean process:
def clean (file, cleaned_file_folder , filename):
    try: 
        read_file = open(file, "r")       #Open file for read 
        
    except FileNotFoundError as error: 
        print (error)                    #Raise and error when file not found
        
    else:                                #If file opend successfully, continue to the function process
        contents_list = []       #Define a empty list for storing file's content.
        contents_list = read_file.readlines() # Read file's contents in line and return them to the list.
        
        len_contents_list = len(contents_list)  # len() to get the lines number in the list.
        child_statments_list = []     # Define a empty list to store line which belong to the child's statements.
        n = 0                  # Define an integer to use in below while loop for item location in contents_list. 
        
        while n <= len_contents_list-1:        # While loop for checking each line in the contents_list. 
            if "CHI:" in contents_list[n]:           #Pick lines that have prefix "*CHI:" 
                child_statments_list.append(contents_list[n])   
                n += 1
                if not "%" in contents_list[n]:      #and it's extend line which it's the next line not start with "%".
                    child_statments_list.append(contents_list[n])
                    n += 1
            else:
                n +=1      
                
        #Lines processing-------------------------------------------------
        
        #A. To strip the prefix "*CHI:"    
        CHI_stripped_list = []                         # Define a empty list to store stripped lines
        for line in child_statments_list:              # To strip the prefix "*CHI:" for lines
            CHI_stripped_list.append(line.strip("*CHI:")) # and to add into a new list: CHI_stripped_list
            
        #B. To strip tab "\t"
        tab_stripped_list = []                        # Define a empty list to store stripped lines.
        for line in CHI_stripped_list:                 # To strip tab "\t" for lines
            tab_stripped_list.append(line.strip("\t")) # and to add into a new list: tab_stripped_list.
        
        #C. To divide content to words and store to word_list
        temp_list = []                          #Defind a empty temporary list and store lines with
        for line in tab_stripped_list:          #"\n" been replaced by " \n ".
            line = line.replace ("\n"," \n ")   
            temp_list.append(line)
        lines_string = "".join(temp_list)       #Join lines to a single string and split it with " " to get 
        word_list= lines_string.split(" ")      #a list call word_list that stored all words seperately.
        word_list.pop()                         #Delete the last null item in the list, this null in the last item 
                                                #is created when using split " " to split the a string
                                    
        
        #Words processing-------------------------------------------------
        
        retain_symbols_list = ["[//]","[/]","[*]","(.)","(..)","(...)"]   
                                         #Define a list contain symbols that we want to retain.
        remove_symbols_list = ["/","-","(",")"]                      
          #Define a list contain symbols that we want to remove from a word that are not equal to any items in symbols_list.
        
        
        #a. To remove "/","-","(",")" except words == "[//]","[/]","[*]","(.)","(..)","(...)"
        a_list = []                            #Define a list for storing word been processed for #a.
        for word in word_list:
            if word in retain_symbols_list:    #Keep word that equal to any items in symbols_list add it to a_list.
                a_list.append(word) 
            else:                              #If word not in symbols_list, 
                new_word = str()               
                for character in word:         
                    if character not in remove_symbols_list:  #removed word's character for any symbols in remove_symbols_list 
                        new_word += character                #as a new word and add it to a_list.                          
                a_list.append(new_word)  
           
        #b. To remove word have either prefix "+" or "&"
        b_list = []                            #Define a list for storing word been processed for #b.
        for word in a_list:
            if word[0] == "+":
                b_list = b_list
            elif word[0] == "&" :
                b_list = b_list
            else:                            #Add word to b_list only if its prefix is neither "+" or "&"
                b_list.append(word)  
               
            
        #c. To remove words/characters between "[" and "]" but retain words == "[//]","[/]","[*]" .       
        len_b_list = len (b_list)
        n=0
        c_list = []                      #Define a list for storing word been processed for #c.
        while n <= len_b_list-1:
            if b_list[n] in retain_symbols_list:         #Retain word == "[//]","[/]","[*]" and add to c_list.     
                c_list.append(b_list[n])
                n+=1
            elif "[" in b_list[n] and "]" in b_list[n]:  #Remove words that have "[" and "]" but not == "[//]","[/]","[*]" 
                n+=1                                     #like "[/-]".
            elif "[" in b_list[n]:
                n+=1
                while "]" not in b_list[n]:             #Remove words between "[" and "]" but not == "[//]","[/]","[*]" 
                    n+=1                                #like "[abc def ghi]".
                n+=1
            else:
                c_list.append(b_list[n])                #Retain the rest words  and add to c_list.
                n+=1
                
        #d. To remove prefix "<"  and suffix ">"  from words
        len_c_list = len (c_list)
        e_list =[]                     #Define a list for storing word been processed for #d.   
        n=0
        while n <= len_c_list-1:
            if  c_list[n][0] == "<":                   #Remove prefix "<" for a word and add to e_list.
                e_list.append(c_list[n].strip("<"))
                n+=1
            elif c_list[n][-1] == ">":                 #Remove suffix ">" for a word and add to e_list. 
                e_list.append(c_list[n].strip(">"))
                n+=1
            else:
                e_list.append(c_list[n])               #Retain the rest words  and add to e_list.
                n+=1

        #e. File clean finished -------------------------------------------------
        
        cleaned_string = " ".join(e_list)             #Join words together with " " to a string.
        cleaned_string = cleaned_string.replace("\n ","\n") 
                  #Replace"\n " in string with "\n" to get cleaned file contains cleaned child statements in lines.
            
        outputfile = cleaned_file_folder +"/"+ filename[0:-4]+"_cleaned.txt"   #Define a file pathname and
        output_file = open (outputfile, "w")                        #create file to write cleaned lines to the file.
        for line in cleaned_string:
            output_file.write(line)

        read_file.close()                             #Close read_file
        output_file.close()                           #Close output_file

        
#Define a function for creating a directory
def make_dir(path):
    try:                                           
        os.makedirs(path, exist_ok=True)                       #Create a new directory
    except TypeError as error:
        if exc.errno == errno.EEXIST and os.path.isdir(path):   #If directory already exit, pass the make_dir function
            pass
        else: 
            raise                                               #else, raise error 
            print (error)
            
#---------------------------------------------------------------------------------------------------------------------           
import glob       # Import glob                 
import os         # Import os       
import errno      # Import errno     

#For Group SLI:

#Make a new directory for SLI cleaned file
cleaned_file_folder = "SLI cleaned"   #Assign a folder path name for make_dir function to 
make_dir (cleaned_file_folder)                                      #create a directory for store the SLI cleaned files.

#Start file cleaning
input_folder = glob.glob(r"SLI/*.txt")  #Grab pathname for SLI files in a folder
for file in input_folder:                                         #For loop to call clean function to clean each file.
    filename = os.path.basename(file)                             # (In the clean function, file will be cleaned and 
    clean (file, cleaned_file_folder, filename )                  # out up to a new file)

#For Group TD:

#Make a new directory for TD cleaned file:
cleaned_file_folder = "TD cleaned"   #Assign a folder path name for make_dir function to 
make_dir (cleaned_file_folder)                                     #create a directory for store the SLI cleaned files.

#Start file cleaning
input_folder = glob.glob(r"TD/*.txt")  #Grab pathname for TD files in a folder
for file in input_folder:                                         #For loop to call clean function to clean each file.
    filename = os.path.basename(file)                             # (In the clean function, file will be cleaned and 
    clean (file, cleaned_file_folder, filename )                  # out up to a new file)
                                          


# In[ ]:



