# # Python 3.5.2 
import base64
from PIL import Image
import cv2
import numpy as np
import os
import io
from random import randint
import datetime
import io
from base64 import decodestring

with open('xyz.txt') as f:
 i=0
 for base64_string in f:
      i+=1
      sbuf = io.BytesIO()
      sbuf.write(base64.b64decode(base64_string))
      pimg = Image.open(sbuf)
      np_array_image = np.array(pimg)
      text = 'Time ' + str(datetime.datetime.now())
      cv2.putText(np_array_image, text, (0,25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
      cv2.putText(np_array_image, str(randint(0, 9)), (13,60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
      output_frame = "output"+str(i)+".jpg"
   
      #Convert to numpy array base64
      im = Image.fromarray(np_array_image.astype("uint8"))
      rawBytes = io.BytesIO()
      im.save(rawBytes, "PNG")
      rawBytes.seek(0)  # return to the start of the file
      encode = base64.b64encode(rawBytes.read())
      encode_str = encode.decode("utf-8")
      
      #Convert Base64 to Image
      outputframe = "output"+str(i)+".jpeg"
      with open(outputframe, "wb") as fh:
          fh.write(base64.decodebytes(encode))
