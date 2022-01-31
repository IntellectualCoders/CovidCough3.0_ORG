# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 11:42:45 2021

@author: Deepa Kapoor
"""
from pydub import AudioSegment
from pathlib import Path
entries = Path('C:/Users/Deepa Kapoor/Data Science/virufy-data-main/clinical/segmented/pos/')
for entry in entries.iterdir():

    print(entry.name)
    a = entry.name.split('.')
    print(a[0] + '.wav')
    src = 'C:/Users/Deepa Kapoor/Data Science/virufy-data-main/clinical/segmented/pos/' + entry.name
    dst = 'C:/Users/Deepa Kapoor/Data Science/virufy-data-main/clinical/segmented/cpos/' + a[0] + '.wav'
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")
    
#entries = Path('C:/Users/Deepa Kapoor/Data Science/virufy-data-main/clinical/segmented/neg/')
#for entry in entries.iterdir():
#    print(entry.name)
#    a= entry.name.split('.')
#    print(a[0] + '.wav')