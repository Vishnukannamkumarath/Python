from PIL import Image
f=Image.open("new_image.jpeg")
a=f.resize((150,150))
a.save("vishnu.jpeg")
