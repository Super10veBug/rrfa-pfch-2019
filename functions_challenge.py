import xml.etree.ElementTree as etree
import re
import csv

ElementTree = etree.parse('RRFA.01.TEST_ead.xml')

root = ElementTree.getroot()
xmldict = XmlDictConfig(root)

# rrfa01_data = open('rrfa01_data.csv', 'w')

# csvwriter = csv.writer(rrfa01_data)

# result_list = []
# NEXT STEP IS TURN DATA INTO LIST, THEN DICTIONARIES SO, [{'unittitles' : []}, {'containers' :[]}
for did_headings in root.findall(".//{urn:isbn:1-931666-22-9}did"):
	for containers in did_headings.findall(".//{urn:isbn:1-931666-22-9}container"):
		# print(append(containers.text)
		for unittitles in did_headings.findall(".//{urn:isbn:1-931666-22-9}unittitle"):
		# print(append(unittitles.text)

			# dictionary = {}
   			#dictionary['containers.text'] = item.get('containers')
   			#dictionary['unittitles.text'] = item.get('unittitles')
			# result_list.append(dictionary)
			# print(result_list)
# I AM GOING TO TRY TO USE "class dict" to turn this into a dictionary. 



# IDEA FOR LATER ----------------------------------------------------------------------------
# import xmltodict
# import csv

# xmldict = xmltodict.parse(yourxml)

# f = csv.writer(open('yourcsv.csv', "w"))

# #write field names to file keys of the dict, or you can specify the ones you outlined in your output eg.
# f.writerow(xmldict.keys())

# #write the contents
# for key in xmldict:
#     f.writerow(key['attrs'], key['attrs'] etc. etc.)