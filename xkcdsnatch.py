#! /usr/bin/python
import os, urllib, re
p = re.compile('http://imgs.xkcd.com/comics/.*?\"')
u = urllib.urlopen('http://dynamic.xkcd.com/comic/random/')
s = u.read()
u.close()
m = p.search(s)
if m:
    c = m.group()[:-1]
    os.system('feh %s &' % c)

