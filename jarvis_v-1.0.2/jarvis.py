import sys, os, pyowm, pyttsx3, time, datetime, webbrowser, smtplib, wikipedia, wolframalpha, random
from playsound import playsound

sys.path.insert(0, 'modules/')
from data_store import *
from func import *
sys.path.insert(0, '/../')

#import speech_recognition as sr #pip install speechRecognition


ai = 'JARVIS :'

while True:
    
    os.system('color a')
    
#=====================  Query/History  ============================================
    history_file = open('includes\\history_file.jv', 'a')
    
    query = input('YOU : ')
    query = query.lower()
    
    DateTime = datetime.datetime.now().strftime('%H:%M') + ' ' + datetime.datetime.now().strftime('%D')
    str(DateTime)
    
    history_details = query + ' - ' + DateTime
    history_file.write(history_details)
    history_file.write('\n')
    history_file.close()
    
#=====================  J.A.R.V.I.S. Version  ============================================
    if 'jarvis --v' in query or 'jv --v' in query:
        print ('''                  ################################################
                  #                J.A.R.V.I.S.                  #
                  #                                              #
                  #  Project        : JARVIS AI                  #
                  #  Model no.      : JV_001928                  #
                  #  Version        : V-1.0.2                    #
                  #  Developer      : Vaibhav Shukla             #
                  #  Special Thanks : Aditya Gaur                #
                  #                                              #
                  ################################################''')
        speak('Hi, I\'m JARVIS, version one point zero point two')
#=====================  Chat History  ============================================
    elif 'show' in query and 'history' in query or 'chat' in query and 'history' in query or 'history' in query:
        history_file = open('includes\\history_file.jv', 'r')
        r_history_file = history_file.readlines()
        y = 1

        if r_history_file != []:
            pr('Here is the history of what you said me at what time -')
            for x in r_history_file:
                print(f'{y}.) {x}')
                y += 1
            speak('Here is the history of what you said at what time -')
        else:
            pr('There is no saved History in there.')
            speak('There is no saved History in there.')
        history_file.close()
        
    elif 'delete' in query and 'history' in query or 'clear' in query and 'history' in query:
        
        pr('Do you really want me to clear all history. [Y/N]')
        speak('Do you really want me to clear all history.')
        choice = str(input())

        if choice in choice_y:
            history_file = open('includes\\history_file.jv', 'w')
            history_file.write('')
            print(' All history cleared.')
            speak('All history cleared.')
        elif choice in choice_n:
            print(' Ok sir !')
            speak('Ok sir')
        else:
            print('You were suppose to answer in yes or no.')
            speak('You were suppose to answer in yes or no.')

        history_file.close()

    elif 'cls' in query:
        history_file = open('includes\\history_file.jv', 'w')
        history_file.write('')
        history_file.close()
        pr('Command Executed !')
        speak('Command Executed !')
        

#=========================      Greet      ============================================

    elif 'hi' in query or 'hey' in query:
        hi_ans = random.choice(hi)
        pr(hi_ans)
        speak(hi_ans)
        
    elif 'hello' in query:
        greet = random.choice(list(rd_greet.keys()))
        greet_lang = rd_greet.get(greet)
        pr(f'{greet} that\'s Hello in {greet_lang}, how can i help you ?')
        speak(f'{greet}, that\'s Hello in {greet_lang}, how can i help you ?')
    
    elif 'good' in query or 'like' in query or 'great' in query or 'love' in query or 'bravo' in query or 'wow' in query:
        if 'bye' not in query:
            glad_rnd = random.choice(glad)
            pr(glad_rnd)
            speak(glad_rnd)

    elif "whats up" in query or "what\'s up" in query or 'how are you' in query:
        rand_fine = random.choice(fine)
        pr(rand_fine)
        speak(rand_fine)
        

#=========================      Flip a coin      ============================================
    elif 'flip a coin' in query:
        pr('Flipping...')
        speak('Flipping')

        playsound('mp3\\coinflip.mp3')

        toss = random.randint(0, 1)

        if toss == 0:
            pr('Its Head')
            speak('Its Head')
        elif toss == 1:
            pr('Its Tail')
            speak('Its Tail')

            
