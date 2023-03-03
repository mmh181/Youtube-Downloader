import tkinter
import customtkinter
from pytube import YouTube


def start_download():
    try:
        yt_link = link.get()
        yt_object = YouTube(yt_link, on_progress_callback=on_progress)
        video = yt_object.streams.get_highest_resolution()
        title.configure(text=yt_object.title, text_color="white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded!")
        print("try block executed")
    except:
        finishLabel.configure(text="Download Error", text_color="red")
        print("except block executed")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.file_size
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    # update progress bar

    progressBar.set(float(percentage_of_completion) / 100)


# System settings


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame

app = customtkinter.CTk()  # top-level widget
app.geometry("720x480")  # screen size
app.title("Youtube Downloader")  # title

# Adding UI elements

title = customtkinter.CTkLabel(app, text="Input a YouTube link")
title.pack(padx=10, pady=10)  # pack is a layout manager that positions widgets in an app frame.

# text input for link
url_var = tkinter.StringVar()  # collects input from link by being called in link.
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished downloading

finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Progress percentage

pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download button

download = customtkinter.CTkButton(app, text="Download", command=start_download)
download.pack(padx=10, pady=10)

# loop the app so window stays open

app.mainloop()  # tells python to run the tkinter event as a loop.

# Define a start download function
