import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import time

pygame.mixer.init()
def play(folder , song):
    try:
        file_path = os.path.join(folder, song)
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
               
        print(f"Now playing {song}")
        


    except Exception as e:
        print(f"Playback failed {e}")
        return
    
if __name__ == "__main__":

        folder = r"A:\Music Player\music"
        if not os.path.isdir(folder):
            print("the folder did not exist") 
        else:
            while True:
                try:
                    songs = os.listdir(folder)
 
                    if songs == []:
                        print("No files in the music folder")
                        break
                    
                    print("---------SONGS---------")
                    for index , song in enumerate(songs , start=1):
                        print(f"{index}. {song}")
                    print("-----------------------")

                    choice_input = input("Enter the song number (or 'Q' to quit): ").strip()

                    if choice_input.lower() == "q":
                        break

                    try:
                        choice = int(choice_input) - 1
                    except ValueError:
                        print("Please enter a song number or Q to quit.\n")
                        continue
                    
                    if 0 <= choice < len(songs):
                        play(folder,songs[choice])
                        time.sleep(0.1)
                        playing = True
                        while playing:
                            print("Commands: [P]ause , [R]esume , [S]top")
                            command = input("Enter the command: ").lower()

                            if command == "p":
                                pygame.mixer.music.pause()
                            elif command == "r":
                                pygame.mixer.music.unpause()
                            elif command == "s":
                                pygame.mixer.music.stop()
                                playing = False
                            else:
                                print("Enter a valid command")

                    else:
                        print("Invalid choice\n")
                    
                                            

                except FileNotFoundError as e:
                    print("\nEnter a valid song\n")
                except OSError as o:
                    print("")