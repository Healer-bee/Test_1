import pyttsx3
import speech_recognition as sr
friday=pyttsx3.init()
voices = friday.getProperty('voices')
rate = friday.getProperty('rate')
friday.setProperty('voice', voices[2].id) 
friday.setProperty('rate', 300)

def speak(audio):
    for i in audio:
        if i in [".",",",";",":"] :
            audio = audio.replace(i, '\n')
    for i in audio.splitlines():
        print(i)
        # friday.say(i)
        # friday.runAndWait()
            
# def command():         
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         if r.pause_threshold ==0.5:
#             audio = r.listen(source)
#         else: audio = r.listen(source,phrase_time_limit=5)
  
#     try:
#         query = r.recognize_google(audio, language ='vi-VN')
#         print(f"Healer: {query}\n")
  
#     except Exception as e:
#         query=""
#         return "None"
     
#     return query
# if __name__  =="__main__":
#  while True:
#         query=command().lower()
#         #All the command will store in lower case for easy recognition
#         #Program 1:--------------------------------------Giao tiếp-----------------------------------------------------------
#         if query=="":
#             print("...")
#         else: 
#             print("I'm here" )

speak("thu hút đầu tư, giảm giá đầu ra nhằm kiểm soát lạm phát. Phương án tổng thể điều hành chính sách tài khóa được yêu cầu báo cáo Thủ tướng trước ngày 15/4.")