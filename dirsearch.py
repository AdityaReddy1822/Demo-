import pyqrcode
s = "https://www.google.com"
url = pyqrcode.create(s)
url.png("qr.png")