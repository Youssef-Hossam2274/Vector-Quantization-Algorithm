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
 
    # width is the width of the block
    # height is the height of the block
    # codeBookSize is the size of the codebook

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

def test_getCodeBook():
    pixels = [[1, 2, 7, 9, 4, 11],
              [3, 4, 6, 6, 12, 12],
              [4, 9, 15, 14, 9, 9],
              [10, 10, 20, 18, 8, 8],
              [4, 3, 17, 16, 1, 5],
              [4, 5, 18, 18, 5, 6]]

    codeBook = getCodeBook(pixels, 2, 2, 8)
    print(codeBook)

def main():
    compression()
    decompression()
    # test_getCodeBook()

main()

