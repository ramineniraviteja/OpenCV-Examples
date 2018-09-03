import base64
from PIL import Image
import cv2
from StringIO import StringIO
import numpy as np
import os
import io



with open('xyz.txt') as f:
 i=0
 for base64_string in f:
   i+=1
   if i==1:
      #print(i)
      sbuf = StringIO()
      sbuf.write(base64.b64decode(base64_string))
      pimg = Image.open(sbuf)
      np_array_image = np.array(pimg)
      #return np.array(pimg)
      text = 'Hello This is Streaming Frame ' + str(i)
      cv2.putText(np_array_image, text, (0,25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
      output_frame = "output"+str(i)+".jpg"
      #cv2.imwrite(os.path.join("/home/ubuntu/output_frames/", output_frame), np_array_image)
      im = Image.fromarray(np_array_image.astype("uint8"))
      rawBytes = io.BytesIO()
      im.save(rawBytes, "PNG")
      rawBytes.seek(0)  # return to the start of the file
      print(base64.b64encode(rawBytes.read())) 
      #if a == base64_string:
      #   print("True")
