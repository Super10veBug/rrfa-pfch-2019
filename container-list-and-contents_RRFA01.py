import xml.etree.ElementTree as etree
import re
import csv

ElementTree = etree.parse('RRFA.01.TEST_ead.xml')

root = ElementTree.getroot()

# rrfa01_data = open('rrfa01_data.csv', 'w')

# csvwriter = csv.writer(rrfa01_data)

result_list = []
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



