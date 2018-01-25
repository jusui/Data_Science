#coding:utf-8

import re

s = '<html><head><title>Title</title>'
ss = '<aaa>|公式国名 = {{lang|en|United Kingdom of Great Britain and Northern Ireland}}<ref>'

match = re.match('<.*?>', ss).group(0)
print(match)
