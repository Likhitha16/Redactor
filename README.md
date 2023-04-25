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

<b> Bugs and Assumptions </b>


When redacting text that contains sensitive information such as dates, phone numbers, and addresses, it is important to keep in mind some potential bugs and assumptions that may arise:

Regular Expressions (RegEx) Limitations: One common method of redaction is using regular expressions to identify and replace patterns in the text. However, regular expressions can have limitations and may not always capture every possible variation of the sensitive information. For example, a regular expression that matches a standard US phone number format may not capture international phone numbers or alternative phone number formats.

Contextual Ambiguity: Sometimes, the sensitive information may be ambiguous in its context, making it difficult to determine what to redact. For example, a string of numbers may represent either a phone number or a social security number. In such cases, it is important to consider the surrounding text and other contextual clues to make an informed decision about what to redact.

Data Loss: Redacting sensitive information can lead to unintentional data loss, where information that should not be redacted is inadvertently removed. For example, if an address contains a key identifier such as a building number, it may be important to retain this information for the intended recipient of the redacted text.

Inconsistencies: Sometimes, the sensitive information may be inconsistent in its format or structure, making it challenging to accurately redact. For example, a date may be written in different formats such as "04/25/2023" or "April 25, 2023". Similarly, addresses may be written in different formats depending on the location and cultural conventions.

False Sense of Security: Redacting sensitive information may give the impression that the text is now safe to share, when in fact the redaction may be reversible using advanced techniques such as forensic analysis. Therefore, it is important to consider the sensitivity of the information being shared and the potential risks of sharing redacted text.

To avoid these potential issues, it is recommended to use a combination of techniques such as automated redaction tools, manual verification, and expert review to ensure accurate and secure redaction of sensitive information.

https://github.com/Likhitha16/cs5293sp23-project1/blob/main/ezgif.com-video-to-gif.gif