#=========================      Remember      ============================================
    elif 'told' in query and 'remember' in query or 'reminder' in query:
        remem_file = open('includes\\remem_file.jv', 'r')
        r_remem_file = remem_file.readlines()
        y = 1

        if r_remem_file != []:
            pr('You told me to remember following things -')
            for x in r_remem_file:
                print(f'{y}.) {x}')
                y += 1
            speak('You told me to remember following things -')
        else:
            pr('You haven\'t told me anything to remember.')
            speak('You haven\'t told me anything to remember.')
        remem_file.close()
        
    elif 'remember' in query:
        remem = format(query.replace('remember', ''))
        remem_file = open('includes\\remem_file.jv', 'a')
        
        if remem != '':
            remem_file.write(remem)
            remem_file.write('\n')
            pr('Ok I\'ll remember that !')
            speak('Ok I\'ll remember that')
        else:
            pr('Maybe you forget to tell what to remember.')
            speak('Maybe you forget to tell what to remember.')
        remem_file.close()
        

    elif 'forget' and '#' in query:
        chars = 'forget# '
        for c in chars:
            query = format(query.replace(c, ''))
        query = int(query)
        query -= 1
        infile = open('includes\\remem_file.jv','r').readlines()
        with open('includes\\remem_file.jv','w') as outfile:
            for index,line in enumerate(infile):
                if index != query:
                    outfile.write(line)
        pr(f'Forgotten #{query+1}')
        speak(f'Forgotten number {query+1}')

    elif 'forget' in query:
        remem_file = open('includes\\remem_file.jv', 'r') #open reading
        r_remem_file = remem_file.readlines()
        
        if r_remem_file != []:
            remem_file.close()      #close the reading file.
            pr('Do you really want me to forget everything that I remember. [Y/N]')
            speak('Do you really want me to forget everything that I remember.')
            choice = str(input())

            if choice in choice_y:
                remem_file = open('includes\\remem_file.jv', 'w')
                remem_file.write('')
                pr('As per your choice, I erased everything from my memory.')
                speak('As per your choice, I erased everything from my memory.')
            elif choice in choice_n:
                pr('Ok sir !')
                speak('Ok sir')
            else:
                pr('You were suppose to answer in yes or no.')
                speak('You were suppose to answer in yes or no.')
        else:
            pr('You haven\'t told me anything to remember.')
            speak('You haven\'t told me anything to remember.')
        remem_file.close()

#==========================  YourName  ==================================================

    elif 'your' in query and 'name' in query:
        if 'my' in query:
            pr('Please be clear with the words, I mean your name or my name')
            speak('Please be clear with the words, I mean your name or my name')
        else:
            pr('My name is Jarvis and I\'m your assistant AI.')
            speak('My name is Jarvis and I\'m your assistant AI.')
            

#==========================  MyName  ==================================================

    elif 'change my name' in query:
        speak('Sure!')
        pr('Enter your new name :')
        speak('Enter your new name.')
        name = str(input())

        pr(f'So its {name} right ! [Y/N]')
        speak(f'So its {name} right !')
        choice = str(input())

        if choice in choice_y:
            name_file = open('includes\\name_file.jv', 'w')
            name_file.write(name)

            pr(f'Fine, i\'ll call you {name} from now.')
            speak(f'Fine, i\'ll call you {name} from now.')
        elif choice in choice_n:
            pr('Ok fine !')
            speak('ok fine')

        name_file.close()
    
    elif 'my' in query and 'name' in query:
        if 'your' in query:
            pr('Please be clear with the words, I mean your name or my name')
            speak('Please be clear with the words, I mean your name or my name')
        else:
            name_file = open('includes\\name_file.jv', 'r')
            r_name_file = name_file.read()

            if r_name_file is '':
                name_file.close()
                pr_f(' You haven\'t told me your name. Do you want me to remember your name ?[Y/N]')
                speak('You haven\'t told me your name. Do you want me to remember your name ?')
                choice = str(input())

                if choice in choice_y:
                    pr_f('Enter your name please')
                    speak('Enter your name please')
                    name = str(input())
                    
                    pr_f(f'So its {name} right ! [Y/N]')
                    speak(f'So its {name} right !')
                    choice = str(input())

                    name_file = open('includes\\name_file.jv', 'w')
                    
                    if choice in choice_y:
                        name_file.write(name)
                        
                        pr(f'Fine, i\'ll call you {name} from now.')
                        speak(f'Fine, i\'ll call you {name} from now.')
                    elif choice in choice_n:
                        pr_f('So what should I call you ?')
                        speak('So what should I call you ?')
                        name = str(input())

                        name_file.write(name)
                        
                        pr(f'Fine, i\'ll call you {name} from now.')
                        speak(f'Fine, i\'ll call you {name} from now.')
                        
                    else:
                        pr('You were supposed to answer in yes or no !')
                        speak('You were supposed to answer in yes or no !')

                    name_file.close()

                    
                elif choice in choice_n:
                    pr('Ok fine, no problem. Perhaps you would like to talk more with me !')
                    speak('Ok fine, no problem. Perhaps you would like to talk more with me !')
                else:
                        pr('You were supposed to answer in yes or no !')
                        speak('You were supposed to answer in yes or no !')
            elif r_name_file is not '':
                pr(f'That\'s {r_name_file} !')
                speak(f'That\'s {r_name_file}')
                

