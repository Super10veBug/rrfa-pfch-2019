import xml.etree.ElementTree as etree
import re
import csv

ElementTree = etree.parse('RRFA.02.TEST_ead.xml')

root = ElementTree.getroot()

# print(root)

# for a in root:
# 	print(a)
# 	for b in a:
# 		print(b)
# 		for c in b:
# 			print(c)
# 			for d in c:
# 				print(d)
# 				for e in d:
# 					print(e)

result_list = []
csv_columns = ['unittitle', 'container : box | object | Reg Number |', 'extent', 'physfacet', 'physloc']
csv_file = 'rrfa02_extents-and-more_data.csv'

for did_headings in root.findall(".//{urn:isbn:1-931666-22-9}did"):
	dictionary = {
	"unittitle" : "",
	"container : box | object | Reg Number |" : "",
	"extent" : "",
	"physfacet" : "",
	"physloc" : ""
	}

	for unittitle in did_headings.findall(".//{urn:isbn:1-931666-22-9}unittitle"):
		dictionary['unittitle'] = dictionary['unittitle'] + unittitle.text + ' | '
	for container in did_headings.findall(".//{urn:isbn:1-931666-22-9}container"):
		dictionary['container : box | object | Reg Number |'] = dictionary['container : box | object | Reg Number |'] + container.text + ' | '
	for extent in did_headings.findall(".//{urn:isbn:1-931666-22-9}extent"):
		dictionary['extent'] = dictionary['extent'] + extent.text + ' | '
	for physfacet in did_headings.findall(".//{urn:isbn:1-931666-22-9}physfacet"):
		dictionary['physfacet'] = dictionary['physfacet'] + physfacet.text + ' | '
	for physloc in did_headings.findall(".//{urn:isbn:1-931666-22-9}physloc"):
		dictionary['physloc'] = dictionary['physloc'] + physloc.text + ' | '
	result_list.append(dictionary)
	print(result_list)

with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in result_list:
    	writer.writerow(data)