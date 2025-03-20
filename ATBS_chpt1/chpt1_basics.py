#program says hi, asks for name, and asks for age
print('Hello, world!')
print('What is your name?')
name = input()  #input name
print('It\'s nice to meet you, ' + name)
print ('Your name is ' + str(len(name)) + ' characters long.')
print('How old are you? (enter a number)')
age = input() #input age
print('In five years, you will be ' + str(int(age) + 5))