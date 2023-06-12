# Find and Download Music on Youtube
# import libraries

from pytube import YouTube

import os
from sys import argv


from pytube import YouTube

import os
from sys import argv

link = input('Please enter youtube music link:')

yt = YouTube(link)

#filter the video
stream = yt.streams.filter(subtype="mp4").first()


# download the file
out_file = stream.download(output_path=r"C:\Users\Administrator\Desktop")

# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp4'
os.rename(out_file, new_file)

# result of success
print(yt.title + " has been successfully downloaded.")
