import PIL


def wb_negative(image):
    im = PIL.Image.open(image)
    pixels = im.load()
    x, y = im.size
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            bw = 255 - (r + g + b) // 3
            pixels[i, j] = bw, bw, bw
    im.save("out.png")


wb_negative('')