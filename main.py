import customtkinter as ctk
from tkinter import ttk
from pytube import YouTube

def startDownload():
    try:
        ytLink = entry_url.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="white")
        finishlabel.configure(text="")
        video.download()
        finishlabel.configure(text="Downloaded!")
    except Exception as e:
        finishlabel.configure(text=f"Download Error: {str(e)}", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completeion = bytes_downloaded/total_size * 100
    print(percentage_of_completeion)
    

# create a root window
root = ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# title window
root.title("YouTube Downloader")

# set min and max dimensions
root.geometry("720x480")
root.minsize(720, 480)
root.maxsize(1080, 720)

# create frame
content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

# create label
url_label = ctk.CTkLabel(content_frame, text="Enter a YouTube link")
url_label.pack(pady=("10p", "5p"))
entry_url = ctk.CTkEntry(content_frame, width=400, height=40)
entry_url.pack(pady=("10p", "5p"))

# download button
download_button = ctk.CTkButton(content_frame, text="Download", command=startDownload)
download_button.pack(pady=("10p", "5p"))

# status
title = ctk.CTkLabel(content_frame, text="", text_color="white")
title.pack(pady=("10p", "5p"))
finishlabel = ctk.CTkLabel(content_frame, text="")
finishlabel.pack(pady=("10p", "5p"))

# start app
root.mainloop()