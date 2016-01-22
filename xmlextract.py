#Web apps using python
#Week 5 assignmetn 1
import urllib
import xml.etree.ElementTree as ET


url = raw_input("Enter location: ")
data = urllib.urlopen(url).read()
print "Retrieving ", url
print len(data), " characters"
#Data contains the entire document retrived using the url
#Now generating the XML Tree
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
print "Count: " , len(lst)
result = 0;
for item in lst:
	num = item.find('count').text
	result = result + int(num)
print "Sum: ", result