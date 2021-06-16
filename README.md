# Text-Encrypter

Encrypts text with python

## Examples

```bash
#outputs the encrypted string
$ python3 encrypter.py "Hello World"

#outputs the encrypted content of the file
$ python3 encrypter.py ./text.txt
```

## Decorder

How to decode the encrypted string

```python
>>> text = "72&@!&101&@!&108&@!&108&@!&111&@!&32&@!&87&@!&111&@!&114&@!&108&@!&100&@!&" # This is the encoded string
>>> text_num = text.split("&@!&")
>>> print(chr(int(text_num[0])))
```

This will output "Hello World"
