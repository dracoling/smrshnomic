"""
this is a python3 script. github limits how many times you can
use their api if you do not authenticate - 60 times per hour. keep
that in mind when you use this.
"""

import urllib.request as r
import json
import base64

def grab(url):
  f = r.urlopen(url)
  doc = f.read().decode()
  f.close()
  return doc

def js(url):
  d = grab(url)
  return json.loads(d)

_active = 'https://api.github.com/repos/dracoling/smrshnomic/contents/proposals/active'
_file = 'https://raw.github.com/dracoling/smrshnomic/master/proposals/active/%s'

try:
  stuff = js(_active)
  for t in stuff:
    name = t["name"]
    content = grab(_file % name)
    print(content)

except (r.HTTPError) as err:
  if err.code == 404:
    print("no active proposals")
  else:
    raise
