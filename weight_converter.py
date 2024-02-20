weight = int(input('Enter the weight: '))
unit= input('(L)bs or (K)g: ')

if unit.upper() == 'L':
   converted = 0.45 * weight
   print(f'you are {converted} kilos')
else:
    converted = weight / 0.45
    print(f'you are{converted} pounds')