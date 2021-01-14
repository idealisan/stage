# sitemap generator
# run this at the root of the server

import os
import requests.utils

# no need of ending slash
site = "https://stage.gp.idealisan.com"

# preventing adding page resources
blocked_res=[".js",".css",".jpg","jpeg",".png",".svg"]
allowed_res=[".html",".htm",".php",".xhtml"]

def isAllowed(filename):
    for r in allowed_res:
        if filename.endswith(r):
            return True
    return False

server_root = os.path.curdir

sitemap=[]

steps = os.walk(server_root)
for pathes, dirs, files in steps:
    # print(dirs)
    for f in files:
        fp = pathes.replace('\\', '/') + '/' + f
        fp = site + fp[1:]
        if '/.' in fp or not isAllowed(f):
            # print("hidden")
            pass
        else:
            fp = requests.utils.requote_uri(fp)
            print(fp)
            sitemap.append(fp)

f=open("sitemap.txt","w",encoding="utf-8")
for url in sitemap:
    f.write(url)
    f.write("\r\n")
f.close()
