command = ''
started = False
while True:
    command = input('> ')
    if command == 'start':
        if started:
            print('car is already started')
        else:
            started = True
            print('car is started!Ready to go!!.....')
    elif command == 'stop':
        if not started:
            print('car is already stopped')
        else:
            started = False
            print('car stopped')
    elif command == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - exit the game
        ''')
    elif command == 'quit':
        break
    else:
        print('Sorry! I do not understand')
