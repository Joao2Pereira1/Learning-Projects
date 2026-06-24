import io

import numpy as np
from PIL import Image, ImageFilter, ImageOps


# Função para abrir e processar a imagem
def open_image(image_path):
    img = Image.open(image_path)
    return img


# Função para converter a imagem para escala de cinza
def convert_to_grayscale(img):
    return img.convert("L")


# Função para inverter as cores da imagem
def invert_colors(img):
    img_array = np.array(img)
    inverted_img_array = 255 - img_array
    return Image.fromarray(inverted_img_array)


# Função para redimensionar a imagem
def resize_image(img, width, height):
    return img.resize((width, height))


# Função para aplicar um filtro de desfoque (blur)
def blur_image(img):
    return img.filter(ImageFilter.BLUR)


# Função principal para processar a imagem
def process_image(path, algorithm):
    with Image.open(path) as img:
        if algorithm == "gray_scale":
            img = ImageOps.grayscale(img)
        elif algorithm == "invert_colors":
            img = ImageOps.invert(img.convert("RGB"))
        elif algorithm == "resize_image":
            img = img.resize((300, 300))
        elif algorithm == "blur_image":
            img = img.filter(ImageFilter.GaussianBlur(radius=3))
        else:
            raise ValueError("Algoritmo desconhecido")

    # Salva a imagem processada em memória como PNG
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    return buffer.getvalue()
