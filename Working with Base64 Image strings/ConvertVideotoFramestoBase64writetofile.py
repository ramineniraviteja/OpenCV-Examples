import cv2
import os
from PIL import Image
import io
import base64


cap = cv2.VideoCapture("LinkedIn.MP4")

# Check if camera opened successfully
if (cap.isOpened() == False):
  print("Unable to read camera feed")

i=0
outF = open("myOutFile.txt", "w")

while(True):
  ret, frame = cap.read()
  #print(frame)
  if ret == True:
    i +=1
    input = "input"+str(i)+".jpg"
    
    #Convert to numpy array base64
    im = Image.fromarray(frame.astype("uint8"))
    rawBytes = io.BytesIO()
    im.save(rawBytes, "PNG")
    rawBytes.seek(0)  # return to the start of the file
    encode = base64.b64encode(rawBytes.read())
    encode_str = encode.decode("utf-8")
    outF.write(encode_str)
    outF.write("\n")
    if cv2.waitKey(1) &0xFF == ord('q'):
      break

  # Break the loop
  else:
    break
outF.close()
# When everything done, release the video capture and video write objects
cap.release()
# Closes all the frames
cv2.destroyAllWindows()
