# import the ElementTree, Regex, and CSV modules. I imported pprint to more easily view the result_list in Terminal
import xml.etree.ElementTree as etree
import re
import csv
import pprint

# parse through the xml document -- 

# the file name for the xml document you want to parse goes inside of the parentheses
ElementTree = etree.parse('RRFA.01.TEST_ead.xml')
# look for the root element,which should be EAD
root = ElementTree.getroot()

# and then loop through the elements to identify children of the root.
# print(root)
# for a in root:
# 	print(a)
# 	print('--------------------')
# 	for b in a:
# 		print(b)
# 		print('--------------------')
# 		for c in b:
# 			print(c)
# 			print('--------------------')
# 			for d in c:
# 				print(d)
# 				print('--------------------')

# this is preparing the results of the .findall expression to be returned in a list
result_list = []
# here we are naming the csv columns and choosing the name for the csv file
csv_columns = ['container', 'unittitle']
csv_file = 'rrfa01_container-title_data.csv'

# we are going to build a python dictionary using the results of the .findall regular expression
for did_headings in root.findall(".//{urn:isbn:1-931666-22-9}did"):
	dictionary = {
	"container" : ""
	}
# here we are locating all of the text data for the <container> fields which are nested under the <did> fields
	for containers in did_headings.findall(".//{urn:isbn:1-931666-22-9}container"):
		dictionary['container'] = dictionary['container'] + containers.text
	for unittitles in did_headings.findall(".//{urn:isbn:1-931666-22-9}unittitle"):
		dictionary['unittitle'] = unittitles.text
	# and appending the results into the dictionary as outlined above
	result_list.append(dictionary)
	# you should see a python dictionary when you run this script in the Terminal
	print(result_list)

# here the code for writing the python dictionary to a csv file
with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in result_list:
    	writer.writerow(data)
