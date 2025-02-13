font = CurrentFont()

for glyph in font:
    hasQuads = False
    for contour in glyph:
        for point in contour.points:
            if point.type == "qcurve":
                hasQuads = True
    if hasQuads:
        glyph.convertToCubic()

font.save()
                
                
    
    