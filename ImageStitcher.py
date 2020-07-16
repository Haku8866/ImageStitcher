from PIL import ImageColor, Image
import glob, os

class SplicedImage:
    def __init__(self, img, coordx, coordy):
        self.img = img
        self.coordx = coordx
        self.coordy = coordy

names = []
coords = []
unames = []

totalw = 0
totalh = 0

cnstw = 0
cnsth = 0

lowest = [9999, 9999]

for infile in glob.glob("*.png"):
    file, ext = os.path.splitext(infile)
    if file == "Output":
        continue
    test = file.split("-")
    if int(test[0]) < lowest[0]:
        lowest[0] = int(test[0])
    if int(test[1]) < lowest[1]:
        lowest[1] = int(test[1])

for infile in glob.glob("*.png"):
    file, ext = os.path.splitext(infile)
    if file == "Output":
        continue
    coords = file.split("-")
    if int(coords[0]) == lowest[0] and int(coords[1]) == lowest[1]:
        coords = file.split("-")
        cnstw = int(coords[0])
        cnsth = int(coords[1])

for infile in glob.glob("*.png"):
    file, ext = os.path.splitext(infile)
    if file == "Output":
        continue
    coords = file.split("-")
    img2 = Image.open(infile)
    names.append(SplicedImage(img2, int(coords[0])-cnstw, int(coords[1])-cnsth))

for image in names:
    if not image.coordy in unames:
        totalh += image.img.height
        unames.append(image.coordy)
unames = []
for image in names:
    if not image.coordx in unames:
        totalw += image.img.width
        unames.append(image.coordx)
print(f"Output: {totalw} x {totalh}")
output = Image.new("RGBA", (totalw, totalh), color=0)

cnt = 0
len = len(names)

for image in names:
    output.paste(image.img, (image.coordx*16, image.coordy*16))
    cnt += 1
    print(f"{cnt}/{len} complete...")

print("Saving image as output.png...")
output.save("output.png")

print("Done! Press enter to finish.")
input()