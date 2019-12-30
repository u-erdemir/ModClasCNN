# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 16:19:58 2019

@author: Ubeydullah Erdemir
"""
import pickle
import numpy as np
import csv
import time

# Filtering criterias
snr_val = np.arange(0,20,2)
labels = ['BPSK','QPSK']
sample_count = 1000
frame_length = 128
test_data_ratio = 0.2

# Load the file
print("Loading the file...")
file_pickle = open('RML2016.10a_dict.pkl','rb')
raw_data = pickle.load(file_pickle, encoding='latin1')

# Files to be written
write_train_data = open('./Filtered/Train/train_data.csv','w', newline='')
write_train_labels = open('./Filtered/Train/train_labels.csv','w', newline='')
write_train_snr = open('./Filtered/Train/train_snr.csv','w', newline='')
write_test_data = open('./Filtered/Test/test_data.csv','w', newline='')
write_test_labels = open('./Filtered/Test/test_labels.csv','w', newline='')
write_test_snr = open('./Filtered/Test/test_snr.csv','w', newline='')

train_data = csv.writer(write_train_data)
train_labels = csv.writer(write_train_labels)
train_snr = csv.writer(write_train_snr)
test_data = csv.writer(write_test_data)
test_labels = csv.writer(write_test_labels)
test_snr = csv.writer(write_test_snr)

for l in labels:
        for i in snr_val:
                print("Label:",l,"SNR:",i)
                time.sleep(0.1)
                tmp = raw_data[(l,i)]
                np.random.shuffle(tmp) #Make the data random sequenced
                arr = np.ndarray([sample_count,frame_length])
                comp_array = np.complex_(arr)
                
                counter = 0
                for k in range(sample_count):
                    print(counter)
                    # Data separation
                    if counter<(sample_count*test_data_ratio):
                        print("test")
                        test_data.writerow(np.complex_(tmp[k,0] + 1j*tmp[k,1]))
                        test_labels.writerow([l])
                        test_snr.writerow([i])
                    else:
                        train_data.writerow(np.complex_(tmp[k,0] + 1j*tmp[k,1]))
                        train_labels.writerow([l])
                        train_snr.writerow([i])
                    counter += 1


