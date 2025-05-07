from PIL import Image

# >>> SETT FILNAVNET HER <<<
original_path = 'rainy.png'  # Endre til filen du vil bruke
output_path = 'rainy_b.png'  # Valgfritt: endre navnet på det nye bildet

# Velg fargen du vil bruke (her: lys blå)
new_color = (115, 190, 250)

# Åpne bildet og konverter til RGBA
img = Image.open(original_path).convert("RGBA")
pixels = img.getdata()

# Bytt svart med ny farge
new_pixels = []
for pixel in pixels:
    if pixel[0:3] == (0, 0, 0):
        new_pixels.append(new_color + (pixel[3],))
    else:
        new_pixels.append(pixel)

# Lagre det nye bildet
img.putdata(new_pixels)
img.save(output_path)

print(f'Bildet er lagret som {output_path}')