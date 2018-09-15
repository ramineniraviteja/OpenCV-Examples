import glob
import os
import base64
import codecs

if os.path.exists("base64.txt"):
   os.remove("base64.txt")
else:
   print("Sorry, I can not remove file base64.txt")


images_dir="/home/ubuntu/input_frames"
os.chdir(images_dir)
files = glob.glob("*.jpg")
files.sort(key=os.path.getmtime)
#print(files)
#print("\n".join(files))
#print(len(files))

f = open(os.path.join("/home/ubuntu/", "base64.txt"), 'w')
#with open(os.path.join("/home/ubuntu/", "base64.txt"), 'w') as f:
i=0
for image in files:
    i+=1
    b64 = base64.encodestring(open(image,"rb").read())
    base64_string = b64.decode("utf8").replace('\n', '')
    f.write(base64_string)
    f.write("\n")
f.close()
