import qrcode

data = input('Put the information to be codified: ')
qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color = 'black', back_coor = 'white')

img.save('path_to_save')