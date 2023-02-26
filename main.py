# -*- coding: utf-8 -*-
import speech_recognition as sr # recognise speech
import playsound # to play an audio file
from gtts import gTTS # google text to speech
import random
import os
import time
from sys import exit
from time import ctime
import webbrowser
import pyttsx3

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True
        
r = sr.Recognizer() # initialise a recogniser





def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ""

        try:
            voice_data = r.recognize_google(audio,language='th')
            print(voice_data)
        except sr.UnknownValueError: # error: recognizer does not understand
            print('Error')
        except sr.RequestError:
            print('Sorry, the service is down')# error: recognizer is not connected
        print(f">> {voice_data.lower()}") # print what user said
        return voice_data.lower()

    
    

def speak(audio_string):
    engine = pyttsx3.init()
    TH_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_thTH_Pattara"
    engine.setProperty('volume', 0.9)  # Volume 0-1e
    engine.setProperty('rate', 125)  #148
    engine.setProperty('voice', TH_voice_id)
    engine.say(audio_string)
    engine.runAndWait()
 
def respond(voice_data):
    if there_exists(['ว่าไง','ไง','สวัสดี']):
        greetings = ["สวัสดีครับผม มีอะไรให้ผมช่วยมั้ยครับ", "มีอะไรให้ผมช่วยมั้ยครับ", "สวัสดีครับ วันนี้เป็นยังไงบ้างครับ", "ให้ช่วยอะไรไหมครับ", "มีอะไรรึเปล่าครับ"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        speak(greet)
        
    if there_exists(['ชื่ออะไร','คุณเป็นใคร','คุณคือใคร']):
        speak('สวัสดีครับ ผมชื่อมาโนชครับ')
    
    #เปิดเพลงใน youtube
    if there_exists(['เปิดเพลง']):
        search_term = voice_data.split("เพลง")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak(f'นี่ครับ {search_term} ในยูทุป')
    
    #search google
    if there_exists(["ค้นหา"]) and 'เพลง' not in voice_data:
        search_term = voice_data.split("หา")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'นี่ครับ {search_term} ในกูเกิ้ล')
    
    #stock plan
    if there_exists(["หุ้น",'วางแผนหุ้น']):
        url = "https://th.tradingview.com/"
        webbrowser.get().open(url)
        speak('พร้อมแล้วครับผม')
    
    if there_exists(["รายงานสภาพอากาศ"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        speak("นี่ครับผม")
     

        
    if there_exists(['กี่โมงแล้ว','ตอนนี้กี่โมง','กี่โมง','วันนี้วันอะไร','วันที่เท่าไร']):
        speak(ctime())

    if there_exists(["ปิดโปรแกรม", "ออก", "ปิดระบบ"]):
        speak("กำลังปิดระบบครับผม")
        exit()
        
        
time.sleep(1)
speak("สวัสดีครับผม มีอะไรให้ผมช่วยมั้ยครับ")

wake='มาโนช'
while(1):
    print('listen...')
    voice_data = get_audio() # get the voice input
    respond(voice_data) # respond
'''    if voice_data.count(wake) > 0:
        print('listen...')
        speak("ว่ามาเลยครับผม")
        voice_data = get_audio()
        respond(voice_data) # respond'''



