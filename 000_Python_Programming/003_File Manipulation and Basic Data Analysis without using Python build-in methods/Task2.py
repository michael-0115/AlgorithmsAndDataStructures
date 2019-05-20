
# coding: utf-8

# In[22]:

def statistics(file):

    try: 
        read_file = open(file, "r")       #Open file for read 
        
    except FileNotFoundError as error:   #Raise and error when file not found
        print (error)                 
        
    else:                               #If file opend successfully, continue to the function process
        content_string = read_file.read() # Read file's content to a string
        content_string = content_string.replace("\n", "") #Remove all "\n" in the string by using replace method  
                                                          #as string is immutable
        word_list = content_string.split(" ")  #Delete the last null item in the list, this null in the last item                                 
        word_list.pop()                       #is created when using split " " to split the a string  

        check_item_dict = {0:"!",1:"?",2:".",3:"[/]",4:"[//]",5:"[*]",6:"(.)",7:"(..)",8:"(...)",9:",",10:";",11:":"} 
                                                          #define a dictionary list out items need to be counted
        not_word_list = ["[/]","[//]","[*]","(.)","(..)","(...)","!","?",".",",",";",":",]
                                                          #define a list for item not a word 


        #1. To count the occurrence of certain symbols in word_list for sybols listed in check_item_dict:
        count_list = []                                         #Define a empty list to store the number of occurrence                                                                        
        n = 0                                                 
        while n <= 8:                                               #To count the occurrence                                              
            count_list.append(word_list.count (check_item_dict[n])) #and store the number to the count_list.     
            n += 1

        #2. To count unique word:
        lowercase_list = []                 #Define list to store words all been lowercase for counting unique words.
        for word in word_list:              #For word not in the not_word_list, 
            if word not in not_word_list:    #lowercase it and add to the lowercase_list.
                lowercase_list.append(word.lower())
        unique_word_list = set(lowercase_list)        #Get unique words in lowercase_list

        #3. Do statistics:
        count_item_dic = {}                #Define a dictionary for store items with its number counted from word_list.
        count_item_dic["statement"] = sum(count_list[0:3])     #Number of statements which ends with "!" or "?" or "."
        count_item_dic["unique_words"] = len(unique_word_list) #Number of unique word
        count_item_dic["repititions"] = count_list[3]          #Number of "[/]" 
        count_item_dic["retracings"] = count_list[4]           #Number of "[//]" 
        count_item_dic["errors"] =  count_list[5]              #Number of "[*]" 
        count_item_dic["pauses"] = sum(count_list[6:9])        #Number of "(.)","(..)","(...)"

        read_file.close()                                     #Close read_file
        return count_item_dic                                 #Return data

    
#A. Statistic---------------------------------------------
import glob                #import glob function

#for Group SLI:
input_folder = glob.glob(r"SLI cleaned/*.txt")                                       
total_files = len(input_folder)        #Grab pathname for files in SLI cleaned folder to get number of files
SLI_stat_list = []                  #Define a list to store the result from statistic function 
n = 1 
while n <= total_files:          #There are 10 files, call statistic function for each file sequently        
    file = "SLI cleaned/"+"SLI-"+str(n)+"_cleaned.txt"
    result= statistics(file)      #to do run the statistic process.
    SLI_stat_list.append(result)  #And return data to the SLI_stat_list 
    n +=1

#for Group TD:
input_folder = glob.glob(r"TD cleaned/*.txt") 
total_files = len(input_folder)       #Grab pathname for files TD cleaned folder to get number of files
TD_stat_list = []                  #Define a list to store the result from statistic function 
n = 1
while n <= total_files:          #There are 10 files, call statistic function for each file sequently  
    file = "TD cleaned/"+"TD-"+str(n)+"_cleaned.txt"
    result= statistics(file)     #to do run the statistic process.
    TD_stat_list.append(result)  #And return data to the SLI_stat_list 
    n +=1

    
    
#B. Report----------------------------------------------
import pandas as pd           #import pandas

files = ["file-1","file-2","file-3","file-4","file-5","file-6","file-7","file-8","file-9","file-10"]
stats_type = ['statement','unique_words','repititions','retracings','errors','pauses']

#for Group SLI:
#Create a pandas data frame for the statistic result for 10 file in Group SLI
SLI_report= pd.DataFrame(SLI_stat_list, index = files, columns=stats_type, dtype ='float64')
SLI_report_ave = SLI_report.copy()

#Create a nother pandas data frame that including the mean value for SLI group 
SLI_report_ave.loc['average'] = SLI_report_ave.mean() 
print ("Following are the statistics for SLI")
print (SLI_report_ave.round(1))            #Out put as a report 

print () 

#for Group TD:
#Create a pandas data frame for the statistic result for 10 file in Group TD
TD_report= pd.DataFrame(TD_stat_list, index = files, columns=stats_type, dtype ='float64')
TD_report_ave = TD_report.copy()

#Create a nother pandas data frame that including the mean value for TD group 
TD_report_ave.loc['average'] = TD_report_ave.mean()
print ("Following are the statistics for TD")  
print (TD_report_ave.round(1))            #Out put as a report 
 


# In[23]:

#C. Plot chart (Group SLI)----------------------------------------------
import matplotlib.pyplot as plt           #import matplotlib

#Dataframe to barchart, using matplotlib subplot:
SLI_plot = SLI_report.plot(subplots=True, figsize=(15, 15), kind = "bar")  
plt.suptitle("Statistics barchart for SLI", size=30)
plt.savefig('Chart1_SLI.png')    #Save the chart as a file  
plt.show()                      #Plot the chart as output


# In[24]:

#C. Plot chart (Group TD)----------------------------------------------
#for Group TD: 
#Dataframe to barchart, using matplotlib subplot:
TD_plot = TD_report.plot(subplots=True, figsize=(15, 15), kind = "bar")
plt.suptitle("Statistics barchart for TD", size=30)
plt.savefig('Chart2_TD.png')    #Save the chart as a file  
plt.show()                      #Plot the chart as output


# In[25]:

#D. Groups comparaison (compare SLI with TD)----------------------------------------------

mean_SLI = SLI_report_ave[-1:]  #Take means values from both group SLI and TD to a new pandas dataframe
mean_TD  = TD_report_ave[-1:]   
groups_statistics = pd.concat([mean_SLI,mean_TD], axis=0)
groups_statistics.index = ["SLI","TD"]
                                #And Dataframe to barchart, using matplotlib subplot 
groups_statistics.plot(subplots=True, figsize=(6, 15), kind = "bar", width=0.1)
plt.suptitle("Statistic barchart"+"\n"+"means between"+"\n"+"Group SLI and Group TD", size=25)
plt.savefig('Chart3_SLT TD.png') #Save the chart as a file  
plt.show()                       #Plot the chart as output


# In[ ]:



