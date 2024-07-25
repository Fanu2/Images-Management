from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

# Path to the directory containing MP4 files
directory_path = '/home/jasvir/Music/Movie work/Concatenate/'

# List all MP4 files in the directory
mp4_files = [f for f in os.listdir(directory_path) if f.endswith('.mp4')]

# Sort files if needed (e.g., by name)
mp4_files.sort()

# Create a list to hold video clips
clips = []

for file_name in mp4_files:
    file_path = os.path.join(directory_path, file_name)
    print(f"Loading video: {file_path}")
    clip = VideoFileClip(file_path)
    clips.append(clip)

# Concatenate all video clips
final_clip = concatenate_videoclips(clips, method="compose")

# Path for the output file
output_file_path = '/home/jasvir/Music/Movie work/Concatenate/concatenated_video.mp4'

# Write the result to a file
final_clip.write_videofile(output_file_path, codec='libx264', audio_codec='aac')

print(f"Concatenated video created successfully: {output_file_path}")
