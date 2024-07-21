from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT']='1'
import pygame, sys
from time import sleep
import time

pygame.mixer.init()
print("Mine all Mine...")

pygame.mixer.music.load('my_love_mine_all_mine.mp3')

pygame.mixer.music.play()
    
def play():
    lyrics = [
        ("Moon, tell me if I could", 0.18),
        ("Send up my heart to you?", 0.12),
        ("So, when I die", 0.12),
        ("which I must do",0.12),
        ("Could it shine down here with you?",0.125),
        ("Cause my love is mine, all mine", 0.11),
        ("I love mine, mine, mine", 0.165),   
        ("Nothing in the world belongs to me",0.13),
        ("But my love is mine, all mine, all mine",0.12),                
            
    ]

                        
    delays = [0.4, 0.5, 0.42,0.23, 0.6,0.72, 0.05, 0.28,0.045]
    
    for i, (line, charDelay) in enumerate(lyrics):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(charDelay)
        time.sleep(delays[i])
        print('')

play()     