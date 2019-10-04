import os
os.system('pip install pyinstaller')
os.system('pip install pyowm')
os.system('pip install pyttsx3')
os.system('pip install wikipedia')
os.system('pip install wolframalpha')
os.system('pip install geocoder')
os.system('pip install playsound')
os.system('pip install speechrecognition')
os.system('cls')


import sys, shutil, win32com.client, pyowm, pyttsx3, time, datetime, webbrowser, smtplib, wikipedia, wolframalpha, random
from playsound import playsound

sys.path.insert(0, 'modules/')
from func import *

#import speech_recognition as sr #pip install speechRecognition


#==================================================================================
#=========================== Profile Check ========================================
#==================================================================================

pro_file = open('includes\\profile.jv')
pro_file_r = pro_file.read()

if pro_file_r == '':
    print('Sir ! you are running this program for first time \nSo first we need to create your profile')
    speak('Sir ! you are running this program for first time, So first we need to create your profile')
    speak('press any key to continue')
    os.system('pause')
    pro_file = open('includes\\profile.jv', 'w')
    pro_file.close()
else:
    print('You have already installed J.A.R.V.I.S.')
    speak('You have already installed JARVIS')
    sys.exit()
pro_file.close()

#==================================================================================
#==================================================================================
#==================================================================================

os.system('cls')

print('Welcome  here !')
speak('Welcome  here !')
print('\n')

print('I\'m  J.A.R.V.I.S. !')
speak('I\'m  JARVIS !')
print('Just A Rather Very Intelligent System')
speak('Just A Rather Very Intelligent System')
print('\n')

print('I\'m here, present in your service...')
speak('I\'m here, present in your service...')
print('\n')

print('Please enter your credentials (the fields with * are optional)')
speak('Please enter your credentials')

pro_file = open('includes\\profile.jv', 'a')

print('\n')
print('Enter your name :')
speak('Enter your name please')
name = str(input())
pro_file.write(name)
pro_file.write('\n')


print('\n')
print('Enter your Date of Birth :')
speak('Enter your date of birth')
dob = str(input())
pro_file.write(dob)
pro_file.write('\n')


print('\n')
print('Enter your phone number : *')
speak('Enter your phone number, it is optional you may skip this')
phoneno = str(input())
pro_file.write(phoneno)
pro_file.write('\n')


print('\n')
print('Enter your Email ID :')
speak('Enter your email ID')
email = str(input())
pro_file.write(email)
pro_file.write('\n')


print('\n')
print('Enter your Music Directory : *')
speak('Enter your music directory (optional)')
music_dir = str(input())
pro_file.write(music_dir)
pro_file.write('\n')


print('\n')
print('Enter your Video Directory : *')
speak('Enter your Video directory (optional)')
movie_dir = str(input())
pro_file.write(movie_dir)
pro_file.write('\n')


print('\n')
print('Enter Serial key : (type \'trial\' to install trial version)')
speak('Enter serial key of the product')
serial_key = str(input())
if serial_key == 'trial':
	ex_date = datetime.datetime.now().strftime('%Y-%m-%d') + '0000-00-30'
    pro_file.write(ex_date)
    pro_file.write('\n')
else:
    while serial_key != 'S1-MRVAIBH-20040131':
        print('Incorrect Serial Key !')
        speak('Incorrect Serial Key !')
        serial_key = str(input())

if serial_key == 'S1-MRVAIBH-20040131':
    pro_file.write(serial_key)
    pro_file.write('\n')

pro_file.close()

os.system('cls')

print('Profile Created !!')
speak('profile created')
os.system('cls')
#==================================================================================
#========================== Create EXE ============================================
#==================================================================================
print('Writing jarvis.py')
speak('writing jarvis.py')
time.sleep(2)
os.system('cls')

jv_file = open('modules\\jarvis.py', 'w')
jv_file_r = jv_file.write('''from main import *''')
jv_file.close()
print('jarvis.py Created')
speak('jarvis.py created')
time.sleep(1)
os.system('cls')

