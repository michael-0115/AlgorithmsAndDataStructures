
# coding: utf-8

# In[ ]:

input_str = "" #define string for storing the input.
input_list = "" #define list for storing the input by sentences.
output_str = "" #define string for the output.
delimiter_tuple = (".","?","!") #define a tuple for delimiter.

input_str = input ("To input a number of lines of text:" + "\n")# prompt the user for the input.

while input_str.count(".") + input_str.count("?") + input_str.count("!") < 5:#while loop to count the total delimiters.                                                                         
    input_str += " " + input ("There is no 5 sentences, please type more lines:" + "\n")
    #prompt the user for another input when total delimiters is less than 5.
    #user's input concatenate with the previous input.
    #while loop end if total delimiters is not less than 5.
    
for character in delimiter_tuple:#replace whitespace after each delimiter by a "#".  
     if character in input_str:
        input_str= input_str.replace ( character + " ", character + "#" )
        
input_list = input_str.split ("#")# split "#" from input string to input list. 
                                  # each item in the list is a sentence from uesr's input. 
    
output_str = (input_list [0] + " " + input_list [1] + " " + input_list [2] + " " + input_list [3] + " " + input_list [4])
#pick up first 5 items in input list and concatenate them with whitespace between into the defined output string. 
#the first 5 items in input list are the first 5 sentences of user's input.
#output sting is a single string that contain the first 5 sentences from user's input.

print ("The first 5 lines of your input:" + "\n" + output_str) #display the output string.


# In[ ]:



