alpha = 'abcdefghijklmnopqrstuvwxyz'
key = 3
newMessage = ''
oldMessage = ''

message = input('Please enter a message: ')

for character in message:
    if character in alpha:
        position = alpha.find(character)
        newPosition = (position + key) % 26
        newCharacter = alpha[newPosition]
        newMessage += newCharacter
    else:
        newMessage += character

print('Your new message is: ', newMessage)

for character in newMessage:
    if character in alpha:
        position = alpha.find(character)
        newPosition = (position - key) % 26
        newCharacter = alpha[newPosition]
        oldMessage += newCharacter
    else:
        oldMessage += character

print('Your new message is: ', oldMessage)
