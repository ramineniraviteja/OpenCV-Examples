import base64

b64 = base64.encodestring(open("inputframe.jpeg","rb").read())

encode = b64.decode("utf8")

outputframe = "output.jpeg"
with open(outputframe, "wb") as fh:
    fh.write(base64.decodebytes(encode))

