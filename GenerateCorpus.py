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
    num_words = 10 #number of words in each line
    count = 1   #count the number of words
    string = ""     #store words

    # Open output file
    output_text = open(output_file,'w',encoding='utf-8')

    # get all text files
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(folder_path+"\\"+filename, 'r', encoding='utf-8') as file:

                # Process each line in the input file
                for line in file:
                    words = line.strip().split()
                    
                    # Create lines with the specified number of words
                    for word in words:
                        # change the number ==> number of words in one line
                        if (count%num_words == 0):
                            string = string + "\n"
                            output_text.write(string)
                            string = ""
                        # else add word to the string line
                        string = string + word +" "
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
