from moviepy.editor import VideoFileClip, AudioFileClip, ImageClip, CompositeVideoClip
from moviepy.video.fx import resize

# Paths to the files
image_or_video_path = '//home/jasvir/Music/Movie work/movie/12.mp4'  # Use an image or video
audio_file_path = '/home/jasvir/Music/Movie work/movie/tappe.mp3'
output_file_path = '/home/jasvir/Music/Movie work/movie/animated_music_video1.mp4'

# Load the base video or create a video from an image
if image_or_video_path.endswith(('.png', '.jpg', '.jpeg')):
    # Create a video from an image
    base_clip = ImageClip(image_or_video_path, duration=20)  # Duration in seconds
    base_clip = base_clip.set_duration(10).resize(height=720)  # Resize to fit video dimensions
else:
    # Load video
    base_clip = VideoFileClip(image_or_video_path).subclip(0, 10)  # Trim to 10 seconds

# Load the audio file
audio_clip = AudioFileClip(audio_file_path).subclip(0, 10)  # Trim to match video duration

# Set audio to the video
base_clip = base_clip.set_audio(audio_clip)

# Output the final video
base_clip.write_videofile(output_file_path, codec='libx264', audio_codec='aac')

print(f"Animated music video created successfully: {output_file_path}")
