import qrcode
from PIL import Image
qr= main.QRCode(version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,border=4,)

qrcode.add_data("sammy_whatever")
qr.make(fit=True)


