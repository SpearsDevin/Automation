import tkinter as tk
import subprocess
import webbrowser

def button1_clicked():
    subprocess.Popen("C:/Users/%UserProfile%/AppData/Local/Programs/Microsoft VS Code/Code.exe")
    subprocess.Popen("C:/Users/%UserProfile%/AppData/Local/Discord/Update.exe --processStart Discord.exe")
    subprocess.Popen("C:/Users/%UserProfile%/AppData/Roaming/Spotify/Spotify.exe")
    webbrowser.open("https://dev.to/")
    webbrowser.open("https://stackoverflow.com/")
def button2_clicked():
    subprocess.Popen("C:/Users/%UserProfile%/AppData/Local/Discord/Update.exe --processStart Discord.exe")
    subprocess.Popen("C:/Users/%UserProfile%/AppData/Roaming/Spotify/Spotify.exe")
    webbrowser.open("https://www.owlbear.rodeo/game/tvl-EDmdF")
    webbrowser.open("https://www.dndbeyond.com/characters/63633483")

def button3_clicked():
    print("Button 3 clicked")

def button4_clicked():
    print("Button 4 clicked")

root = tk.Tk()
root.title("My GUI")
root.config(bg='black') # set background color to light blue
#root.geometry("400x400") # set the dimensions of the window
root.iconbitmap( "")


button1 = tk.Button(root, text="Programming Apps",height=5, width=20, bd=0, command=button1_clicked, bg='white') # set the background color of the button
button1.grid(row=0, column=0, padx=10, pady=10)

button2 = tk.Button(root, text="DND",height=5, width=20,bd=0, command=button2_clicked, bg='red') # set the background color of the button
button2.grid(row=0, column=1, padx=10, pady=10)

#button3 = tk.Button(root, text="",height=5, width=20, bd=0, command=button3_clicked, bg='white') # set the background color of the button
#button3.grid(row=1, column=0, padx=10, pady=10)

#button4 = tk.Button(root, text="",height=5, width=20,bd=0, command=button4_clicked, bg='white') # set the background color of the button
#button4.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()
