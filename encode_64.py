import base64
image = open('sample.jpg', 'rb')
image_read = image.read()
image_64_encode = base64.encodestring(image_read)

file = open("test.txt","w")
file.write(image_64_encode)
file.close()
print ("encoding done")
