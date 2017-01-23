# common function
#Author: Christine Lakits
import sys
import requests
import json
import csv
from lxml import html
from datetime import datetime
from time import mktime


def json2csv(data):


        key_list = []
        for section in data:
            for key in section:
                if key != "interfaces":
	                if key not in key_list:
	                    key_list.append(key)
        for key in key_list:
            print key + ",",
        print "\r"

        for section in data:
            for key in key_list:
                if key in section:
	                print str(section[key]) + ",",
                else:
                    print ",",
            print "\r"
def csv2json_file(csv_file,json_file):
    result = []
    with open(csv_file,'rU') as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        for row in reader:
            result.extend([{title[i]:row[title[i]] for i in range(len(title))}])

    with open(json_file, "w") as f:
        f.write(json.dumps(result, indent=4, sort_keys=True))

def json2csv_file(json_file,csv_file,header_row):
    csvfile = csv.writer(open(csv_file, "wb+"))

    with open(json_file, "r") as json_data:
        data = json.load(json_data)

    csvfile.writerow(header_row)
    for d in data:
        row = []
        for h in header_row:
            row.append(d[h])
        csvfile.writerow(row)


def search4match(orig_dict, search_dict):
    search_result = []
    search_key=search_dict.keys()[0]
    search_value=search_dict.values()[0]
    for d in orig_dict:
        if d[search_key] == search_value:
            #print "found"
            #for i in d:
                #print i, d[i]
            search_result.append(d)
        #else:
            #print "NOT found"
    return search_result

