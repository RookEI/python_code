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


heading = "Python: An Introduction, and Python: Advanced"

header, _, subheader = heading.partition(': ')

print(header)
print(subheader)

first, second, third = heading.partition(': ')

print(first)
print(second)
print(third)


tags = 'python,coding,programming,development'

list_of_tags = tags.split(',')
#list_of_tags = tags.split()

print(list_of_tags)

heading = "Python: An Introduction"

heading, subheading = heading.split(': ')

print(heading)
print(subheading)


api_data = '5'
greeting = 'Hi there'

print(api_data.isalpha())
print(greeting.isalpha())

print(api_data.isnumeric())
print(greeting.isnumeric())