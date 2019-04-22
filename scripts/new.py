from sys import argv
from slugify import slugify
import os

title      = "New Post"
categories = ""
tags       = ""

if len(argv) >= 2:
    title = argv[1]
if len(argv) >= 3:
    categories = argv[2]
if len(argv) >= 4:
    tags = argv[3]

filename = '_drafts/' + slugify(title) + '.md'
if not os.path.isfile(filename):
    f = open(filename, 'w', encoding='UTF-8')
    f.write('---\nlayout: post\ntitle: "' + title + '"\ncategories: ' + categories + '\ntags: ' + tags + '\n---\n\n')
    f.close()
    print('Created a new post: ' + filename)