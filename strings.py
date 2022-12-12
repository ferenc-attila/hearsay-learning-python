test = 'random'

print(test[0])
print(type(test[0]))
print(test.index('d'))

print(test[1:12])
print(test[:3])

print(test[0:5:2])
print(test[-3])
print(test[-1])

anotherTest = 'UPPERlower'

print(anotherTest.upper())
print(anotherTest.lower())

stringToSplit = 'Hello Python'

sliced = stringToSplit.split()

print(sliced)

anotherStringToSplit = 'Hello, Python'

anotherSliced = anotherStringToSplit.split(',')

print(anotherSliced)

# Special characters

print('This is a \t tabulator')
print('This is a \n new line.')
print('It\'s an escape character: \\')
