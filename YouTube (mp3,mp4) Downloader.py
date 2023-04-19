from pytube import YouTube as yb
import PySimpleGUI as sg
import os


def videos_downloader(link):
    youtube_object = yb(link)
    youtube_object = youtube_object.streams.get_by_resolution("720p")
    
    try:
        youtube_object.download("D:\youtube video installer")
        print("Download compleated Successfully")
    
    except:
        print("an error accured")
    
    

def audio_downloader(link):
    youtube_object = yb(link)
    youtube_object = youtube_object.streams.filter(only_audio=True).get_audio_only()
    try:
        downloaded_file = youtube_object.download("D:\youtube video installer")
        print("Download compleated Successfully")

    finally:
        base, ext = os.path.splitext(downloaded_file)
        new_file = base + '.mp3'
        os.rename(downloaded_file, new_file)


sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('YouTube High Resolution Video Downloader')],
            [sg.Text('Enter ur link '), sg.InputText()],
            [sg.Button('mp3'), sg.Button('mp4')],
            [sg.Button('Cancel')]]
# Create the Window
window = sg.Window('YouTube Video Downloader', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'): # if user closes window or clicks cancel
        break
    if event == "mp4":
        videos_downloader(values[0])
        break

    if event == "mp3":
        audio_downloader(values[0])
        break

window.close()



