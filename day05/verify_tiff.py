from PIL import Image

with Image.open("sample12.tif") as img:
    page_count = 0

    while True:
        try:
            img.seek(page_count)
            page_count += 1
        except EOFError:
            break

print("Total TIFF pages:", page_count)

assert page_count == 12

print("TIFF page count verified!")