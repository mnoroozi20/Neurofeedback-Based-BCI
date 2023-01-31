import os
import datetime
import csv

today = datetime.datetime.now()

print(today)
date = today.strftime("%Y%m%d")

# parameters below, need to auto update or be changed manually if can't auto
sub_num = 1
stage = "Pre"
block_num = 7
file_name = "eeg_data.csv"


# Data/date/subj{num}/{stage(pre/neuro/post)}/block{num}/{actual file ie {stage}_b{num}.csv}
# other folder called "Neruofeedback" - contains code


path = f"C:/Neuro_data/{date}/Subject_{sub_num}/Stage_{stage}/Block_{block_num}"

isExist = os.path.exists(path)

if not isExist:
    try:
        os.makedirs(path)
    except OSError:
        print("Creation of directory %s failed" % path)
    else:
        print("Successfully created the directory %s" % path)

with open(os.path.join(path, file_name), 'w') as temp_file:
    print("Files added")
    writer = csv.writer(temp_file)
    for row in data:
        writer.writerow(data)

    print("EEG data saved in folder")


