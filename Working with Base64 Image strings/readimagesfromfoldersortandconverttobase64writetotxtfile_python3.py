import glob
import os
import base64
import codecs

#Remove the text fileif exists
if os.path.exists("base64.txt"):
   os.remove("base64.txt")
else:
   print("Sorry, I can not remove file base64.txt")

#Input Images directory
images_dir="/home/ubuntu/input_frames"
os.chdir(images_dir)
#access only .jpg format images
files = glob.glob("*.jpg")
#Sort Filename by creation time stamp
files.sort(key=os.path.getmtime)

#Read images from input folder in a loop and convert to base64 format. Then write to Text file
f = open(os.path.join("/home/ubuntu/", "base64.txt"), 'w')
i=0
for image in files:
    i+=1
    b64 = base64.encodestring(open(image,"rb").read())
    base64_string = b64.decode("utf8").replace('\n', '')
    f.write(base64_string)
    f.write("\n")
f.close()
