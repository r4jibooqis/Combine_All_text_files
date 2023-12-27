# by Raji Booqis
import os

##########  function for renaming files  ##########
def RenameFiles(folder_path):
    # number of file
    num = 0     
    # loop that take each file and change it's name
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            new_name = "File_" + str(num) +".txt"
            num += 1
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))


########## funciton for combining all textfiles in one text file to be corpus ##########
def createCorpus(folder_path,output_file):
    count = 1   #count the number of words
    string = ""     #store words

    # Open output file
    output_text = open(output_file,'w',encoding='utf-8')

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(folder_path+"\\"+filename, 'r', encoding='utf-8') as file:

                # create line as string and write it in output_text
                for line in file:

                    # change the number ==> number of words in one line
                    if (count%7 == 0):
                        string = string + "\n"
                        output_text.write(string)
                        string = ""

                    string = string + line.strip() +" "
                    count = count + 1
    # close output file
    output_text.close()

#######################################################################################################
    
#### 1) set the folder path that contain all text files && the output text file path (Corpus)
folder = r"C:\\folder\\path\\"  #EDIT HERE
output_file = r"C:\\file\\path\\Corpus.txt" #EDIT HERE

#### 2) run the code
RenameFiles(folder)
createCorpus(folder,output_file)
