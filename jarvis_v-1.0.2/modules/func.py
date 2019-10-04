import sys, os, pyowm, pyttsx3, time, datetime, webbrowser, smtplib, wikipedia, wolframalpha, random
from playsound import playsound

#========================== Calculator Function ========================================
class Calc:
	def add(num1,num2):
		return num1 + num2

	def sub(num1,num2):
		return num1 - num2

	def multi(num1,num2):
		return num1 * num2
				
	def div(num1,num2):
		return num1 / num2

	def sqr(num1,num2):
		return num1 ** num2

	def d_div(num1,num2):
		return num1 // num2


#=========================  Print Function  ===============================================
def pr(sent):
    print('\n' + 'JARVIS : ' + sent + '\n')
def pr_f(sent):
    print('\n' + 'JARVIS : ' + sent)
def pr_l(sent):
    print('JARVIS : ' + sent + '\n')

#=========================  Speak Function  ===============================================
client = wolframalpha.Client('XH36VW-TQ664L22RL')
owm = pyowm.OWM('341e0b6e855b5d16826afae9a1eb2d58')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
engine.runAndWait()


def speak(audio):
    os.system('color c')
    engine.say(audio)
    engine.runAndWait()
    os.system('color a')

#========================== Create Folder Function ========================================

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except:
        print('Error in creating new folder - ' + directory)
        
#============================= Alarm Function =============================================

def alarm():
    hour = int(input('Enter hour: '))
    min = int(input('Enter minute: '))
    sec = int(input('Enter seconds: '))

    print(f'Alarm is set for {hour}:{min}:{sec}')

    while True:
        if time.localtime().tm_hour==hour and time.localtime().tm_min == min and time.localtime().tm_sec == sec:
            print('Wake UP')
            speak('Wake UP')
            break
    music_dir = 'C:\\Users\\Vinod\\Music\\Playlists'
    songs = os.listdir(music_dir)
    for music_list in songs:
        print(music_list)
        os.startfile(os.path.join(music_dir, songs[0]))

#========================== Send Email Function ========================================

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shuklavaibhav336@gmail.com', 'vaibhav1928')
    server.sendmail('shuklavaibhav336@gmail.com', to, content)
    server.close()
