# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 12:20:24 2021

@author: Deepa Kapoor
"""
import os, csv
import pandas as pd
df = pd.DataFrame([], columns=['corona_test','cough_filename'])
for path, dirs, files in os.walk("C:/Users/Deepa Kapoor/Data Science/New Project/train_3000_examples/neg16kHz/"):
    for filename in files:
        print(filename)
        df.loc[len(df.index)]=['negative',filename]
for path, dirs, files in os.walk("C:/Users/Deepa Kapoor/Data Science/New Project/train_3000_examples/pos16kHz/"):
     for filename in files:
         print(filename)
         df.loc[len(df.index)]=['positive',filename]


df.to_csv("dataset_minor_3000.csv", encoding='utf-8', index=False)