msg = input('> ')
words = msg.split(' ')
emojis = {
    ":)" : '😀',
    ":(" : '😔'
}
output = ''
for i in words:
    output += emojis.get(i,i) + " "
print(output)