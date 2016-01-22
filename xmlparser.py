import xml.etree.ElementTree as ET

data = '''
<ammaland>
<campus>
	<bangalore>
		<cse>xyz</cse>
		<ece>abc</ece>
		<eie>def</eie>
	</bangalore>
	<amritapuri>
		<cse> LOL amma </cse>
		<ece name="louda"> LOLOL amma </ece>
	</amritapuri>
</campus>
</ammaland>'''

campus = ET.fromstring(data)
items = campus.findall('ammaland/campus/')
print len(items)
print ('Bangalore') , items.find('bangalore').items('cse').text
