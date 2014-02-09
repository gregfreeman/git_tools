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
    description='This program clones all repositories specified in a file as mirrors',
    add_help=False
    ) 
parser.add_argument('file')

def main():    
    args = parser.parse_args()
    repos = open(args.file, "r").readlines()
    basedir=os.getcwd()
    for repo in repos:
        words=repo.strip().split('/')
        parts=words[-1].split('.')
        folder=words[-1];
        if len(folder)>0 :
            print folder
            if (not os.path.exists(os.path.join(basedir,folder))):
                print 'cloning repo:' + folder
                os.chdir(basedir)
                os.system('git clone --mirror '+repo)
            else:
                print 'found repo:' + folder
                os.chdir(os.path.join(basedir,folder))
                os.system('git remote update')
                os.chdir(basedir)

if __name__ == '__main__':
    main()

