from PIL import Image
import os
import numpy as np

def listImages(folder_path):
    return [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

def loadImage(imageName: str) -> Image:
    imagePath = os.path.join("Images", imageName)
    return Image.open(imagePath)


def convertImageToGrid(image: Image) -> list[list]:
    grayscale_image = image.convert("L")
    pixels = list(grayscale_image.getdata())
    width, height = grayscale_image.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

    return pixels    

def saveImage(image:Image, savePath:str):
    imagePath = os.path.join("Images", savePath)
    image.save(imagePath)

def convertPixelsToImage(pixels, size):
    # Ensure pixels is a numpy array
    pixels = np.array(pixels, dtype=np.uint8)
    
    # Create an Image object from the pixel array
    image = Image.fromarray(pixels)
    
    # Resize the image to the specified size
    image = image.resize(size)
    
    return image

def saveCodeBook(codeBook: list[list[list]], fileName: str = "codeBook.txt"):
    with open(fileName, 'w') as file:
        file.write(f'len:{len(codeBook)}\n')
        file.write(f'width:{len(codeBook[0][0])}\n')
        file.write(f'hight:{len(codeBook[0])}\n')
        for block in codeBook:
            for row in block:
                file.write(' '.join(map(str, row)) + '\n')
            file.write('\n')

def saveCompressedImage(compressedImage: list[list], fileName: str):
    with open(fileName, 'w') as file:
        for row in compressedImage:
            file.write(' '.join(map(str, row)) + '\n')