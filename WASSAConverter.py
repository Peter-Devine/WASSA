import argparse
import os
import pandas as pd
import numpy as np

# Takes input and output directories as arguments
parser=argparse.ArgumentParser()
parser.add_argument('--input', default=".", help='The file path of the unzipped Facebook VA dataset')
parser.add_argument('--output', default="./data", help='The file path of the output dataset')

args = parser.parse_args()
INPUT_PATH = args.input
OUTPUT_PATH = args.output

# Make the output directory if it does not currently exist
if not os.path.exists(OUTPUT_PATH):
    os.mkdir(OUTPUT_PATH)

emotions = ['anger', 'fear', 'joy', 'sadness']
dataframe_types = ['train', 'dev', 'test']

for dataframe_type in dataframe_types:
    if dataframe_type == "train":
        file_suffix = dataframe_type
    else:
        file_suffix = dataframe_type + ".gold"
    
    anger = pd.read_csv(INPUT_PATH + "/anger-ratings-0to1." + file_suffix + ".txt", sep='\t', encoding="utf-8", names=["id", "text", "emotion", "intensity"])
    fear = pd.read_csv(INPUT_PATH + "/fear-ratings-0to1." + file_suffix + ".txt", sep='\t', encoding="utf-8", names=["id", "text", "emotion", "intensity"])
    joy = pd.read_csv(INPUT_PATH + "/joy-ratings-0to1." + file_suffix + ".txt", sep='\t', encoding="utf-8", names=["id", "text", "emotion", "intensity"])
    sadness = pd.read_csv(INPUT_PATH + "/sadness-ratings-0to1." + file_suffix + ".txt", sep='\t', encoding="utf-8", names=["id", "text", "emotion", "intensity"])
    
    wassa = anger.append(fear).append(joy).append(sadness).reset_index(drop=True)
    
    wassa.to_csv(OUTPUT_PATH+"/"+dataframe_type+".tsv", sep='\t', encoding="utf-8")