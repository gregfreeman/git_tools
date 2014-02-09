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
from jinja2 import Template
import codecs

def main():
    datafile=open('deps.json')
    data=json.load(datafile)
    subdeps=[]
    deps=data['needs']
    for dep in deps:
        url=dep['url']
        path=dep['path']
        if len(path)>0 and len(url)>0 :
            if (not os.path.exists(path)):
                if dep.has_key('branch'):
                    branch=dep['branch']
                    print 'adding dependency:' + path + ', ' + url + ' ,branch:' + branch
                    os.system('git submodule add -b '+branch+' '+url+' '+path)
                else:
                    print 'adding dependency:' + path + ', ' + url
                    os.system('git submodule add  '+url + ' '+path)
            else:
                print 'dependency present:' + path
            subdeps.extend(find_sub(path))
    extradeps=[]
    for dep in subdeps:
        url=dep['url']
        path=dep['path']
        if len(path)>0 and len(url)>0 :
            print path,url

    if data.has_key('matlab'):
        matlab_data=data['matlab']
        matlab_setup(matlab_data,deps)


def find_sub(folder):
    file=os.path.join(folder,'deps.json')
    subdeps=[]
    if os.path.isfile(file):
        deps=open(file)
        data=json.load(deps)
        subdeps=data['needs']
    return subdeps
    

def matlab_setup(matlab_data,deps):    
    print matlab_data
    if not matlab_data.has_key('m_setup'):
        return
    if matlab_data['m_setup']=='no':
        return
    
    path=os.path.split(os.getcwd())
    name=path[-1]

    folders=[d['path'] for d in deps]
    if matlab_data.has_key('folders'):
        folders.extend(matlab_data['folders'])

    cmds=[]
    if matlab_data.has_key('commands'):
        cmds=matlab_data['commands']
    print cmds

    outfile='setup_%s.m'%name
    print 'creating:', outfile
    print folders
    template = Template(template_txt)    
    html=template.render(name=name,folders=folders,cmds=cmds)
    f=codecs.open(outfile,'w','utf-8')
    f.write(html)
    f.close()
    
    
    
template_txt='''% function setup_{{ name }}

fullpath = mfilename('fullpath');
idx      = find(fullpath == filesep);
proj_folder = fullpath(1:(idx(end)-1));

addpath(proj_folder )
{% for folder in folders %}addpath(fullfile(proj_folder,'{{folder}}'))
{% endfor %}

{% for cmd in cmds %}{{cmd}}
{% endfor %}

'''


if __name__ == '__main__':
    main()

