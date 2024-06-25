
---

# Eliminación de Fondo Blanco de Imágenes

Este script en Python utiliza la biblioteca PIL (Python Imaging Library) para eliminar el fondo blanco de una imagen y reemplazarlo por transparencia. Es útil para procesar imágenes y eliminar fondos uniformes blancos.

## Requisitos

- Python 3.x
- Biblioteca PIL (Pillow)

Para instalar Pillow, ejecuta:

```bash
pip install Pillow
```

## Uso

El script `remove_background.py` acepta dos argumentos:
1. La ruta de la imagen de entrada.
2. La ruta de la imagen de salida.

### Ejecución del Script

Para ejecutar el script, usa el siguiente comando:

```bash
python remove_background.py <imagen_entrada> <imagen_salida>
```

Donde:
- `<imagen_entrada>` es la ruta a la imagen que deseas procesar.
- `<imagen_salida>` es la ruta donde se guardará la imagen procesada.

### Ejemplo

```bash
python remove_background.py imagen_original.png imagen_sin_fondo.png
```

### Descripción del Código

1. **Importación de la Biblioteca**:
    ```python
    from PIL import Image
    ```

2. **Definición de la Función `remove_white_background`**:
    - Abre la imagen de entrada.
    - Convierte la imagen al modo "RGBA" para manejar la transparencia.
    - Obtiene los datos de la imagen.
    - Procesa cada píxel de la imagen:
        - Si el píxel es blanco (o un tono de blanco), lo convierte en transparente.
        - Si no, lo deja sin cambios.
    - Guarda la nueva imagen con el fondo transparente.

    ```python
    def remove_white_background(image_path, output_path):
        img = Image.open(image_path)
        img = img.convert("RGBA")

        datas = img.getdata()

        new_data = []
        for item in datas:
            # Cambia todos los píxeles blancos (también tonos de blancos)
            # a transparente
            if item[0] > 200 and item[1] > 200 and item[2] > 200:
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(item)

        img.putdata(new_data)
        img.save(output_path, "PNG")
    ```

3. **Ejecución del Script**:
    - Verifica que se hayan proporcionado los argumentos correctos.
    - Llama a la función `remove_white_background` con los argumentos proporcionados.

    ```python
    if __name__ == "__main__":
        import sys
        if len(sys.argv) != 3:
            print("Uso: python remove_background.py <imagen_entrada> <imagen_salida>")
        else:
            remove_white_background(sys.argv[1], sys.argv[2])
    ```

---
