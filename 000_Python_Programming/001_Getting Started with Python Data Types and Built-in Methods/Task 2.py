
# coding: utf-8

# In[ ]:

#below codes are all same as task 1 for user's input texts  till "..............................." line :

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
#......................................................................................................................

output_str2 = "" #Define string for the output sentences line by line.

output_str2 = (input_list [0]+"\n"+ input_list [1]+"\n"+ input_list [2]+"\n"+ input_list [3]+"\n"+ input_list [4])
#pick up the first 5 items in the and concatenate them with "\n" between into output_str2.
#the first 5 items are the first 5 sentences of user's input.
#the string has these 5 sentences line by line as the character "\n" seperated each sentences as a newline.

print ("The first 5 lines of your input in individual sentences:" + "\n" + output_str2)
#to display the output string 2.
#5 sentences of user's input show individually on the screen, line by line. 

character_list = []#Define a list for storing each character from the 5 sentences.
punctuation_tuple = (",","!","?",".",";",":")#Define a tuple for punctuation mark.
token_str = "" #Define a string for storing all tokens and whitespace.
token_list = ""#Define a string for storing tokens only.

for character in output_str2: #for loop to check each character's type.
    if  character in punctuation_tuple:#if character is punctuation mark. 
        character_list.append(' ') #append a whitespace to the character_list.
        character_list.append(character)# follwed by appending the character to the character_list.
    elif character == "\n":#if character is "\n".
        character_list.append(' ')#replace it by append a whitespace to character_list
    else:
        character_list.append(character)#append character to the character_list.

token_str = "".join(character_list) #items in character list join together as a string.
                                    #with tokens and whitespace in the string.

token_list = token_str.split ()#apply split() to the string to exclud the whitespace.
                               #return a list contains tokens only.

print ("Total number of tokens:", len(token_list)) #display the unmebr of tokens on the screen.


# In[ ]:



