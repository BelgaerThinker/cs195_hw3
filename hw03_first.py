import json

# Create message_file list and add in the following keys: "num_recipients",
#   "message_time", "message"
message_file = "messages.json.txt"

message_data = []

for line in open(message_file):
    message_full = json.loads(line)
    # message has following keys: {"sender", "recipients",  "num_recipients",
    #                               "message_time", "message"}
    message = {}
    message["num_recipients"] = message_full["num_recipients"]
    message["message_time"] = message_full["message_time"]
    message["message"] = message_full["message"]
    
    message_data.append(message)

from string import punctuation
set_punct = set(punctuation)
set_punct = set_punct - {"'"}

def sanitize(text, set_excludes):
    """Return a `sanitized` version of the string `text`. Characters
    in `set_excludes` are removed.
    
    Specifically, We:
    1. Replace any characters in set_excludes with spaces, 
    2. Convert uppercase letters to lowercase, 
    3. Remove one-letter words. 
    4. Remove words containing "http://"
    
    For example:
        "John's car" -> "john s car" -> "john car"
    assuming punctuation is to be excluded.
    """
    
    text = text.lower()
    
    # split into words to remove hyperlinks, then join back into string:
    text = " ".join([ w for w in text.split() if not ("http://" in w) ])
    
    # filter bad letters (this uses a python ternary statement):
    letters_noPunct = [ (" " if c in set_excludes else c) for c in text ]
    
    # Join letters into string, then split into words to 
    # remove one-letter words
    text = "".join(letters_noPunct)
    words = text.split()
    long_enuf_words = [w.strip() for w in words if len(w)>1]
    
    return " ".join(long_enuf_words) # spaces between words
    
for message in message_data:
    message["message"] = sanitize(message["message"], set_punct)
    
print message_data[1]["message"]    
        
                
#import csv
#bio_file = "bios.csv"
#
#infile = open(bio_file, "rb")
#reader = csv.reader(infile)
#
#for row in reader:
#    bio = row
#    break
#    
#print bio