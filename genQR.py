import qrcode as qr


def gen_qrcode(text: str, file: str):
    qr_code = qr.make(text)
    qr_code.save(file)
