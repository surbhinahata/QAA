#!/usr/bin/env python

import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Python script for map and unmapped alignment")
    parser.add_argument("-f", "--filename", help="Specify the input filename.", type = str)
    return parser.parse_args()
args = get_args()

filehandle=args.filename

with open(filehandle, "r") as fh:
    mappedRead:int = 0
    unmappedRead:int = 0
    flaglist:list = []
    sec_alignment = 0

    for line in fh:
        if line.startswith("@"):
            pass
        else:
            #focus on second column
            flagList = line.split('\t')[1]
            #print(flagList)
            flag = int(flagList)
            #print(flag)
            if((flag & 256) == 256):
                pass
                #sec_alignment+=1
            elif ((flag & 4) != 4):
                mappedRead+=1
            else:
                unmappedRead+=1
    print(f'Mapped reads: {mappedRead}')
    print(f'Unmapped reads: {unmappedRead}')