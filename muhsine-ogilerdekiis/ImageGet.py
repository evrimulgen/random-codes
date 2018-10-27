API_ID = '4994840896590599480'
API_SECRED = '538f73cc0022e546ffe7b7acc6b37102ce356d211efec68af08ee6e44939eaed'

import requests, re, os, os.path, sys
from urllib.request import urlretrieve

URL = "https://tr.pinterest.com/muhsineyidiz/t%C4%B1%C4%9F-i%C5%9Fleri/"
END_POINT = str(sys.argv[1])
#site = requests.get("https://tr.pinterest.com/muhsineyidiz/%s/" % END_POINT)
#file = open(END_POINT + '.html', encoding="utf8")
myPath = "C:\\Users\\Raq\\Desktop\\muhsine"
count = 0
library = []

for i in str(open(END_POINT + '.html', encoding="utf8").readlines()).split(" "):#str(requests.get(URL).text).split(" "):
  if re.findall('http.*\.jpg', i):
    try:
      #if re.findall('http.*\.jpg', i)[0].startswith("https://i.pinimg.com/originals/"):
        current_img = re.findall('http.*\.jpg', i)[0]
        img_lib_name = current_img.split("/")[-1].split(".")[0]
        if img_lib_name not in library:
          count += 1
          library.append(img_lib_name)
          urlretrieve(current_img, os.path.join(myPath, "%s\\%s_%s.jpg" % (END_POINT, END_POINT, str(len(os.listdir(os.path.join(myPath, END_POINT)))))))
    except:
      print("PASSED", i)
print(library, count, sep='\n')