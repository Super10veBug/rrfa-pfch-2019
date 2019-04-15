import xml.etree.ElementTree as etree
import re

ElementTree = etree.parse('RRFA.02.TEST_ead.xml')

root = ElementTree.getroot()

print(root)

for a in root:
	print(a)
	for b in a:
		print(b)
		for c in b:
			print(c)
			for d in c:
				print(d)

# for did_headings in root.findall(".//{urn:isbn:1-931666-22-9}did"):
# 	for extent in did_headings.findall(".//{urn:isbn:1-931666-22-9}extent"):
# 		print(extent.text)
# 	for container in did_headings.findall(".//")