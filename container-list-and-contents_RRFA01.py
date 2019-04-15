import xml.etree.ElementTree as etree
import re
import csv
import pprint

ElementTree = etree.parse('RRFA.01.TEST_ead.xml')

root = ElementTree.getroot()

# rrfa01_data = open('rrfa01_data.csv', 'w')

# csvwriter = csv.writer(rrfa01_data)

result_list = []
csv_columns = ['container', 'unittitle']
csv_file = 'rrfa01_data.csv'

# NEXT STEP IS TURN DATA INTO LIST, THEN DICTIONARIES SO, [{'unittitles' : []}, {'containers' :[]}
for did_headings in root.findall(".//{urn:isbn:1-931666-22-9}did"):
	dictionary = {
	"container" : ""
	}
	for containers in did_headings.findall(".//{urn:isbn:1-931666-22-9}container"):
		# this will not overwrite repeated fields, but add them instead
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

# except IOError:
# 	print("I/O error") 



	# dictionary['container'] = did_headings.get('containers')
	# dictionary['unittitle'] = did_headings.get('unittitles')





		# result_list={unittitles.text, containers.text}
		# print(result_list)


# with open('rrfa01_data.csv', 'w') as f:
# 	w = csv.DictWriter(f, fieldnames=('containers', 'untititles')
# 	w.writerheader()
# 	w.writerows((containers.text),(untititles.text))

# print(root)

# for a in root:
# 	# print(a)
# 	# print('--------------------')
# 	for b in a:
# 		print(b)
# 		print('--------------------')
# 		for c in b:
# 			print(c)
# 			# print('--------------------')
# 			for d in c:
# 				print(d)
		# 		print('--------------------')



