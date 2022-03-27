from yt_dlp import YoutubeDL

ydl_opts = {'format': 'bestaudio',
            'outtmpl': './Downloads/%(title)s.%(ext)s'}

while (True):
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(input("Input a video URL: "))
        print("Done!\n")
