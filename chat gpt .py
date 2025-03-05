import speech_recognition as sr
import requests
import pyperclip
import pyautogui
import time

pyautogui.click(x=360, y=360)
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('delete')
r=sr.Recognizer()
while True:
      try:
         with sr.Microphone() as mic:
               print('sey')
               add=r.listen(mic)
               text=r.recognize_google(add,language='fa-IR')

               if text:
                mo=requests.get(f"http://5.161.91.18/chat?text={text}")
                print(text)
                print(mo.json()) 
                pyautogui.click(x=360, y=360)
                pyautogui.hotkey('ctrl', 'a') 
                pyperclip.copy(mo.json())
                time.sleep(0.5)
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(0.5)
                pyautogui.click(x=360, y=450)
                time.sleep(11)
                pyautogui.click(x=26, y=600)


      except Exception as e:
         r=sr.Recognizer()
         continue

print(mo.json())