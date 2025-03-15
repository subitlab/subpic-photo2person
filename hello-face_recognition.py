import face_recognition as fr
from PIL import Image
image = fr.load_image_file("006.jpg")
faceLocations = fr.face_locations(image)
print(len(faceLocations))
for i in faceLocations:
    t,r,b,l = i
    face_image = image[t:b,l:r]
    pil_image = Image.fromarray(face_image)
    print(str(i))
    pil_image.save("output/" + str(i) + ".png")