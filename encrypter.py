import sys
import os

letters = []
text = None
letters_text = []
encoded_text_list = []
encoded_text = None

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('Please Enter The Text/File That You Want To Encode')
        quit(-1)
    else:
        isFile = os.path.isfile(str(sys.argv[1]))
        if isFile == True:
            with open(str(sys.argv[1])) as f:
                contents = f.read()
                text = contents
        else:
            text = str(sys.argv[1])

for x in range(0, 1141):
    letters.append(chr(int(x)))

for x in text:
    letters_text.append(x)

def getEncodedText(x):
    if ord(x) in range(0, 1141):
        encoded_text = str(ord(x)) + "&@!&"
        return str(encoded_text)
    else:
        return str(ord(x))

for x in letters_text:
    encoded_text_list.append(getEncodedText(x))

encoded_text = ''.join(x for x in encoded_text_list)
print(encoded_text)
