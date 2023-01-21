import pyqrcode

# The content of the QR code
data = str(input("Enter site address : "))

# Generating the QR code
qr = pyqrcode.create(data)

# Printing the QR code on the screen
print(qr.terminal(quiet_zone=1))

# Saving QR code to file
qr.svg("qr.svg", scale=8)