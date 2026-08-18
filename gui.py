import tkinter as tk
import os
from player import play, pause, resume, stop , insert

folder = r"A:\Music Player\music"
valid_extensions = (".mp3", ".wav")

window = tk.Tk()
window.title("Music Player")
window.geometry("400x300")

icon = tk.PhotoImage(file="image.png")
window.iconphoto(True,icon)

window.config(bg="#3b403d")

side_bar = tk.Frame(window,background="#808584" , width=150 , bd = 5 , relief="raised")
side_bar.pack(side="left" , fill="y", )

songs = [
    f for f in os.listdir(folder)
    if f.endswith(valid_extensions)
]

for song in songs:

    song_button = tk.Button(
        side_bar,
        text=song,
        bg="#111111",
        fg="white",
        anchor="w",
        relief="flat",
        command=lambda song = song: (insert(folder , song) , play() )
    )

    song_button.pack(
        fill="x",
        padx=10,
        pady=10
    )

scrollbar = tk.Scrollbar(side_bar)
scrollbar.pack(side=tk.RIGHT , fill="y")
play_button = tk.Button(
    window,
    text="Play",
    command=lambda: (insert(folder, "justice.mp3") , play())
)
play_button.pack()

pause_button = tk.Button(
    window,
    text="Pause",
    command=pause
)
pause_button.pack()

resume_button = tk.Button(
    window,
    text="Resume",
    command=resume
)
resume_button.pack()

stop_button = tk.Button(
    window,
    text="Stop",
    command=stop
)
stop_button.pack()



window.mainloop()