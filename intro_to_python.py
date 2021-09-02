meal_completed = True
total = 100
tip = total * 1/5
total = total + tip
receipt = "Your total is " + str(total)
print(receipt)

first = 'Springer'
second = 'Bregman'
third = 'Altvue'

print(first)

first = third

print(first)

#sentence = 'the quick brown fox jump over the lazy dog'
#print(sentence)

# sentence = 'The quick brown fox jumped'
# sentence -> variable
# 'The quick brown fox jumped' -> string
# = -> assignment

sentence = 'the quick brown fox jumped over the lazy dog'
sentence_two = sentence.upper()


print(sentence)
print(sentence_two)

sentence = 'the quick brown fox jumped over the lazy dog'.capitalize()
print(sentence)

sentence = 'the quick brown fox jumped over the lazy dog'.title()
print(sentence)

sentence = 'THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG'.lower()
print(sentence)

# The quick brown fox jumped
# T => 0
# h => 1
# e => 2
# ' ' => 3

starter_sentence = 'The quick brown fox jumped'

new_sentence = 'Thy' + starter_sentence[3:]

print(new_sentence)

# Heredoc

content = """
Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.

Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

Integer posuere erat a ante venenatis dapibus posuere velit aliquet.
""".strip()

print(content)

content = """
Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.

Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

Integer posuere erat a ante venenatis dapibus posuere velit aliquet.
"""

print(repr(content))

long_string = '\nNullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.\n\nVestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.\n\nInteger posuere erat a ante venenatis dapibus posuere velit aliquet.\n'

print(long_string)