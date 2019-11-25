from PIL import Image

def entropize(image, rdiff = (0,0), gdiff = (0,0)):
    r,g,b = image.split()
    width, height = image.size #l u r d
    bedge   = (max(rdiff[0], gdiff[0], 0), max(rdiff[1], gdiff[1], 0), width + min(rdiff[0], gdiff[0], 0), height + min(rdiff[1], gdiff[1], 0))
    redge   = (max(0, -1 * rdiff[0], gdiff[0] - rdiff[0]), max(0, -1 * rdiff[1], gdiff[1] - rdiff[1]), min(width, width - rdiff[0], width + gdiff[0] -rdiff[0]), min(height, height - rdiff[1], height + gdiff[1] -rdiff[1]))
    gedge   = (max(0, -1 * gdiff[0], rdiff[0] - gdiff[0]), max(0, -1 * gdiff[1], rdiff[1] - gdiff[1]), min(width, width - gdiff[0], width + rdiff[0] -gdiff[0]), min(height, height - gdiff[1], height + rdiff[1] -gdiff[1]))
    rr = r.crop(redge)
    gg = g.crop(gedge)
    bb = b.crop(bedge)
    merge = Image.merge("RGB", (rr,gg,bb))
    return merge

def entropize_image(infile, rdiff = (0,0), gdiff = (0,0), outfile = None, fileformat = None):
    if not fileformat:
        ext = infile.split(".")[-1]
        if ext == infile:
            raise OSError("Incorrect File Extension")
        else:
            fileformat = ext
    if fileformat == "jpg":
        fileformat = "jpeg"
    if not outfile:
        outfile = infile + "broken.{}".format(fileformat) 
    entropize(Image.open(infile), rdiff = rdiff, gdiff = gdiff).save(outfile, format = fileformat)

if __name__ == "__main__":
    entropize_image(input("File Path\n>>> "), (15,15), (15,15))
