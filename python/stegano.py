from stegano import lsb
secret = lsb.hide("./pyfile/img.jpg", "Hello World")
secret.save("./pyfile/img.jpg")