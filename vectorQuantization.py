def getCodeBook(pixels: list[list], width: int, height: int, codeBookSize: int) -> list[list[list]]:
    imageWidth = len(pixels)
    imageHeight = len(pixels[0])
    blocks = []

    # Divide the image into blocks
    for i in range(0, imageWidth, height):
        for j in range(0, imageHeight, width):
            block = []
            for x in range(height):
                row = []
                for y in range(width):
                    if i + x < imageWidth and j + y < imageHeight:
                        row.append(pixels[i + x][j + y])
                    else:
                        row.append(0)  # Fill with zeros if out of bounds
                block.append(row)
            blocks.append(block)

    def calculateAverageBlock(blocks):
        averageBlock = [[0] * width for _ in range(height)]
        for block in blocks:
            for i in range(height):
                for j in range(width):
                    averageBlock[i][j] += block[i][j]
        for i in range(height):
            for j in range(width):
                averageBlock[i][j] = round(averageBlock[i][j] / len(blocks))
        return averageBlock

    def splitBlocks(blocks, averageBlock):
        lowerBlocks = []
        upperBlocks = []
        for block in blocks:
            lowerBlock = [[max(0, averageBlock[i][j] - 1) for j in range(width)] for i in range(height)]
            upperBlock = [[min(255, averageBlock[i][j] + 1) for j in range(width)] for i in range(height)]
            if findClosestBlock(block, [lowerBlock, upperBlock]) == lowerBlock:
                lowerBlocks.append(block)
            else:
                upperBlocks.append(block)
        return lowerBlocks, upperBlocks

    codeBook = [calculateAverageBlock(blocks)]
    while len(codeBook) < codeBookSize:
        newCodeBook = []
        for block in codeBook:
            lowerBlocks, upperBlocks = splitBlocks(blocks, block)
            if lowerBlocks:
                newCodeBook.append(calculateAverageBlock(lowerBlocks))
            if upperBlocks:
                newCodeBook.append(calculateAverageBlock(upperBlocks))
        codeBook = newCodeBook

    return codeBook[:codeBookSize]

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