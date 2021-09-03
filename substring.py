sentence = 'The quick brown fox jumped over the lazy dog.'

query = sentence.find('oops') #adding the value quick within the string will return an index of 4.
# query_two = sentence.index('oops')

print(query)
# print(query_two)

query = 'oops' in sentence

print(query)