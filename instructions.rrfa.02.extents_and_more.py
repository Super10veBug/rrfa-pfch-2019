# import ElementTree to use "for loops" to search the XML document for desired headings
import xml.etree.ElementTree as etree
# import regular expressions to use "findall" to loop through headings and pull out the desired elements
import re
# import csv module in order to write a csv
import csv

# parse through the xml document -- 
# the file name for the xml document you want to parse goes inside of the parentheses
ElementTree = etree.parse('RRFA.02.TEST_ead.xml')

# get the root element
root = ElementTree.getroot()

# # print the root and run the code through terminal
# print(root)

# # your first heading will say ead, so you want to keep looping to find the names of the fields you are looking for

# for a in root:
# 	print(a)
# 	# keep looping through elements until you find your desired fields
# 	for b in a:
# 		print(b)
# 		for c in b:
# 			print(c)
			# at this point, the results are more robust and we see the fields we are looking for in the Terminal
# 			for d in c:
# 				print(d)
# 				for e in d:
# 					print(e)


# Now you are going to build a python dictionary, which has key:value pairs, where the key is the title we want
# the csv column to be called, and the value is what we are going to pull from the xml data.

# results are going to build a list
result_list = []
# this list contains the names of the csv colum. I've separated the information that we will get back for 
# container data with pipes.
csv_columns = ['unittitle', 'container : box | object | Reg Number |', 'extent', 'physfacet', 'physloc']
# this is what our new csv file will be called in the folder where our data and code have been saved
csv_file = 'rrfa02_extents-and-more_data.csv'

# You want to keys to be the column names, and the value to be an open, and we will define the results using findall
for did_headings in root.findall(".//{urn:isbn:1-931666-22-9}did"):
	dictionary = {
	"unittitle" : "",
	"container : box | object | Reg Number |" : "",
	"extent" : "",
	"physfacet" : "",
	"physloc" : ""
	}

# this is where we define the content of the values in the dictionary, which will fill the cells in our csv file
	# since we looped through the data earlier, we know that the value for the ead field "unittitle"
	# is nested under a did heading, so will use a "for" statement to find all unittitle entries in the data set
	for unittitle in did_headings.findall(".//{urn:isbn:1-931666-22-9}unittitle"):
		# and then we say that in the dictionary, unittitle equals itself plus the data represented as text
		# and then we add a pipe to increase readability of our results, separating multiple entries
		dictionary['unittitle'] = dictionary['unittitle'] + unittitle.text + ' | '
	for container in did_headings.findall(".//{urn:isbn:1-931666-22-9}container"):
		dictionary['container : box | object | Reg Number |'] = dictionary['container : box | object | Reg Number |'] + container.text + ' | '
	for extent in did_headings.findall(".//{urn:isbn:1-931666-22-9}extent"):
		dictionary['extent'] = dictionary['extent'] + extent.text + ' | '
	for physfacet in did_headings.findall(".//{urn:isbn:1-931666-22-9}physfacet"):
		dictionary['physfacet'] = dictionary['physfacet'] + physfacet.text + ' | '
	for physloc in did_headings.findall(".//{urn:isbn:1-931666-22-9}physloc"):
		dictionary['physloc'] = dictionary['physloc'] + physloc.text + ' | '
	# print to test our results
	result_list.append(dictionary)
	print(result_list)

# the chunk of script beginning on line 76 is the CSV writing component. 
# this should not change from script to script. 

with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in result_list:
    	writer.writerow(data)

# Run the code through the terminal one last time with the CSV writing 
# part and a file with the name we've chosen on line 43 should
# appear in the same folder that this file is saved in.

