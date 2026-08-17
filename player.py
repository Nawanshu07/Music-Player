import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import pygame

pygame.mixer.init()


def insert(folder, song):
    file_path = os.path.join(folder, song)
    try:
        pygame.mixer.music.load(file_path)
    except pygame.error as e:
        print(f"Could not load {song}")

def play():
    pygame.mixer.music.play()


def pause():
    pygame.mixer.music.pause()


def resume():
    pygame.mixer.music.unpause()


def stop():
    pygame.mixer.music.stop()