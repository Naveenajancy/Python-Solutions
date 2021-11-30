from functools import reduce

def classPhotos(redShirtHeights, blueShirtheights):
    redShirtHeights.sort(reverse=True)
    blueShirtheights.sort(reverse=True)
    shirtInFirstRow = 'RED' if redShirtHeights[0] < blueShirtheights[0] else 'BLUE'
    for idx in range(len(redShirtHeights)):
        redShirtHeight = redShirtHeights[idx]
        blueShirtheight = blueShirtheights[idx]
        if shirtInFirstRow == 'RED':
            if redShirtHeight >= blueShirtheight:
                return False
        else:
            if blueShirtheight >= redShirtHeight:
                return False
    return True




print(classPhotos([5,8,1,3,4], [6,9,2,4,5]))


