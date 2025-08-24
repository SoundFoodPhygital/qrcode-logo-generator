#!/usr/bin/env python3
import qrcode
import argparse
from PIL import Image
import httpx
from pprint import pprint

# https://shorturl.fm/api/create.php
# https://shorturl.fm/url-shortener-api.php
API_URL = "https://shorturl.fm/api/create.php"


def shorten_url(url: str) -> str:
    data = {"url": url}
    try:
        response = httpx.post(API_URL, json=data)
        response.raise_for_status()
        short_url = response.json()["short_url"]
        print(f"🔗 Accorciamento URL: {url} -> {short_url}")
        if short_url.startswith("http"):
            return short_url
        else:
            print(f"⚠️  Errore nell'accorciamento dell'URL: {short_url}")
            return url
    except httpx.RequestError as e:
        print(f"⚠️  Errore nella richiesta di accorciamento URL: {e}")
        return url


def main(args) -> None:
    data, logo_path, output = args.data, args.logo, args.output

    if args.short_url:
        data = shorten_url(data)

    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    logo = Image.open(logo_path)
    logo_size = int(img.size[0] * 0.25)
    logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

    pos = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)
    img.paste(logo, pos, mask=logo.convert("RGBA"))

    img.save(output)
    print(f"✅ QR con logo salvato in {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Genera un QR code con logo incorporato."
    )
    parser.add_argument("data", type=str, help="Testo o URL da codificare nel QR code.")
    parser.add_argument("--logo", "-l", type=str, help="Percorso del file logo.")
    parser.add_argument("output", type=str, help="Percorso del file di output.")
    parser.add_argument(
        "--short-url",
        "-s",
        action="store_true",
        help="Usa shorturl.fm per accorciare l'URL.",
    )
    args = parser.parse_args()
    main(args)
