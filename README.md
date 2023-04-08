Author : Chandra Likhitha Chopparapu


## The Redactor

This project has been implemented in python and can be run from command line with the below command.

pipenv run python redactor.py --input '*.txt' \
                    --names --dates --phones --genders --address\
                    --output 'files/' \
                    --stats stderr

Packages used in this Project :

• nltk
• spacy
• argparse
• spacy
• os
• glob
• phonenumbers
• logging
• en_core_web_sm

Redactor.py
The primary file where the project's execution begins is this one. All command-line input arguments are parsed in this file before the appropriate functions are called to continue processing the txt files. The parsed arguments are listed below.

--names, --gender, and --input Date, Concept, Product, Statistics

main.py 

I included many functions for each of the functionality in this file. (arguments in above step).

handle_input_files(files):

This technique pulls data from all of the.txt files in the working directory using the argument of the --input flag. The primary file receives this data back in return.

redact_names(text_data):

This method is called when –-names flag is passed in the command line.
This method takes input data returned from handle_input_files() and mask names in the data with Unicode character ██ .
For this purpose, spacy & nltk libraries have been used to identify entities ‘PERSON, ‘GPE’ and ORGANIZATION as all of them are considered names and in particular proper nouns.
This method couldn’t identify some of the surnames or last names and some non-english (not native) names because of spacy and nltk limitations.

redact_dates(input_data):

If the --dates flag is present, this procedure is invoked.
Dates are hidden in the text after input data is received.
Regex has also been utilized to mask the areas where month names are not recognized by the spacy library in order to identify the labels with the "DATE" tag.

redact_phones(input_data):

If the --phones flag is present, this procedure is invoked.
It accepts input data and outputs text with hidden phone numbers.
The phone numbers have been identified for this use using the phonenumbers library.
The phone numbers package that has been recommended for this project's github can be found there.
It was adopted since it was a pure Python project and it supported phone numbers from many countries.

redact_gender(input_data):

If the --genders flag is present, this procedure is invoked.
It accepts input data and outputs text with words associated with gender hidden.
To hide gender words, the spacy library uses pronoun tags and a few gender-related words as filter criteria.
It does not, however, hide all gender words because doing so would involve higher order processing .

write_stats():

This approach logs every redaction type and word count into a text file called stderr/stderr.txt. Every time the --stats flag is used in input, the path is hardcoded so that this method is executed and all the stats are sent to the sterr.txt file.


get_output():

The folder location supplied in the input for the flag --output is where the redacted data is written in this function.
The result is saved as.redacted files with the same name as the text file used as input.

Test Cases
test_redact_names.py
•This technique is used to test the functionality of redacting names. If at least one word is hidden, the statement is true.

test_redact_phno.py
•Using this technique, the functionality of redacting phone digits is tested. If at least 1 word (phno) is hidden, the statement is true.

test_redact_gender.py
•This technique is used to test the functionality of redacting gender. If at least 1 word (related to gender) is hidden, the statement is true.

test_redact_dates.py
•This technique is used to test the functionality of redacting dates. If at least one word is hidden—the date—it is said to be true.

The functionality of redact ideas is tested using the test_redact_concept.py method. If at least 1 word (concept-relevant word) is obscured, the statement is true.

Go to the tests folder and perform pipenv run python -m pytest to run test cases.
