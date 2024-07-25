from moviepy.editor import VideoFileClip, AudioFileClip
from moviepy.audio.fx.all import audio_loop  # Correct import for audio_loop
import os

# Path to the directory containing MP4 files
video_directory = '/home/jasvir/Music/Movie work/Music to titles/'
# Path to the MP3 audio file
audio_file_path = '//home/jasvir/Music/Movie work/Music to titles/1.mp3'
# Directory to save the output files
output_directory = '/home/jasvir/Music/Movie work/Music to titles//output/'

# Check if the audio file exists
if not os.path.isfile(audio_file_path):
    raise FileNotFoundError(f"Audio file not found: {audio_file_path}")

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Load the MP3 audio file
audio_clip = AudioFileClip(audio_file_path)

# Process each MP4 file in the video directory
for file_name in os.listdir(video_directory):
    if file_name.endswith('.mp4'):
        video_file_path = os.path.join(video_directory, file_name)
        print(f"Processing video: {video_file_path}")

        try:
            # Load the video clip
            video_clip = VideoFileClip(video_file_path)

            # Optionally adjust the length of the audio to match the video
            audio_clip_looped = audio_clip.fx(audio_loop, duration=video_clip.duration)

            # Set audio to the video
            final_clip = video_clip.set_audio(audio_clip_looped)

            # Define the output file path
            output_file_path = os.path.join(output_directory, file_name)

            # Write the result to a file
            final_clip.write_videofile(output_file_path, codec='libx264', audio_codec='aac')

            print(f"Video with added audio saved successfully: {output_file_path}")

        except Exception as e:
            print(f"Error processing {file_name}: {e}")
