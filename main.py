import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import time

def main(sound):
    try:
        pygame.mixer.init()
        sound_obj = pygame.mixer.Sound(sound)
        sound_obj.play()
        
        
        duration = sound_obj.get_length()
        time.sleep(duration)
        


    except Exception as e:
        print("Audio initialization failed!")
        return
    

if __name__ == "__main__":

        folder = r"A:\Music Player using python\music"
        if not os.path.isdir(folder):
            print("the folder did not exist") 
        else:
            while True:
                try:
                    songs = "\n".join(os.listdir(folder))
                    if songs == "":
                        print("No files in the music folder")
                        break
                    
                    print(f"songs:\n---------------------------\n{songs}\n---------------------------")
                    choice = input("\nEnter the song you want to play: ")

                    with open(rf"{folder}\{choice}.mp3") as sound:
                        main(rf"{folder}\{choice}.mp3")                        

                except FileNotFoundError as e:
                    print("\nEnter a valid song\n")
                except OSError as o:
                    print("")
                