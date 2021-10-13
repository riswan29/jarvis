from inspect import cleandoc
from math import trunc
from re import S
from sys import flags
from threading import main_thread
import pyttsx3
import datetime
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import wikipedia
# import smtplib
import webbrowser as wb
from gtts.langs import _main_langs
from wikipedia.wikipedia import search, set_lang

engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 170)


def speak(audio):
    engine = gTTS(audio, lang='id')
    engine.save('sound.mp3')
    playsound('sound.mp3')

# def speak(audio):
#     print("   ")
#     print(f" {audio}")
#     print("   ")
#     engine.say(audio)
#     engine.runAndWait()

# +++++++++++++++++++ WAKTU ++++++++++++++++++++++ #


def time_():
    Time = datetime.datetime.now().strftime("%M")
    t_time = int(Time)
    t_menit = ((t_time - 60)*(-1))
    jam = datetime.datetime.now().strftime("%I")
    t_time = int(jam)
    t_jam = (t_time + 1)
    speak("Sekarang  :")
    menit = datetime.datetime.now().minute
    if menit >= 0 and menit < 40:
        speak(datetime.datetime.now().strftime(
            "pukul %I 'lewat':%M menit"))
    else:
        speak(datetime.datetime.now().strftime(
            f"pukul {t_jam} kurang {t_menit} menit"))


def hari():

    hari = datetime.datetime.now()
    Hari = hari.strftime("%A")

    if Hari == "Monday":
        speak("Sekarang Hari senin")

    elif Hari == "Tuesday":
        speak("Sekarang Hari Selasa")

    elif Hari == "Wednesday":
        speak("Sekarang Hari Rabu")

    elif Hari == "Thursday":
        speak("Sekarang Hari Kamis")

    elif Hari == "Friday":
        speak("Sekarang Hari Jum'at")

    elif Hari == "Saturday":
        speak("Sekarang Hari Sabtu")
    else:
        speak("Sekarang Hari Minggu")


# +++++++++++++++++++ Jadwal ++++++++++++++++++++++ #
def jadwal():
    hari = datetime.datetime.now()
    Hari = hari.strftime("%A")

    senin = ['1.Kuliah kelas Komputer Grafik, 4 sks mulai jam 1 siang sampai 4 sore',
             '2.kelas online paithon dikoding ',
             '3.menambah fitur saya agar lebih bagus lagi',
             '4.main game']
    selasa =['1.kuliah kelas Keamanan komputer dan jaringan ,  3 sks mulai dari jam setengah 10 sampai jam 12 siang',
             '2.kelas rekayasa perangkat lunak , 3 sks mulai dari jam 1 siang sampai jam setengah 4 sore',
             '3.kelas online paithon dikoding',
             '4.menambah fitur saya agar lebih bagus lagi',
             '5.Main game']
    rabu = ['1.kuliah kelas sistem oprasi , 3 sks mulai jam 1 siang sampai jam setengah 4 sore',
            '2.kelas online paithon dikoding',
            '3.menambah fitur saya agar lebih bagus lagi',
            '4.Main game']
    kamis = ['1.kuliah kelas sistem informasi , 3 sks mulai jam 10 pagi sampai jam 1 siang',
             '2.Kelas online paithon dikoding',
             '3.menambah fitur saya agar lebih bagus lagi',
             '4.main game']
    jumat = ['1.Kelas online paithon dikoding',
             '2.menambah fitur saya agar lebih bagus lagi',
             '3.main game']
    sabtu = ['1.kuliah kelas kecerdasan buatan , 4 sks mulai jam 8 pagi sampai jam 12 siang',
             '2.Kelas online paithon dikoding',
             '3.menambah fitur saya agar lebih bagus lagi',
             '4.main game']


    if Hari == "Monday":
        speak(f"Jadwal anda sekarang adalah{senin}")

    elif Hari == "Tuesday":
        speak(f"Jadwal anda sekarang adalah{selasa}")

    elif Hari == "Wednesday":
        speak(f"Jadwal anda sekarang adalah{rabu}")

    elif Hari == "Thursday":
        speak(f"Jadwal anda sekarang adalah{kamis}")

    elif Hari == "Friday":
        speak(f"Jadwal anda sekarang adalah{jumat}")

    elif Hari == "Saturday":
        speak(f"Jadwal anda sekarang adalah{sabtu}")
    else:
        speak(f"Jadwal anda sekarang adalah{senin}")


# +++++++++++++++++++ KENDALI ++++++++++++++++++++++ #
def wishme():
    hari()
    speak("Halo Riswan !")
    time_()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Selamat pagi Riswan")
    elif hour >= 12 and hour < 18:
        speak("Selamat siang Riswan")
    elif hour >= 18 and hour < 24:
        speak("selamat Malam Riswan")
    else:
        speak("selamat malam menjelang pagi Riswan")

    speak("Moli assistand akan selalu aktif untuk anda . ada yang bisa saya bantu hari ini?")

# +++++++++++++++++++ Jadwal ++++++++++++++++++++++ #

# +++++++++++++++++++ PERINTAH ++++++++++++++++++++++ #


def perintah():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Mendengar....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Mengenali....")
        query = r.recognize_google(audio, language="id-ID")
        print(query)

    except Exception as e:
        print(e)
        print("Tolong ucapkan sekali lagi")
        return "None"
    return query

# +++++++++++++++++++ EMAIL ++++++++++++++++++++++ #
# def sendEmail(to,content):
#     server = smtplib.SMTP('smtp.gmailcom',587)
#     server.ehlo()
#     server.starttls()

#     server.login('username@gmail.com','password')
#     server.sendmail('username@gmail.com',to,content)
#     server.close()


if __name__ == "__main__":

    wishme()

    while True:

        query = perintah().lower()

        if 'jam' in query:
            time_()

        elif 'wikipedia' in query:
            speak("mencari...")
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=3)
            speak('mencari di wikipedia')
            print(result)
            speak(result)

        # elif 'send email' in query:
        #     try:
        #         speak("what should i say")
        #         content = perintah()

        #         speak('who is the reciever')
        #         reciever = input("Enter reciever's email:")
        #         to = reciever
        #         sendEmail(to,content)
        #         speak(content)
        #         speak('email has been send')

        #     except Exception as e:
        #         print(e)
        #         speak('Unable to send email.')


# +++++++++++++++++++ OPEN WEB ++++++++++++++++++++++ #
        elif 'browser' in query:
            speak('anda ingin saya mencari apa ? ')
            chromepath = '/usr/bin/google-chrome-stable %s'
            
            search = perintah().lower()
            wb.get(chromepath).open_new_tab(search + '.com')

# +++++++++++++++++++ SEARCH YT ++++++++++++++++++++++ #
        elif 'youtube' in query:
            speak('Tuan apa yang ingin anda lihat sekarang ?')
            search_term = perintah().lower()
            speak("saya akan mencari ke youtube sekarang tuan!")
            wb.open('https://www.youtube.com/results?search_query='+search_term)

        elif "jadwal" in query:
            jadwal()
        
        elif "kelas" in query:
            speak("riswan kamu sudah sampai di kelas django paithon dan flask ")
                
                
        elif "angel" in query:
            
            speak("enjel kamu terlalu polos atau gimana sih ?")
                
                
                
                
                 