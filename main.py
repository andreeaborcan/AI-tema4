from xml.etree import ElementTree as ET


def pattern():
	e = ET.parse('pattern.aiml').getroot()
	i=0
	L=[]
	for pattern in e.findall('pattern'):
		L.append(pattern.text)
		i=i+1
	return L
	
	return None

print(pattern())
  

# de aici incepe un fel de main

x = input()