print('Creating EXE')
speak('creating exe')
time.sleep(1)
os.system('cls')
os.system('pyinstaller --hidden-import=win32com.client --hidden-import=pyttsx3 --hidden-import=pyttsx3.drivers --hidden-import=pyttsx3.drivers.dummy --hidden-import=pyttsx3.drivers.espeak --hidden-import=pyttsx3.drivers.nsss --hidden-import=pyttsx3.drivers.sapi5 --hidden-import=pyowm --hidden-import=wikipedia --hidden-import=wolframalpha --hidden-import=playsound --hidden-import=speechrecognition --hidden-import=geocoder -F -i images\\jv_icon.ico modules\\jarvis.py')
os.system('cls')

#==================================================================================
#==================================================================================
#==================================================================================



#==================================================================================
#========================== Create Uninstaller ====================================
#==================================================================================
print('Creating Uninstaller')
speak('creating uninstaller')
time.sleep(2)
os.system('cls')

un_file = open('modules\\uninstall.py', 'w')
un_file_r = un_file.write('''import os, shutil
desktop = r'C:\\Users\\Public\\Desktop'
shortcut_dsk = os.path.join(desktop, 'J.A.R.V.I.S..lnk') 
print('Program Uninstalled Successfully') 
try:
	os.remove('setup.exe')
	os.remove('requirements.txt')
	os.remove('J.A.R.V.I.S..lnk')
	os.remove('jarvis.exe')
	os.remove(shortcut_dsk)
	shutil.rmtree('includes')
	shutil.rmtree('mp3')
	shutil.rmtree('__pycache__')
except:
	pass
os.remove('uninstall.exe')''')
un_file.close()

os.system('pyinstaller -F -i images\\uninstall_icon.ico modules\\uninstall.py')

os.system('cls')

#==================================================================================
#==================================================================================
#==================================================================================


print('Re-Arranging Files...')
speak('rearranging files')
os.rename('dist\\jarvis.exe', 'jarvis.exe')
os.rename('dist\\uninstall.exe', 'uninstall.exe')
time.sleep(2)
os.system('cls')

#==================================================================================
#========================== Create Shorcut ========================================
#==================================================================================
print('Creating Shortcut')
speak('creating shortcut')
time.sleep(1)
os.system('cls')

dir_path = os.path.dirname(os.path.realpath(__file__))
desktop = r'C:\Users\Public\Desktop' # path to where you want to put the .lnk
path_dsk = os.path.join(desktop, 'J.A.R.V.I.S..lnk')
target_dsk = os.path.join(dir_path, 'jarvis.exe')
# icon_dsk = r'images\jv_icon.ico' # not needed, but nice

shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut(path_dsk)
shortcut.Targetpath = target_dsk
# shortcut.IconLocation = icon_dsk
shortcut.WindowStyle = 1 # 7 - Minimized, 3 - Maximized, 1 - Normal
shortcut.save()

shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut('J.A.R.V.I.S..lnk')
shortcut.Targetpath = target_dsk
# shortcut.IconLocation = icon_dsk
shortcut.WindowStyle = 1 # 7 - Minimized, 3 - Maximized, 1 - Normal
shortcut.save()

#==================================================================================
#==================================================================================
#==================================================================================


print('Removing Unwanted Trash')
speak('removing unwanted trash')
time.sleep(1)
os.system('cls')

os.remove('jarvis.spec')
os.remove('uninstall.spec')
shutil.rmtree('build')
shutil.rmtree('dist')
shutil.rmtree('modules')
shutil.rmtree('images')

print('Great ! J.A.R.V.I.S. is installed on your system. Now you are ready to give me commands')
speak('Great ! JARVIS is installed on your system. Now you are ready to give me commands')

os.startfile(desktop + r'\J.A.R.V.I.S..lnk')
os.system('exit')