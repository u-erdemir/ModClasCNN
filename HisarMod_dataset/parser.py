import csv
import numpy as np
import time

sample_count_train = 1000
sample_count_test = 500

# Reading the files
read_label_train = open('./Train/train_labels.csv', 'r')
read_snr_train = open('./Train/train_snr.csv', 'r')
read_file_train = open('./Train/train_data.csv', 'r')

read_label_test = open('./Test/test_labels.csv', 'r')
read_snr_test = open('./Test/test_snr.csv', 'r')
read_file_test = open('./Test/test_data.csv', 'r')

# Creating csv reader object from files
label = csv.reader(read_label_train)
snr = csv.reader(read_snr_train)
data = csv.reader(read_file_train)

label_test = csv.reader(read_label_test)
snr_test = csv.reader(read_snr_test)
data_test = csv.reader(read_file_test)

# From data file sequence number, create which 1000 sample will be taken.
split_label = [13, 15]  # Input label: 13 -> BPSK, 15-> QPSK
split_index = []

SNR_range_begin = 0  # SNR ranges
SNR_range_end = 18

for i in split_label:
    raw = (26 * np.arange(int((SNR_range_begin + 20) / 2), int((SNR_range_end + 22) / 2)) + i).tolist()
    for j in raw:
        split_index.append(j)
split_index.sort()

# ----------TRAINING----------
# SNR
print("SNR Separation")
time.sleep(1)
write_file0 = open('./filtered/Train/train_snr.csv', 'w')
write0 = csv.writer(write_file0)
counter0 = 0
for ind0, d0 in enumerate(snr):
    print(ind0)
    slice_begin = split_index[counter0]
    if slice_begin <= ind0/sample_count_train < slice_begin+1:
        write0.writerow(d0)
        print("saved")
    elif ind0/sample_count_train == slice_begin+1:
        if counter0 == len(split_index)-1:
            break
        counter0 += 1
# write_file0.close()

# Label
print("Label Separation")
time.sleep(1)
write_file1 = open('./filtered/Train/train_labels.csv', 'w')
write1 = csv.writer(write_file1)
counter1 = 0
for ind1, d1 in enumerate(label):
    print(ind1)
    slice_begin = split_index[counter1]
    if slice_begin <= ind1/sample_count_train < slice_begin+1:
        write1.writerow(d1)
        print("saved")
    elif ind1/sample_count_train == slice_begin+1:
        if counter1 == len(split_index)-1:
            break
        counter1 += 1
# write_file1.close()

# Data
print("Data Separation")
time.sleep(1)
write_file2 = open('./filtered/Train/train_data.csv', 'w')
write2 = csv.writer(write_file2)
counter2 = 0
for ind2, d2 in enumerate(data):
    print(ind2)
    slice_begin = split_index[counter2]
    if slice_begin <= ind2/sample_count_train < slice_begin+1:
        write2.writerow(d2)
        print("saved")
    elif ind2/sample_count_train == slice_begin+1:
        if counter2 == len(split_index)-1:
            break
        counter2 += 1
# write_file2.close()

# ----------TEST----------
# SNR
print("SNR Separation")
time.sleep(1)
write_file3 = open('./filtered/Test/test_snr.csv', 'w')
write3 = csv.writer(write_file3)
counter3 = 0
for ind3, d3 in enumerate(snr_test):
    print(ind3)
    slice_begin = split_index[counter3]
    if slice_begin <= ind3/sample_count_test < slice_begin+1:
        write3.writerow(d3)
        print("saved")
    elif ind3/sample_count_test == slice_begin+1:
        if counter3 == len(split_index)-1:
            break
        counter3 += 1
# write_file3.close()

# Label
print("Label Separation")
time.sleep(1)
write_file4 = open('./filtered/Test/test_labels.csv', 'w')
write4 = csv.writer(write_file4)
counter4 = 0
for ind4, d4 in enumerate(label_test):
    print(ind4)
    slice_begin = split_index[counter4]
    if slice_begin <= ind4/sample_count_test < slice_begin+1:
        write4.writerow(d4)
        print("saved")
    elif ind4/sample_count_test == slice_begin+1:
        if counter4 == len(split_index)-1:
            break
        counter4 += 1
# write_file4.close()

# Data
print("Data Separation")
time.sleep(1)
write_file5 = open('./filtered/Test/test_data.csv', 'w')
write5 = csv.writer(write_file5)
counter5 = 0
for ind5, d5 in enumerate(data_test):
    print(ind5)
    slice_begin = split_index[counter5]
    if slice_begin <= ind5/sample_count_test < slice_begin+1:
        write5.writerow(d5)
        print("saved")
    elif ind5/sample_count_test == slice_begin+1:
        if counter5 == len(split_index)-1:
            break
        counter5 += 1
# write_file5.close()