#==========================  Sites Surf  ==================================================

    elif 'open google' in query:
        pr('Opening Google...')
        speak('Opening Google')
        webbrowser.open('google.com')
        pr_l('Here you go !')
        speak('Here you go !')
    elif 'open youtube' in query:
        pr('Opening YouTube...')
        speak('Opening YouTube')
        webbrowser.open('youtube.com')
        pr_l('Here you go !')
        speak('Here you go !')
    elif 'open facebook' in query or 'open fb' in query:
        pr('Opening Facebook...')
        speak('Opening Facebook')
        webbrowser.open('fb.com')
        pr_l('Here you go !')
        speak('Here you go !')
    elif 'open instagram' in query or 'open insta' in query:
        pr('Opening Instagram...')
        speak('Opening Instagram')
        webbrowser.open('instagram.com')
        pr_l('Here you go !')
        speak('Here you go !')

#==========================  Site Searches  ==================================================
    elif 'search google' in query:
        pr('Searching on Google...')
        speak('Searching on Google...')
        g_results = format(query.replace('search google ', ''))
        webbrowser.open(f'google.com/search?q={g_results}')
        pr_l('Here you go !')
        speak('Here you go !')
    elif 'search youtube' in query:
        pr('Searching on YouTube...')
        speak('Searching on YouTube...')
        yt_results = format(query.replace('search youtube ', ''))
        webbrowser.open(f'youtube.com/results?search_results={yt_results}')
        pr_l('Here you go !')
        speak('Here you go !')
        

#==========================  Wikipedia  ==================================================
    elif 'wikipedia' in query:
        try:
            pr('Searching Wikipedia')
            speak('Searching Wikipedia')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=3)
            results_speak = wikipedia.summary(query, sentences=2)
            pr_l('According to wikipedia...')
            pr_l(results)
            speak('According to wikipedia...')
            speak(results_speak)
        except:
            pr('No result found, maybe due to incorrect keyword or bad internet connectivity.')
            speak('No result found, maybe due to incorrect keyword or bad internet connectivity.')

#==========================  Weather  ==================================================
    elif 'weather' in query:
        try:
            pr_f('Enter Location :')
            speak('Enter location')

            city = str(input())
            location = owm.weather_at_place(city)
            weather = location.get_weather()
            temp = weather.get_temperature('celsius')
            humidity = weather.get_humidity()

            
            current_temp = int(temp.get('temp'))
            max_temp = int(temp.get('temp_max'))
            min_temp = int(temp.get('temp_min'))

            pr_f(f'Here are the weather conditions of {city}')
            pr_f(f'Current Temperature: {current_temp} °C')
            pr_f(f'Maximum Temperature: {max_temp} °C')
            pr_f(f'Minimum Temperature: {min_temp} °C')
            pr_f(f'And Humidity: {humidity} %')
            
            speak(f'Current Temperature: {current_temp} °Celsius')
            speak(f'Maximum Temperature: {max_temp} °Celsius')
            speak(f'Minimum Temperature: {min_temp} °Celsius')
            speak(f'And Humidity: {humidity} %')
        except:
            pr('Sorry sir, nothing found. Please check for internet access.')
            speak('Sorry sir, nothing found. Please check for internet access.')


