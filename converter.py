def stream2ASCII(f, filename = None, encoding = "ANSI"):
    assert "b" in f.mode , "Requires a Bytes Stream"
    assert b"P6\x0a" == f.read(3), "Not a Valid binary ppm file"
    header = bytes()
    while header.count(b"\x0a") < 2:
        header += f.read(1)
    width, height, band = map(lambda x : int(x),header.replace(b" ", b"\x0a").split(b"\x0a")[:-1])
    if not filename:
        filename = f.name.strip(".ppm")+"modified.ppm"
    o = open(filename, mode = 'wt', encoding = "ANSI")
    o.write("P3 {} {} {}\n".format(width, height, band))
    for i,j in enumerate(f.read()):
        o.write(str(j) + " ")
    assert i == width * height * 3 - 1, "Incorrect File Size"
    f.close()
    o.close()

def bin2ASCII(infile, outfile = None, encoding = "ANSI"):
    stream2ASCII(open(infile, "rb"), outfile, encoding = encoding)
    
def stream2bin(f, filename = None, encoding = "ANSI"):
    assert "P3 " == f.read(3), "Not a Valid ASCII ppm file"
    header = ""
    while "\n" not in header:
        header += f.read(1)
    width, height, band = map(lambda x : int(x),header.rstrip("\n").split(" "))
    if not filename:
        filename = f.name.strip(".ppm")+"modified.ppm"
    o = open(filename, mode = 'wb')
    o.write(bytes("P6\x0a{} {}\x0a{}\x0a".format(width, height, band), encoding = encoding))
    for i,j in enumerate(f.read().split(" ")[:-1]):
        o.write(bytes([int(j)]))
    assert i == width * height * 3 - 1, "Incorrect File Size"
    f.close()
    o.close()
            
def ASCII2bin(infile, outfile = None, encoding = "ANSI"):
    stream2bin(open(infile, "r", encoding = encoding), outfile, encoding = encoding)



