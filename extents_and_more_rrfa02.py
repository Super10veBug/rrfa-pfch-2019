import xml.etree.ElementTree as etree
import re

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

for did_headings in root.findall(".//{urn:isbn:1-931666-22-9}did"):
	# for extent in did_headings.findall(".//{urn:isbn:1-931666-22-9}extent"):
	# 	print(extent.text)
		extent = did_headings.find(".//{urn:isbn:1-931666-22-9}extent")
		
		# make an if statement -- if no .text then print "-"
	# for container in did_headings.findall(".//{urn:isbn:1-931666-22-9}container"):
	# 	print(container.text)
	# for unittitle in did_headings.findall(".//{urn:isbn:1-931666-22-9}unittitle"):
	# 	print(unittitle.text)
	# for physfacet in did_headings.findall(".//{urn:isbn:1-931666-22-9}physfacet"):
	# 	print(physfacet.text)
	# for pysc_desc_tags in did_headings.findall(".//{urn:isbn:1-931666-22-9}physdesc}"):
	# 	print(pysc_desc_tags.text)
	# 	for x in pysc_desc_tags.findall(".//{urn:isbn:1-931666-22-9}c}"):
	# 		print(x.text)
	# THIS IS NOT DOING ANYTHING ANYMORE- HOW TO GET CONTAINER LIST