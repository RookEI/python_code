sentence = 'The quick brown fox jumped over the lazy dog.'

sentence = sentence.replace('quick', 'slow')

print(sentence.replace('quick', 'slow'))
print(sentence)

sentence = 'The quick brown fox jumped over the lazy dog.'

print(sentence[-4:])

url = 'https://google.com'

print(url.strip('https://'))

url = url.lstrip('https://')
url = url.rstrip('.com')

print(url.capitalize())