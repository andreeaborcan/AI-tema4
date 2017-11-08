from xml.etree import ElementTree as ET


def pattern():
	e = ET.parse('pattern.aiml').getroot()
	i=0
	L=[]
	for pattern in e.findall('pattern'):
		L.append(pattern.text.lower())
		i=i+1
	return L
	
	return None

print(pattern())
  

# de aici incepe un fel de main

def sch(word):
    PATTERN = pattern()
    line_count = 1

    text = ''
    for line in stdin:
        text += line
    print(text)
    
    text = re.findall(text);

    for line in stdin:
        print("line is: " + line)
        for pat in PATTERN:
            x = re.match('[!?.]([a-z ,;]*)=([a-z ,;]*)[!?.]', line)#.match
            if(x is not None and word.lower() in x.group(1).lower()):
                print("g1: "+x.group(1))
                print("Definition : " + x.group(2))
                print("found at line no:" + str(line_count))
            print(x)
        line_count += 1

sch("tata")
