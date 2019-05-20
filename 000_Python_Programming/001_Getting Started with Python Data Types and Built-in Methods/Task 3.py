
# coding: utf-8

# In[ ]:

#below codes are all same as task 1 and task 2 for user's input and basic processing of texts till "............." line :

input_str = "" #define string for storing the input.
input_list = "" #define list for storing the input by sentences.
output_str = "" #define string for the output.
delimiter_tuple = (".","?","!") #define a tuple for delimiter.

input_str = input ("To input a number of lines of text:" + "\n")# Prompt the user for the input.

while input_str.count(".") + input_str.count("?") + input_str.count("!") < 5:#while loop to count the total delimiters.                                                                         
    input_str += " " + input ("There is no 5 sentences, please type more lines:" + "\n")
    #prompt the user for another input when total delimiters is less than 5.
    #user's input concatenate with the previous input.
    #while loop end if total delimiters is not less than 5.
    
for character in delimiter_tuple:#replace whitespace after each delimiter (".","?","!")  by a "#".  
     if character in input_str:
        input_str= input_str.replace ( character + " ", character + "#" )
        
input_list = input_str.split ("#")# split "#" from input string to input list. 
                                  # each item in the list is a sentence from uesr's input.    

output_str2 = "" #Define string for the output sentences line by line.

output_str2 = (input_list [0]+"\n"+ input_list [1]+"\n"+ input_list [2]+"\n"+ input_list [3]+"\n"+ input_list [4])
#pick up the first 5 items in the and concatenate them with "\n" between into output_str2.
#the first 5 items are the first 5 sentences of user's input.
#the string has these 5 sentences line by line as the character "\n" seperated each sentences as a newline.

character_list = []#define a list for storing each character from the 5 sentences.
punctuation_tuple = (",","!","?",".",";",":")#define a tuple for punctuation mark.
token_str = "" #define a string for storing all tokens and whitespace.
token_list = ""#define a string for storing tokens only.

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
#......................................................................................................................

#1)number of words:    
word_list = []#define a list for storing words in items.
punctuation_tuple = (",","!","?",".",";",":")#define a tuple for punctuation mark.

for token in token_list: #for token in token _list.
    if token not in punctuation_tuple:#if it is a punctuation mark which defined in punctuation_tuple
        word_list.append(token)       #append it to the defined word list.
        
print ("The total number of words are:", len (word_list)) #diplay the number of words fron the length of word list. 


#2)number of letters:
letters_number = 0 #define a integer for the number of letters.
for character in output_str2:#for character in output_str2
    if character.isalpha(): # if character is a letter. add 1 value to the letter_number.
        letters_number += 1
    else:                   # if character is not letter. add 0 value to the letter_number.
        letters_number += 0 
        
print ("The total number of letters are:", letters_number) #the value of letter_number is the total number of letters.
                                                           #diplay the letters_number value for total number of letters.


#3)number of unique words:
lowercase_list = []#define a list for storing words in lowercase.
unique_word_list = []#define a list for storing unique words.

for word in word_list: #change all words to lowercase format from word_list and return them to lowercase_list.
    lowercase_list.append(word.lower())
    
unique_word_list = set(lowercase_list) #use set() to get all unique words from lowercase_list to unique_word_list.

print ("The total number of unique words:",len(unique_word_list))#display length of unique_word_list for the total number of unique words.


#4)number of words that begin with an uppercase letter:
uppercase_count = 0 #define a integer numbers of words that begin with an uppercase letter.
for word in word_list: #for word in word_list
    if word[0].isupper():# if the first character of the word is an uppercase, add 1 value to uppercase_count.
        uppercase_count += 1
    else:               # if the first character of the word is an uppercase, add 0 value to uppercase_count.
        uppercase_count += 0   
        
print("The total number of words that begin with an uppercase letter:",uppercase_count)
#the value of uppercase_count is the total number of words that begin with an uppercase letter.
#display total number of words that begin with an uppercase letter.


#5)the total number of different punctuation marks:
punctuation_tuple = (",","!","?",".",";",":")#define a tuple for punctuation mark.
punctuation_count= {} #define a dictionary for storing the punctuation mark and its occurrence in the 5 sentences.

for token in token_list: #for token in token _list
    if token in punctuation_tuple: #if it is a punctuation mark
        if token not in punctuation_count:#append it as a key if and give a value 1 to the punctuation_count dictionary
            punctuation_count[token] = 1  #if it is not there
        else:
            punctuation_count[token] += 1 #otherwise, add 1 value to key's value in the dictionary.
                                          
print("The total number of different punctuation marks are as follow:")
for token in punctuation_count:
    print ("Punctuation mark", token, "has count equal to" , punctuation_count[token]) 
#punctuation_count dictionary now contains all punctuation marks founds with its occurrence in user's 5 input sentences. 
#display the punctuation marks and its number on the screen.


#6)the total number of words that are numbers:
number_count= 0 #define a integer for numbers of words are numbers.
for word in word_list: #for word in word_list
    if word.isdigit(): # if word is all digit, add 1 value to the number_count.
        number_count += 1
    else:              # if word is not all digit, add 0 value to the number_count.    
        number_count += 0     
        
print("The total number of words that are numbers:",number_count)#the value of number_count is the total number of words that are numbers.
                                                                 #display total number of words that are numbers.


# In[ ]:



