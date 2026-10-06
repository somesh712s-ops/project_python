import qrcode
import os 
data = "https://wa.me/917404684266"

qr = qrcode.QRCode(version = 1 ,box_size = 10,border = 4 )

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_colour = "black",back_colour = "white")
img.save("qrcode.png")

img.save("qrcode.png")
os.startfile("qrcode.png")
