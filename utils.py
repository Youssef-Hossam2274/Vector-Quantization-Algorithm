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

def loadCodeBook(fileName: str = "codeBook.txt") -> list[list[list]]:
    with open(fileName, 'r') as file:
        lines = file.readlines()
        codeBookSize = int(lines[0].split(':')[1])
        width = int(lines[1].split(':')[1])
        height = int(lines[2].split(':')[1])
        
        codeBook = []
        block = []
        for line in lines[3:]:
            if line.strip():
                block.append(list(map(int, line.split())))
                if len(block) == height:
                    codeBook.append(block)
                    block = []
        return codeBook

def loadCompressedImage(fileName: str) -> list[list[int]]:
    with open(fileName, 'r') as file:
        compressedImage = []
        for line in file:
            compressedImage.append(list(map(int, line.split())))
    return compressedImage