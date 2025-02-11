font = CurrentFont()

featureTagGlyphName = dict()

for glyph in font:
    if "." in glyph.name:
        baseName, feaTag = glyph.name.split(".")
        if len(feaTag) == 4:
            if feaTag not in featureTagGlyphName:
                featureTagGlyphName[feaTag] = []
            featureTagGlyphName[feaTag].append((baseName, glyph.name))
feaCode = ""
for feaTag, glyphs in featureTagGlyphName.items():
    feaCode += f"feature {feaTag} {{\n"
    baseNames = []
    glypyhNames = []
    for baseName, glyphName in glyphs:
        baseNames.append(baseName)
        glypyhNames.append(glyphName)
    baseNames = " ".join(baseNames)
    glypyhNames = " ".join(glypyhNames)
    feaCode += f"   sub [{baseNames}] by [{glypyhNames}];\n"
    feaCode += f"}} {feaTag};\n"
    feaCode += "\n"
    
print(feaCode)

font.features.text += feaCode

