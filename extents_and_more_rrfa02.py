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
csv_columns = ['extent', 'container', 'unittitle', 'physfacet']
csv_file = 'rrfa02_data.csv'

for did_headings in root.findall(".//{urn:isbn:1-931666-22-9}did"):
	dictionary = {
	"extent" : "",
	"container" : "",
	"unittitle" : "",
	"physfacet" : ""
	}
	for extent in did_headings.findall(".//{urn:isbn:1-931666-22-9}extent"):
		dictionary['extent'] = dictionary['extent'] + extent.text	
	for container in did_headings.findall(".//{urn:isbn:1-931666-22-9}container"):
		dictionary['container'] = dictionary['container'] + container.text
	for unittitle in did_headings.findall(".//{urn:isbn:1-931666-22-9}unittitle"):
		dictionary['unittitle'] = dictionary['unittitle'] + unittitle.text
	for physfacet in did_headings.findall(".//{urn:isbn:1-931666-22-9}physfacet"):
		dictionary['physfacet'] = dictionary['physfacet'] + physfacet.text
	result_list.append(dictionary)
	print(result_list)

with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in result_list:
    	writer.writerow(data)




# DELETED STUFF SECTION

#extent = did_headings.find(".//{urn:isbn:1-931666-22-9}extent")
# make an if statement -- if no .text then print "-"

	# 	for x in pysc_desc_tags.findall(".//{urn:isbn:1-931666-22-9}c}"):
	# 		print(x.text)
	# THIS IS NOT DOING ANYTHING ANYMORE- HOW TO GET CONTAINER LIST