import youtube_dl

link = input('Please enter YouTube music link: ')

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': r"C:\Users\Administrator\Desktop\%(title)s.%(ext)s",
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(link, download=True)
    video_title = info_dict.get('title', None)
    if video_title is not None:
        print(f"{video_title} has been successfully downloaded.")

