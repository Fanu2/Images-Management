import moviepy.editor as mp
from moviepy.config import IMAGEMAGICK_BINARY

# Disable ImageMagick
IMAGEMAGICK_BINARY = None

# Define paths
video_path = "/home/jasvir/Music/Movie work/Trailer/1.mp4"
audio_path = "/home/jasvir/Music/Movie work/Trailer/1.mp3"
output_path = "/home/jasvir/Music/Movie work/Trailer/output_trailer.mp4"

# Load video and audio
video = mp.VideoFileClip(video_path)
audio = mp.AudioFileClip(audio_path)

# Create a title clip
title = mp.TextClip("Movie Title\nThe Ultimate Trailer", fontsize=70, color='white', bg_color='black', size=video.size)
title = title.set_duration(5).set_position('center')

# Concatenate video and title
final_clip = mp.concatenate_videoclips([title, video])

# Set audio and write final video
final_clip = final_clip.set_audio(audio)
final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
