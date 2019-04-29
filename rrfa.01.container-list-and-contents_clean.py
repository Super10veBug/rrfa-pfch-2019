import xml.etree.ElementTree as etree
import re
import csv
import pprint

ElementTree = etree.parse('RRFA.01.TEST_ead.xml')

root = ElementTree.getroot()

result_list = []
csv_columns = ['container', 'unittitle']
csv_file = 'rrfa01_container-title_data.csv'

for did_headings in root.findall(".//{urn:isbn:1-931666-22-9}did"):
	dictionary = {
	"container" : ""
	}

	for containers in did_headings.findall(".//{urn:isbn:1-931666-22-9}container"):
		dictionary['container'] = dictionary['container'] + containers.text
	for unittitles in did_headings.findall(".//{urn:isbn:1-931666-22-9}unittitle"):
		dictionary['unittitle'] = unittitles.text
	result_list.append(dictionary)
	print(result_list)

with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in result_list:
    	writer.writerow(data)
