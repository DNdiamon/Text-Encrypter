import sys

text = None

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Please Enter The Encoded Text")
    else:
        text = str(sys.argv[1])

if text != None:
    text = text
    i_array = []
    res = None

    text_num = text.split("&@!&")
    if text != None:
        for x in text_num:
            try:
                i = chr(int(x))
                i_array.append(i)
            except:
                pass
        res = ''.join(n[0] for n in i_array)
        print(res)
