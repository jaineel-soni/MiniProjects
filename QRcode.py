import qrcode 
from PIL import Image
img = qrcode.make("how you doinn???")
img.save("img.png")
