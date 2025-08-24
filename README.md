# qrcode-logo-generator
A CLI qr-code generator with logo support

## Installation

The project uses `uv` as package manager, we suggest to use `uv` for a better python experience. To install the dependencies, run:

```bash
pip install -e .
```

## Usage

To generate a QR code with a logo, run the following command:

```bash
python main.py --logo "path/to/logo.png" "https://example.com" "output.png"
```

Replace `path/to/logo.png` with the path to your logo image, `https://example.com` with the URL you want to encode, and `output.png` with the desired output file name for the QR code image.

Optionally you can use the --shor-url flag to shorten the URL before generating the QR code:

```bash
python main.py --logo "path/to/logo.png" --short-url "https://example.com" "output.png"
```

Here is the help message for the CLI tool:

```bash
usage: main.py [-h] [--logo LOGO] [--short-url] data output

Genera un QR code con logo incorporato.

positional arguments:
  data                  Testo o URL da codificare nel QR code.
  output                Percorso del file di output.

options:
  -h, --help            show this help message and exit
  --logo LOGO, -l LOGO  Percorso del file logo.
  --short-url, -s       Usa shorturl.fm per accorciare l'URL.
```

## License
This project is licensed under the Apache-2.0 License.
