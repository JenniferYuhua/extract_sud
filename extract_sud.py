#!/usr/bin/python3

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:15:32 2020

@author: Jennifer Zhang
"""


"""
notes for transcriber:
    get into a new session, using capital words SESSION. 
    for example: "AUDIO FILE CHANGE TO MIDDLE SESSION"
"""
import docx2txt
import re
import pandas as pd
import sys
 


def get_sud(transcript_docx, save_path):
    # read in word file
    data = docx2txt.process(transcript_docx)
    # specify extract pattern
    re_pattern  = r"SESSION|[1-9][0-9]?\.\s*\n{1,}\s*\n*|100\.\s*\n{1,}\s*\n*"
    res = re.findall(re_pattern, data) 
    
    sud_list = []
    session_list = []
    current_session = 1
    for i in res:
        if i != "SESSION":
    
            i = i.replace(".", "")
            i = i.replace(" ", "")
            i = i.replace("\n","")
            i = int(i)
            sud_list.append(i)
            session_list.append("SESSION" + str(current_session))        
        else:
            current_session += 1
            sud_list.append(i)
            session_list.append("SESSION" +str(current_session))
            
    sud_df = pd.DataFrame(columns = ["SUD", "SESSION"])
    sud_df["SUD"] = sud_list
    sud_df["SESSION"] = session_list
    sud_df = sud_df[sud_df.SUD != "SESSION"]
    
    sud_df.to_csv(save_path, index=False)
    return
## test file path
##transcript_docx = "Audio/transcript/(2d)_Imaginal_Exposure.docx"    
##save_path = "(2d)_Imaginal_Exposure.csv"


get_sud(sys.argv[1],sys.argv[2])
print("done, check file")

 

