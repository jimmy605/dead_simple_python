def spam():
    message = 'Spam'
    word = 'spam'
    for _ in range(100):
        seperator = ', '
        message += seperator + word
    message += seperator
    message += 'spam!'
    
    return message

print(spam())