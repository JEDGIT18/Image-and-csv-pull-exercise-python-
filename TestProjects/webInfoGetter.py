import random
from  urllib import request
import urllib.request

#----------reads and writes to files------------
fw = open('sample.txt', 'w') #makes or writes a file
fw.write('Writing something\n')#writes to file
fw.write('Writing something again \n') # writes to file
fw.close()
fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()

def downloadTxtData(txtUrl):
    response = request.urlopen(txtUrl)
    txt = response.read()
    txtStr = str(txt)
    lines = txtStr.split("\\n")
    filePath = r'txt.csv'
    fx = open(filePath, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()

def downloadImage(url):
    name = random.randint(0,256)
    image = str(name) + ".jpg"
    urllib.request.urlretrieve(url, image)
