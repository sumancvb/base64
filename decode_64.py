import base64
file = open("test.txt","r")
image_64_encode = file.read()
file.close()

#print image_64_encode
image_64_decode = base64.decodestring(image_64_encode) 
image_result = open('sample_decode.jpg', 'wb') # create a writabl$
image_result.write(image_64_decode)
print ("decoding done")


