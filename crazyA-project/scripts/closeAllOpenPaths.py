font = CurrentFont()
for glyph in font:
    for contour in glyph:
        if contour.open:
            contour.join

font.save()