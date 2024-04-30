import qrcode

def generate_qr_code(data, filename):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create QR code image
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Save QR code image as PNG file
    qr_img.save(filename)

if __name__ == "__main__":
    # String to encode into QR code
    qr_data = "Hello, World!"

    # Filename for the PNG file
    png_filename = "generated_qr_code.png"

    # Generate and save QR code
    generate_qr_code(qr_data, png_filename)

    print(f"QR code saved as {png_filename}")