#==========================  Open Files and Exe(s) ==================================================

    elif 'gta3 cheats' in query:
        pr_f('Opening GTA 3 Cheats...')
        speak('Opening')
        gta3_cheats_dir = 'E:\\Grand Theft Auto 3\\cheats.txt'
        os.startfile(gta3_cheats_dir)
        pr('Command Executed Successfully')
    elif 'gtavc cheats' in query:
        pr_f('Opening GTA Vice City Cheats...')
        speak('Opening')
        gta3_cheats_dir = 'E:\\Grand Theft Auto - Vice City\\cheats.txt'
        os.startfile(gta3_cheats_dir)
        pr('Command Executed Successfully')
    elif 'gta3' in query:
        pr_f('Playing GTA 3...')
        speak('Playing GTA 3')
        gta3_dir = 'E:\\Grand Theft Auto 3\\gta3.exe'
        os.startfile(gta3_dir)
        pr('Command Executed Successfully')
    elif 'gtavc' in query:
        pr_f('Playing GTA Vice City...')
        speak('Playing GTA Vice City')
        gta3_dir = 'E:\\Grand Theft Auto - Vice City\\gta-vc.exe'
        os.startfile(gta3_dir)
        pr('Command Executed Successfully')
    elif 'chrome' in query:
        pr_f('Opening...')
        chrome_dir = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
        os.startfile(chrome_dir)
        speak('opening')
        pr('Command Executed Successfully')


#=========================   Timer ==================================================
    elif 'timer' in query:
        speak('Set Timer')
        sec = int(input('Enter time limit (in sec) : '))
        
        pr_f(f'So alarm will ring after {sec} seconds')
        for i in range(sec):
            time.sleep(1)
            
        music_dir = 'C:\\Users\\Vinod\\Music\\Playlists'
        songs = os.listdir(music_dir)
        for music_list in songs:
            pr(music_list)
        os.startfile(os.path.join(music_dir, songs[0]))

#==========================  Folders/Directories ==================================================    
    elif 'create folder ' in query:
        folder_name = format(query.replace('create folder ', ''))
        createFolder(folder_name)
        pr(f'New folder created {folder_name}')
        speak(f'New folder created {folder_name}')

    elif 'create folder' in query:
        createFolder('New Folder')
        pr(f'New folder created')
        speak(f'New folder created')
        
        
#=========================   Email ==================================================

    elif 'email to vaibhav' in query:
        try:
            pr('What would be the content ?')
            speak('What would be the content ?')

            content = str(input('Content :'))
            to = 'shuklavaibhav336@gmail.com'
            sendEmail(to, content)
            pr('Email sent to Vaibhav')
            speak('Email sent to Vaibhav')
        except:
            pr('Sorry, unable to sent email')
            speak('Sorry, unable to sent email')
            

#=========================   PlayMusic  ==================================================

    elif 'music dir' in query:
        pr('Opening Music Directory...')
        speak('got it')
        os.system(f'explorer C:\\Users\\Vinod\\Music')
    elif 'play music' in query:
        pr('Playing Music...')
        speak('Playing Music')
        music_dir = 'C:\\Users\\Vinod\\Music\\Playlists'
        songs = os.listdir(music_dir)
        for music_list in songs:
            pr(music_list)
        os.startfile(os.path.join(music_dir, songs[0]))

#=========================   Directories  ==================================================

    elif 'jv project' in query:
        os.system(f'explorer H:\\python\\jarvis\\jarvis')
        pr('Opening Jarvis Project...')
        speak('Opening Jarvis Project...')
    elif 'test area' in query:
        os.system(f'explorer H:\\test')
        pr('Opening Test Directory...')
        speak('Opening Test Directory...')

#=========================   DateTime  ==================================================

    elif 'time' in query:
        strTime = datetime.datetime.now().strftime('%H:%M')
        pr(f'The time is {strTime}')
        speak(f'The time is {strTime}')
    elif 'date' in query:
        strDate = datetime.datetime.now().strftime('%D')
        pr(f'The date is {strDate}')
        speak(f'The date is {strDate}')

