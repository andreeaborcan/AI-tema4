import re
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


def sch(word, file_name):
    word=word.lower()
    patterns = pattern()
    line_count = 1
    """
    text = ''
    for line in stdin:
        text += line[0:-1]
    print(text)

    text = re.sub('[.?!]+', '$', text);
    text = text.split('$');
    print(text)
    """
    pos = 0
    with open(file_name, 'r') as input_file:
        for line in input_file:
            line = line.lower()
            line = re.sub('[.?!]+', '$', line)
            line = line.split('$')
            for sentence in line:
                for pat in patterns:
                    #print(sentence)
                    x = re.match('([-a-z0-9 ,;]*)([ ,]'+pat+')([-a-z0-9 ,;]*)', sentence)#.match
                    #if x is not None:
                    #print(x.groups())
                    if(x is not None and word.lower() in x.group(1).lower()):
                        print("Found:            \"" + sentence+"\"")
                        print("Definition:       \""+x.group(3)+"")
                        print("found at line no: " + str(line_count))
                        #print("g1: "+x.group(1))
                    #print(x)
            line_count += 1


while(True):
	print("ce definitie cauti?")
	x = input()
	sch(x, "text2")



