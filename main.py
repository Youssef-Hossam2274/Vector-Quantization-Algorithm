from PIL import Image
from utils import listImages, loadImage, convertImageToGrid, saveImage, convertPixelsToImage



def main():
    # print(listImages("Images"))
    # imageName = input("Enter the name of the image you want to compress:")
    imageName = "House.bmp"

    image = loadImage(imageName)
    image.show()

    pixels = convertImageToGrid(image)

    print(pixels)
    


main()