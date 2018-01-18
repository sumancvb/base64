import base64
image = open('sample.jpg', 'rb')
image_read = image.read()
image_64_encode = base64.encodestring(image_read)

file = open("test.txt","w")
file.write(image_64_encode)
file.close()

#print image_64_encode
image_64_decode = base64.decodestring(image_64_encode) 
image_result = open('sample_decode.jpg', 'wb') # create a writabl$
image_result.write(image_64_decode)

print("done")