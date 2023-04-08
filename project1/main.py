import nltk
import glob
import spacy
import re
import os
#import phonenumbers

#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
#nltk.download('wordnet')
from nltk.tag import StanfordNERTagger
from nltk import word_tokenize,sent_tokenize,pos_tag
from nltk import ne_chunk
from nltk.corpus import stopwords
from nltk.corpus import wordnet

stats_list = []
def read_input_files(files):
    all_data = []
    all_files = nltk.flatten(files)
    for files in all_files:
        file1 = glob.glob(files)
        print(file1)
        for each_file in file1:
            data  = open(each_file,"r").read()
            all_data.append(data)
           # print(data)
    return all_data


def redact_names(text):
    for names in text:
        words = word_tokenize(names)
        #print(words)
        pos_tags = nltk.pos_tag(words)
        ners = nltk.ne_chunk(pos_tags,binary=False)
        #print(pos_tags)
    redacted_words = []
    for i in range(len(words)):
        word, pos = pos_tags[i] 
        if  pos == 'NNP' and word[0].isupper() and  pos != 'VB':
            redacted_words.append('\u2588'*len(word))
        else:
            redacted_words.append(word)
    redacted_text = ' '.join(redacted_words)
   # print(redacted_text)
    string = 'redact_names'
    get_stats(string,len(redacted_text))
    return redacted_text
     #   words = word_tokenize(sentence)
      #  pos_tags = nltk.pos_tag(words)
       # redacted_words = []
        #for word, pos in pos_tags:
         #   if pos == 'NNP':
          #      redacted_words.append('\u2588' * len(word))
           # else:
            #    redacted_words.append(word)
       # redacted_sentences.append(' '.join(redacted_words))
    #redacted_text = ' '.join(redacted_sentences)
    #return redacted_text

def redact_dates(text):
    # Regex pattern to match dates in different formats
    date_patterns = [
        r'\d{1,2}\/\d{1,2}\/\d{2,4}', # mm/dd/yy or mm/dd/yyyy
        r'\d{1,2}\-\d{1,2}\-\d{2,4}', # mm-dd-yy or mm-dd-yyyy
        r'\d{1,2}\.\d{1,2}\.\d{2,4}', # mm.dd.yy or mm.dd.yyyy
        r'\d{1,2}\s+\w+\s+\d{2,4}', # dd Month yy or dd Month yyyy
        r'\w+\s+\d{1,2},\s+\d{2,4}', # Month dd, yyyy or Month d, yyyy
        r'\d{4}\/\d{1,2}\/\d{1,2}', # yyyy/mm/dd
        r'\d{4}\-\d{1,2}\-\d{1,2}', # yyyy-mm-dd
        r'\d{4}\.\d{1,2}\.\d{1,2}', # yyyy.mm.dd
        r'\d{8}', # yyyymmdd
        r'\d{1,2}\s+\w+\s+\d{4}', # dd Month yyyy
        r'\w+\s+\d{1,2}\s+\d{4}',
       r' \b\d{1,2}(st|nd|rd|th)\b',
       r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(st|nd|rd|th)?,\s+\d{4}|\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(st|nd|rd|th)?,\s+\d{2}([02468][048]|[13579][26])'# Month dd yyyy
    ]
    # Compile the regex patterns
    date_regex = re.compile('|'.join(date_patterns))
    
    # Replace the dates in the text with a redacted string
    redacted_text = date_regex.sub('\u2588' * 10, text)
    string = 'redact_dates'
    get_stats(string,len(redacted_text))
  #  print(redacted_text)
    return redacted_text




