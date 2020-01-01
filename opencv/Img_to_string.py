import base64
 
with open("lena.jpg", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    print (str)

    f= open("lena.txt","w+")
    
    f.write(str.decode())
    f.close()