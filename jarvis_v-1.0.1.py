import sys

sent = ['']
words = ['']
choice_y = ['y', 'Y', 'Yes', 'yes', 'YES']
choice_n = ['n', 'N', 'No', 'no', 'NO']

while '' in sent and '' in words:
    name = ''
    x = input('YOU : ')
    words.append(x)
    sent.append(x)
    words = x.split()

    notunderstand = 'Sorry I don\'t understand'
    ai = 'JARVIS :'


    ########################################################################
    if 'hi' in words and sent:
        print(ai, 'Hey! how can I help you ?')
        sent = ['']
        words = ['']
    ########################################################################
    elif 'hello' in words and sent:
        print(ai, 'Namaste! that\'s Hello in Hindi, how can i help you ?')
        sent = ['']
        words = ['']
    ########################################################################
    elif 'your' in words and 'name' in words:
        if 'my' in words:
            print('Please be clear with the words, I mean your name or my name')
            sent = ['']
            words = ['']
        else:
            print(ai, 'My name is Jarvis and I\'m your assistant AI.')
            sent = ['']
            words = ['']
    ########################################################################
    elif 'my' in words and 'name' in words:
        if 'your' in words:
            print('Please be clear with the words, I mean your name or my name')
            sent = ['']
            words = ['']
        else:
            if name == '':
                print('You haven\'t told me your name. Do you want me to remember your name ?[Y/N]')
                choice = str(input())

                if choice in choice_y:
                    name = str(input('Enter your good name please : '))
                    print('So its', name, 'right ! [Y/N]')
                    choice = str(input())

                    if choice in choice_y:
                        print('So I\'ll call you', name)
                    elif choice in choice_n:
                        name = ''
                        name = str(input('So what should I call you : '))
                        print('Fine I\'ll call you', name, 'from now.')
                    else:
                        print('Invalid input, you were supposed choose within given options ?[Y/N]')

                        
                elif choice in choice_n:
                    print('It\'s OK, Fine!')
                else:
                    print('Invalid input, you were supposed choose within given options ?[Y/N]')

            else:
                print('Your name is', name)
            sent = ['']
            words = ['']
    ########################################################################
    elif '+' in words or '-' in words or '*' in words or '/' in words:
        
        if words[1] == '+':
            add = float(words[0]) + float(words[2])
            print('That\'s', add)
            sent = ['']
            words = ['']
        elif words[1] == '-':
            sub = float(words[0]) - float(words[2])
            print('That\'s', sub)
            sent = ['']
            words = ['']
        elif words[1] == '*':
            mul = float(words[0]) * float(words[2])
            print('That\'s', mul)
            sent = ['']
            words = ['']
        elif words[1] == '/':
            div = float(words[0]) / float(words[2])
            print('That\'s', div)
            sent = ['']
            words = ['']
        else:
            print('Enter valid numbers or operators')
    ########################################################################
    elif 'exit' in sent:
        print('Bye have a great time !!')
        sys.exit()
    ########################################################################
    else:
        print(notunderstand)
        sent = ['']
        words = ['']
    ########################################################################
    
    
