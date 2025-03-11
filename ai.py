import cv2
import pytesseract
import speech_recognition as sr
import json
import pyttsx3
import numpy as np
from googletrans import Translator
import os
import tradingview_ta
import pandas as pd
import requests
from tradingview_ta import TA_Handler, Interval, Exchange

# Tesseract OCR yo‘li (Windows uchun)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Xotira fayli
XOTIRA_FAYL = "dars_xotira.json"
translator = Translator()
engine = pyttsx3.init()

# ======== 1. OVOZ ORQALI BUYRUQLARNI ANIQLASH ======== #
def ovoz_buyruq_ol():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("[INFO] Buyruq ayting...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            text = recognizer.recognize_google(audio, language="uz-UZ")
            print("[Ovozdan]:", text)
            return text.lower()
        except sr.UnknownValueError:
            print("[XATO] Buyruq tushunilmadi.")
            return ""
        except sr.RequestError:
            print("[XATO] Google xizmatida muammo bor.")
            return ""

# ======== 2. BUYRUQLARNI BAJARISH ======== #
def ovoz_boshqaruv():
    while True:
        buyruq = ovoz_buyruq_ol()

        if "video yoz" in buyruq:
            video_yozish()
        
        elif "video matn" in buyruq:
            video_matn_oqish()

        elif "ovozni matn" in buyruq:
            ovoz_matn()

        elif "tarjima qil" in buyruq:
            matn = ovoz_buyruq_ol()
            tarjima = matn_tarjima(matn, "en")
            print("[Tarjima]:", tarjima)
        
        elif "tradingview" in buyruq:
            tradingview_malumot()
        
        elif "bilim kuchaytir" in buyruq:
            bilim_kuchaytirish()

        elif "stop" in buyruq or "to‘xta" in buyruq:
            print("[INFO] Dastur to‘xtatildi.")
            engine.say("Dastur to‘xtatildi.")
            engine.runAndWait()
            break

        else:
            print("[INFO] Noma'lum buyruq.")
            engine.say("Bu buyruqni tushunmadim.")
            engine.runAndWait()

# ======== 3. KAMERA ORQALI VIDEO YARATISH ======== #
def video_yozish(output_file="video_dars.avi"):
    cap = cv2.VideoCapture(0)  
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (640, 480))

    print("[INFO] Video yozilmoqda. Tugatish uchun 'q' bosing.")
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("[INFO] Video yozish tugadi.")

# ======== 4. VIDEO MATNLARNI TANIB OLISh ======== #
def video_matn_oqish(video_file="video_dars.avi"):
    cap = cv2.VideoCapture(video_file)
    matnlar = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray, config="--oem 3 --psm 6")
        if text.strip():
            matnlar.append(text.strip())
            print("[TEXT]:", text)

        cv2.imshow("Video", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return " ".join(matnlar)

# ======== 5. TARJIMA QILISH ======== #
def matn_tarjima(matn, til="en"):
    tarjima = translator.translate(matn, dest=til)
    print(f"[TARJIMA ({til})]: {tarjima.text}")
    return tarjima.text

# ======== 6. TRADINGVIEW MA'LUMOTLARINI OLISh ======== #
def tradingview_malumot(kriptovalyuta="BTCUSDT"):
    analiz = TA_Handler(
        symbol=kriptovalyuta,
        screener="crypto",
        exchange="BINANCE",
        interval=Interval.INTERVAL_1_HOUR
    )

    natija = analiz.get_analysis().summary
    print(f"[TradingView Tavsiyasi]: {json.dumps(natija, indent=4)}")

    return natija

# ======== 7. SAQLANGAN BILIMNI KUCHAYTIRISH ======== #
def bilim_kuchaytirish():
    try:
        with open(XOTIRA_FAYL, "r") as file:
            dars_xotira = json.load(file)
        
        yangi_matn = dars_xotira["matn"] + " Yangi bilimlar qo‘shildi!"
        yangi_tarjima = dars_xotira["tarjima"] + " New knowledge has been added!"
        xotira_saqlash(dars_xotira["dars_nomi"], yangi_matn, yangi_tarjima)
        print("[INFO] Bilimlar kuchaytirildi!")
    except FileNotFoundError:
        print("[XATO] Xotira fayli topilmadi!")

# ======== 8. BARCHA BOSQICHLARNI ISHLATISH ======== #
if __name__ == "__main__":
    print("[INFO] Sun'iy qo'l ovoz orqali boshqarishga tayyor.")
    engine.say("Salom, men tayyorman! Buyruq bering.")
    engine.runAndWait()
    ovoz_boshqaruv()
