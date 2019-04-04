import re
from json import load, dump
import os

def body_out(fname):
    with open(fname, encoding= 'utf-8') as f:
        text = f.read()
    return text

def src(start_path):
    for root, dirs, files in os.walk(start_path):
        names = files
    for name in names:
        if name.endswith('.xml'):
            text = body_out(name)
            name = name.strip(".xml")
            print(name)
            #print(text[:1000])



def main():
    src('.')






if __name__ == "__main__":
    main()