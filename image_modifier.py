from PIL import Image
import glob, os

for infile in glob.glob("ic_*"):
    img = Image.open(infile).convert("RGB")
    img.rotate(90).resize((128,128)).save("/opt/icons/" + infile, "JPEG")
