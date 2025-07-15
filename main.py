#!/usr/bin/env python3
import sys
import qrcode
from PIL import Image

if len(sys.argv) < 4:
    print("Uso: qrcode_logo.py <testo_o_url> <logo.png> <output.png>")
    sys.exit(1)

data, logo_path, output = sys.argv[1], sys.argv[2], sys.argv[3]

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

logo = Image.open(logo_path)
logo_size = int(img.size[0] * 0.2)
logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

pos = ((img.size[0] - logo_size)//2, (img.size[1] - logo_size)//2)
img.paste(logo, pos, mask=logo.convert("RGBA"))

img.save(output)
print(f"✅ QR con logo salvato in {output}")