def redact_phone_numbers(text):
    phone_pattern1 = r'\(?[0-9]{3}\)?[-.\s]?[0-9]{3}[-.\s]?[0-9]{4}'
    phone_pattern2 = r'\d{1}-\d{3}-\d{3}-\d{4}'
    phone_pattern3 = r'\(\s*\d{3}\s*\)\s*\d{3}-\d{4}'
    phone_pattern4 = r'\+1\s*\(\s*\d{3}\s*\)\s*\d{3}[-.\s]*\d{4}'
    # Regex pattern to match phone numbers in different formats
    phone_regex = re.compile(phone_pattern1 + '|' + phone_pattern2 + '|' + phone_pattern3 + '|' + phone_pattern4)

    # Replace the phone numbers in the text with a redacted string
    redacted_text = phone_regex.sub('\u2588' * 10, text)
    string = 'redact_phone_numbers'
    get_stats(string,len(redacted_text))
    #print(redacted_text)
    return redacted_text


def redact_genders(text):
     genders=['him','her','hers','male',
              'man','woman','women','men','she', 'he' , 'his',
              'female', 'himself', 'herself','wife','husband']
     pattern = r"\b(" + "|".join(genders) + r")\b"
     redacted_text = re.sub(pattern, "\u2588" * len("\\1"), text, flags=re.IGNORECASE)
     string = 'redact_genders'
     get_stats(string,len(redacted_text))
     #redacted_text = text
   #  words = text.split()
    # for i, word in enumerate(words):
     #    lowercase_word = word.lower()
      #   if lowercase_word in genders:
       #                  if (i == 0 or not words[i-1].endswith('.')) and (i == len(words)-1 or not words[i+1].startswith('.')):
        #                     redacted_text = redacted_text.replace(word, '\u2588' * len(word))
         #elif word.title() in genders:
          #               if (i == 0 or not words[i-1].endswith('.')) and (i == len(words)-1 or not words[i+1].startswith('.')):
           #                  redacted_text = redacted_text.replace(word, '\u2588' * len(word))
    # print(redacted_text)
     return redacted_text

def redact_address(text):
    # Regular expression to match addresses
    address_pattern0 = r'\d+'
    address_pattern1 = r'([0-9]{3,4}\s.+,\s.+,\s[A-Z]{2}(?:\s[0-9]{5}|\s))'
    address_pattern = re.compile(address_pattern0 + "|" + address_pattern1)
    
    # Replace matches with asterisks
    redacted_address = address_pattern.sub('\u2588', text)
    string = 'redact_address'
    get_stats(string,len(redacted_address))
   # print(redacted_address)
   # print(redacted_address)
    return redacted_address

def get_stats(redacted_type = None , count = 0):
    temp = "The wordcount of " + redacted_type + ":" + str(count)
    stats_list.append(temp)
    return stats_list

def write_stats(stats_list = stats_list):
    path = ('./stderr/stderr.txt')
    file = open(path,"w",encoding = "utf-8")
    for i in range(len(stats_list)):
        file.write(stats_list[i])
        file.write("\n")
    file.close()
    return stats_list


        


def get_output_files(input_files,input_data,output_path):
    file_names = []
    file_data = []
    files = nltk.flatten(input_files)
    #print(files)
    for i in range(len(files)):
            input_files = glob.glob(files[i])
           # print(input_files)

            for j in range(len(input_files)):
                if '.txt' in input_files[j]:
                    input_files[j] = input_files[j].replace(".txt",".redacted")

                file_names.append(input_files[j])
              #  print(file_names)
                
            for i in range(len(file_names)):
                for j in range(len(input_data)):
                        file_data = input_data
                        #print(file_data)
                        path1 = (os.getcwd())
               #         print(path1)
                        path2 = (output_path+'/'+file_names[i])
                #        print(path2)
                 #       print(output_path)
                        folder_path = os.path.join(path1,output_path)
                        final_path = os.path.join(path1,path2)
                  #      print(folder_path)
                        if os.path.isdir(folder_path):
                            final_file = open(final_path, "w", encoding = "utf-8")
                        else:
                            os.mkdir(folder_path)
                            final_file = open(final_path, "w" , encoding = "utf-8")
                        final_file.write(file_data)
                        final_file.close()
            return len(file_names)



      