#=========================   Calculator  ==================================================
    elif 'calc help' in query:
        print ('''                  ####################################################
                  #                Calculator Help                   #
                  #  Step 1.) Enter first number.                    #
                  #  Step 2.) Enter operator number.                 #
                  #           such as [+, -, *, /, ** or //]         #
                  #           + is for Addition                      #
                  #           - is for Subtraction                   #
                  #           * is for Multiplication                #
                  #           / is for Division                      #
                  #           ** is for Squaring                     #
                  #           // is for Remainder Division           #
                  #  Step 3.) Enter second number.                   #
                  #           (you have to enter the power of the    #
                  #           number if you are using **)            #
                  ####################################################''')
        speak ('Here are the instructions to use the Calculator.')

    elif 'calc'in query:
        try:
            speak('All right')
            num1 = float(input('Enter 1st Number : '))
            operator = str(input('Enter Operator : '))
            num2 = float(input('Enter 2nd Number : '))

            if operator == '+':
                sum = Calc.add(num1, num2)
            elif operator == '-':
                sum = Calc.sub(num1, num2)
            elif operator == '*':
                sum = Calc.multi(num1, num2)
            elif operator == '/':
                sum = Calc.div(num1, num2)
            elif operator == '**':
                sum = Calc.sqr(num1, num2)
            elif operator == '//':
                sum = Calc.d_div(num1, num2)
            else:
                pr('Invalid Operator ! Use +, -, *, /, ** or // only. To see the list of features of Operators write \'calc help\'')
                speak('Invalid Operator !')

            pr(f'Answer is {sum}')
            speak(f'Answer is {sum}')
        except:
            pr('Invalid Operator ! Use +, -, *, /, ** or // only. To see the list of features of Operators write \'calc help\'')
            speak('Invalid Operator !')

    elif '+' in query or '-' in query or '*' in query or '/' in query:
        pr('Type \'calc\' keyword to use Calculator')
        speak('Type \'calc\' keyword to use Calculator')

#=========================   Launch Explorer  ==================================================

    elif 'goto' in query:
        speak('Sure Sir')
        query = format(query.replace('goto ', ''))
        os.system(f'explorer c:\\{query}')
        pr('Operation executed !')
        continue

#=========================   Trick   ==================================================
    elif 'show' in query and 'trick' in query:
        x=0

        def trick():
            global x
            pr_f('Trick', x)
            os.system('explorer C:\\"{}"'.format(query.replace('open', '').replace('launch', '')))
            x+=1
            
        while True:
            try:
                trick()
            except KeyboardInterrupt:
                pr_f('Really nigguh !!')
                speak('Really nigguh')

#=========================   Siri/Alexa/Bixbi/Friday   ==================================================
    elif 'siri' in query:
        siri_ans = random.choice(siri)
        pr(siri_ans)
        speak(siri_ans)
    elif 'alexa' in query:
        alexa_ans = random.choice(alexa)
        pr(alexa_ans)
        speak(alexa_ans)
    elif 'bixbi' in query:
        bixbi_ans = random.choice(bixbi)
        pr(bixbi_ans)
        speak(bixbi_ans)
    elif 'friday' in query:
        friday_ans = random.choice(friday)
        pr(friday_ans)
        speak(friday_ans)

#=========================   Exit  ==================================================


    elif 'exit' in query or 'bye' in query or 'close' in query:
        pr('Bye have a great time !!')
        speak('Bye have a great time !!')
        sys.exit()

#=========================   Wifi Connect and Disconnect  ==================================================
    elif 'wifi' in query or 'wlan' in query:
        if 'disconnect' in query:
            os.system(f'netsh wlan disconnect')
            pr_l('Disconnected !')
            speak('Disconnected !')
        elif 'connect' in query:
            query = format(query.replace('wifi ', ''))
            query = format(query.replace('wlan ', ''))
            query = format(query.replace('connect ', ''))
            os.system(f'netsh wlan connect name="{query}"')
            pr(f'Connected to {query}!')
            speak(f'Connected to {query}!')

