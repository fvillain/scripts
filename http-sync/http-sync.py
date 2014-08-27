#!/usr/bin/env python

import yaml
from subprocess import call
from os import makedirs,isdir

stream = open('mapping.yml','r')
mapping = yaml.load(stream);

for dns in mapping.keys():
    print ("=== "+ dns +" ===")
    epo = mapping[dns];

    for component in epo.keys():
       link = epo[component]['link']
       name = epo[component]['name']

       if name == None or link == None :
          break

       directory = dns + '/' + component 
       filename = directory + '/' + name
  
       if not isdir( directory ) :
          print("+ create directory : "+directory)
          makedirs(directory)

       print ("+ download "+ component)
       print ("   - from : "+ link )
       print ("   - to   : "+ filename )
       dlstatus = call("wget -q -O "+filename+" "+link, shell=True)

       if dlstatus == 0 :
          print ("   OK !")
       else:
          print >>sys.stderr, "    FAILURE ", dlstatus

