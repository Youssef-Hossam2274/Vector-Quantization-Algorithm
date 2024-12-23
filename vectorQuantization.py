TODO: "remove this implementaiton and implement the vector quationation algorithm" # type: ignore
def getCodeBook(pixels: list[list], width: int, hight: int, codeBookSize: int) -> list[list[list]]:
   
    codebook = []
    for i in range(0, len(pixels), hight):
        for j in range(0, len(pixels[0]), width):
            block = [row[j:j+width] for row in pixels[i:i+hight]]
            codebook.append(block)
            if len(codebook) == codeBookSize:
                return codebook
    return codebook

def findClosestBlock(block: list[list], codeBook: list[list[list]]) -> list[list]:
    minDistance = float('inf')
    closestBlock = None
    for codeBlock in codeBook:
        distance = sum(
            (block[i][j] - codeBlock[i][j]) ** 2
            for i in range(len(block))
            for j in range(len(block[0]))
        )
        if distance < minDistance:
            minDistance = distance
            closestBlock = codeBlock
    return closestBlock


def compressImage(pixels: list[list], codeBook: list[list[list]], width: int, hight: int) -> list[list[int]]:
    compressedPixels = [[0] * (len(pixels[0]) // width) for _ in range(len(pixels) // hight)]
    for i in range(0, len(pixels), hight):
        for j in range(0, len(pixels[0]), width):
            block = [row[j:j+width] for row in pixels[i:i+hight]]
            closestBlock = findClosestBlock(block, codeBook)
            label = codeBook.index(closestBlock)
            compressedPixels[i // hight][j // width] = label
    return compressedPixels

def decompressImage(compressedImage: list[list[int]], codeBook: list[list[list]], width: int, height: int) -> list[list[int]]:
    pixels = []
    for i in range(len(compressedImage)):
        row = []
        for j in range(len(compressedImage[0])):
            label = compressedImage[i][j]
            block = codeBook[label]
            for k in range(height):
                if len(pixels) <= i * height + k:
                    pixels.append([])
                pixels[i * height + k].extend(block[k])
    return pixels