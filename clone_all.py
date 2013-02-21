#!/usr/bin/env python
# encoding: utf-8
"""
clone_all.py

Created by Greg on 2013-02-20.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import argparse, subprocess

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    usage='%(prog)s file',
    description='This program parses a file',
    add_help=False
    ) 
parser.add_argument('file')

def main():    
    args = parser.parse_args()
    repos = open(args.file, "r").readlines()
    for repo in repos:
        words=repo.strip().split('/')
        parts=words[-1].split('.')
        folder=parts[0];
        if len(folder)>0 :
            if (not os.path.exists(folder)):
                print 'cloning repo:' + folder
                os.system('git clone '+repo)
            else:
                print 'found repo:' + folder


if __name__ == '__main__':
    main()

