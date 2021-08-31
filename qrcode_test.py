import qrcode

src = "weixin://wxpay/bizpayurl?pr=uoVSH48zz"
img = qrcode.make(src)

qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=8,
    border=4)
