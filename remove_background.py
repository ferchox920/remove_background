from PIL import Image

def remove_white_background(image_path, output_path):
    img = Image.open(image_path)
    img = img.convert("RGBA")

    datas = img.getdata()

    new_data = []
    for item in datas:
      
        if item[0] > 200 and item[1] > 200 and item[2] > 200:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    img.putdata(new_data)
    img.save(output_path, "PNG")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Uso: python remove_background.py <imagen_entrada> <imagen_salida>")
    else:
        remove_white_background(sys.argv[1], sys.argv[2])
