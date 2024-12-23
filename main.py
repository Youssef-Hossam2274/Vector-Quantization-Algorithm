from PIL import Image
from utils import listImages, loadImage, convertImageToGrid, saveImage, convertPixelsToImage, saveCodeBook, saveCompressedImage, loadCodeBook, loadCompressedImage
from vectorQuantization import getCodeBook, compressImage, decompressImage


def compression():
    # print(listImages("Images"))
    # imageName = input("Enter the name of the image you want to compress:")
    
    imageName = "photographer.bmp"
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
    codeBook = loadCodeBook()
    width = len(codeBook[0][0])
    height = len(codeBook[0])

    compressedImage = loadCompressedImage("compressedImage.txt")
    pixels = decompressImage(compressedImage, codeBook, width, height)    

    image = convertPixelsToImage(pixels, (len(pixels[0]), len(pixels)))
    image.show()

def main():
    compression()
    decompression()





main()