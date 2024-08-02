from PIL import Image
from pyzbar.pyzbar import decode

data = decode(Image.open('path_where_is_the_qr'))

print(data)
