import tkinter
import customtkinter
from pytube import YouTube

# DEF 
def start_download():
    try:
        yt_url = link.get()
        yt_object = YouTube(yt_url, on_progress_callback=on_progress)
        title.configure(text=yt_object.title)
        video = yt_object.streams.get_highest_resolution()
        video.download()
        finished_downloading.configure(text="Downloaded!", text_color="green")

    except:
        finished_downloading.configure(text="Something went wrong! Could be a invalid link!", text_color="red")
        print('YT Download error')
    
    # print("Downloaded!")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent_of_completion = bytes_downloaded / total_size * 100
    percent_str = str(int(percent_of_completion))
    p_percent.configure(text=percent_str + "%")
    p_percent.update()

    p_bar.set(float(percent_of_completion) / 100)

# SYSTEM SETTINGS
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# APP FRAME
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# ADDING UIs
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

yt_url = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=yt_url)
link.pack()

download_button = customtkinter.CTkButton(app, text="Download", command=start_download)
download_button.pack(padx=10, pady=10)

# PROGRESS

p_percent = customtkinter.CTkLabel(app, text="0%")
p_percent.pack()
p_bar = customtkinter.CTkProgressBar(app, width=400)
p_bar.set(0)
p_bar.pack()

# FINISHED LABEL
finished_downloading = customtkinter.CTkLabel(app, text="")
finished_downloading.pack()

# RUN APP
app.mainloop()