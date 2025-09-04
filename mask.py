#This function checks some shaped code against an image mask to see if it is accurate
#image masks have "\n" as "\n", space as space, and hashtag ("#") or at symbol ("@") as any character.

def checkTextMask(text,mask):
    outputMask = ""
    maskSplit = mask.split("\n")
    lineNo = len(maskSplit)
    text = text.split("\n")
    if len(text) < lineNo:
        for i in range(0,lineNo-len(text)):
            text.append("")
    fixedText = []
    for i in range(0,lineNo):
        lineLen = len(maskSplit[i])
        fixedText.append(text[i].ljust(lineLen)[:lineLen])

    text = "\n".join(fixedText)
    
    currentLineNo = 1
    outputMask += str(currentLineNo).ljust(5)
    for i in range(0,len(text)):
        if mask[i] in ["#","@"] and text[i] != " ":
            outputMask += "#"
        elif mask[i] == " " and text[i] == " ":
            outputMask += "#"
        elif mask[i] == "\n" and text[i] == "\n":
            outputMask += "\n"
            currentLineNo += 1
            outputMask += str(currentLineNo).ljust(5)
        else:
            outputMask += text[i]
    
    print("A hashtag '#' indicates a correct character/space placement, any other characters or spaces are incorrect.")
    print(outputMask)
