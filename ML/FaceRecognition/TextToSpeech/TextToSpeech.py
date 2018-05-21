#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def getTextToMp3(str, language):
    from gtts import gTTS
    tts = gTTS(text=str, lang=language)
    try:
        tts.save("voice.mp3")
    except:
        pass

def saySomthing(str, language):
    import pygame
    getTextToMp3(str, language)
    pygame.mixer.init()
    pygame.mixer.music.load("./voice.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    pygame.mixer.stop()
    pygame.mixer.quit()
    del pygame
