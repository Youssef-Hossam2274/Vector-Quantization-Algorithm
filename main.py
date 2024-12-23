from PIL import Image
from utils import listImages, loadImage, convertImageToGrid, saveImage, convertPixelsToImage, saveCodeBook, saveCompressedImage
from vectorQuantization import getCodeBook, compressImage


def compression():
    # print(listImages("Images"))
    # imageName = input("Enter the name of the image you want to compress:")
    
    imageName = "fruit.bmp"
    image = loadImage(imageName)
    pixels = convertImageToGrid(image)


    # width = int(input("Enter the width of the block: "))
    # height = int(input("Enter the height of the block: "))
    # codeBookSize = int(input("Enter the size of the codebook: "))
    width = 8
    height = 4
    codeBookSize = 8
    
    codeBook = getCodeBook(pixels, width, height, codeBookSize)

    saveCodeBook(codeBook)

    compressedPixels = compressImage(pixels, codeBook, width, height)
    
    saveCompressedImage(compressedPixels, "compressedImage.txt")


def decompression():
    pass

def main():
    compression()





main()