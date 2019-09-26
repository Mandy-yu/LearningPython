#!/usr/bin/python
import sys
import re
import fileinput
import json

my_file= sys.argv[1]
for each_line_of_text in fileinput.input(my_file):
    if re.match(r'.*\t.*\tgene\t', each_line_of_text):
       text_in_columns = re.split('\t',each_line_of_text)
       gene_name_matches = re.findall('gene_name \"(.*?)\";',each_line_of_text)
       if len(text_in_columns)>3:
          DIctionrary={}
          DIctionrary["geneName"]=gene_name_matches
          DIctionrary["chr"]=text_in_columns[0]
          DIctionrary["startPos"]=text_in_columns[3]
          DIctionrary["endPos"]=text_in_columns[4]
          print(json.dumps(DIctionrary))