#=========================   Shutdown/Restart/Sleep/Logoff/Signout  ==================================================
    
    elif 'shutdown f' in query:
        speak('Ok , good bye Sir !!')
        os.system('shutdown /s /t 0')
        sys.exit()
    elif 'restart f' in query:
        speak('Ok, see you later Sir !!')
        os.system('shutdown /r /t 0')
        sys.exit()
    elif 'logoff f' in query:
        speak('Ok Sir !!')
        os.system('shutdown /l /t 0')
        sys.exit()
    elif 'restart' in query:
        speak('Ok Sir !!')
        speak('You have about 30 seconds to save your files or abort the process of restarting PC. ')
        os.system('shutdown /r')
        sys.exit()
    elif 'shutdown' in query:
        speak('Ok Sir !!')
        speak('You have about 30 seconds to save your files or abort the process of shutting down PC.')
        os.system('shutdown /s')
        sys.exit()
    elif 'logoff' in query:
        speak('Ok Sir !!')
        speak('You have about 30 seconds to save your or abort the process of logging off PC')
        os.system('shutdown /l')
        sys.exit()
    elif 'sleep' in query:
        speak('Ok Sir')
        os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
    elif 'abort' in query:
        speak('Ok Sir')
        os.system('shutdown /a')
        speak('Command Executed')

#=========================  Chatting  =========================================================
    elif query is '':
        blank_rnd = random.choice(blank)
        pr(blank_rnd)
        speak(blank_rnd)
    elif 'fact' in query:
        fact_rnd = random.choice(facts)
        pr(fact_rnd)
        speak(f'Do you know, {fact_rnd}')
    elif 'google fact' in query:
        google_fact_rnd = random.choice(google_facts)
        pr(google_fact_rnd)
        speak(google_fact_rnd)
    elif 'what' in query and 'can' in query and 'do' in query:
    	print ('''                  ####################################################
                  #       I can serve you following facilities :     #
                  #                                                  #
                  #  1.) I can play music, movies and games.         #
                  #  2.) I can remember things.                      #
                  #  3.) I can search anything on Google, Youtube    #
                  #      and Wikipedia.                              #
                  #  4.) I can tell you Facts about many things.     #
                  #  5.) I can control your PC and perform functions #
                  #      like shutdown, restart, logout, sleep etc.  #
                  #  6.) I can set timer and alarm.                  #
                  #  7.) I can act as a calculator.                  #
                  #  8.) I can send Email.                           #
                  #  9.) You can chat with me.                       #
                  #  10.) I'll connect you to wifi, whenever you     #
                  #       want.                                      #
                  ####################################################''')
    	speak('Here are some top 10 services I can provide you.')

    elif 'marry' in query or 'married' in query:
        married_rnd = random.choice(married)
        pr(married_rnd)
        speak(married_rnd)
    elif 'hurt' in query or 'hell' in query or 'angry' in query or 'bad' in query or 'damn' in query or 'poor' in query or 'shit' in query:
        remorse_rnd = random.choice(remorse)
        pr(remorse_rnd)
        speak(remorse_rnd)
    elif 'oh' in query or 'ok' in query or 'fine' in query or 'hmm' in query:
        expressions_rnd = random.choice(expressions)
        pr(expressions_rnd)
        speak(expressions_rnd)

#=========================   Not Understand  ==================================================
    else:
            speak('Searching')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    pr(results)
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    pr_f('According to Wikipedia')
                    pr_l(results)
                    speak('According to Wikipedia')
                    speak(results)
        
            except:
                
                engine.setProperty('rate', 200)
                notunderstand = random.choice(exception)
                pr_f('Nothing found !')
                pr(notunderstand)
                speak(notunderstand)
                if notunderstand != exception[2]:
                    print('Do you want me to search it on web. [Y/N]')
                    speak('Do you want me to search it on web.')

                    choice = input()
                    
                    if choice in choice_y:
                        print('\n Searching on Google...')
                        speak('Searching on Google')
                        webbrowser.open(f'google.com/search?q={query}')
                    elif choice in choice_n:
                        pr('No problem !')
                        speak('No problem.')
                    else:
                        pr('You were supposed to answer in yes or no !')
                        speak('You were supposed to answer in yes or no !')
                    engine.setProperty('rate', 150)
