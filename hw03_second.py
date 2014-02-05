import csv

bio_file = "bios.csv"

# open 'bios.csv' document and read in data
infile = open(bio_file, "rb")
reader = csv.reader(infile)

# create bio_data list that keeps info on the following keys:
#   "signup_date", "age", "gender"
bio_data = []

row_num = 0

for row in reader:
    # skip header document in file
    if row_num == 0:
        row_num += 1
    else:
        bio = {}
        # bio has the following keys: {"signup_date", "age", "gender"}
        bio["signup_date"] = row[1]
        bio["age"] = row[3]
        bio["gender"] = row[4]
        bio_data.append(bio)    
    
print len(bio_data)