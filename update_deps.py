#!/usr/bin/env python
# encoding: utf-8
"""
update_deps.py

Created by Greg on 2013-02-20.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import json

def main():
    deps=open('deps.json')
    data=json.loads(deps)
    for dep in data:
        url=dep['url']
        path=dep['path']
        if len(path)>0 and len(url)>0 :
            if (not os.path.exists(path)):
                print 'adding dependency:' + path + ', ' + url
                os.system('git submodule add  '+url + ' '+path)
            else:
                print 'dependency present:' + path
    

if __name__ == '__main__':
    main()

