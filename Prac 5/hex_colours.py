COLOUR_TO_CODE = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "aquamarine1": "#7fffd4", "azure1": "#f0ffff", "beige": "#f5f5dc", "bisque1": "#ffe4c4", "black": "#000000", "BlanchedAlmond": "#ffebcd", "blue1": "#0000ff", "brown": "#a52a2a"}
print(COLOUR_TO_CODE)

colour_id = input("Enter the colour: ")
while colour_id != "":
    if colour_id in COLOUR_TO_CODE:
        print(colour_id, "is", COLOUR_TO_CODE[colour_id])
    else:
        print("Invalid colour name")
    colour_id = input("Enter the colour: ")