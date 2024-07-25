import cv2
import numpy as np
import os
from moviepy.editor import VideoFileClip, AudioFileClip

# Paths
image_directory = '/home/jasvir/Music/Movie work/video/'
audio_file_path = '/home/jasvir/Music/Movie work/video/1.mp3'
output_video_path = '/home/jasvir/Music/Movie work/video/output_video.mp4'

# Cartoonize function
def cartoonize_image(image_path):
    # Read image
    img = cv2.imread(image_path)
    # Resize for consistency
    img = cv2.resize(img, (640, 480))

    # Apply cartoon effect
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255,
                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 9, 10)
    color = cv2.bilateralFilter(img, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon

# Create a list of cartoonized images
cartoon_images = []
for file_name in sorted(os.listdir(image_directory)):
    if file_name.endswith('.jpg') or file_name.endswith('.png'):
        image_path = os.path.join(image_directory, file_name)
        cartoon_image = cartoonize_image(image_path)
        cartoon_image_path = os.path.join(image_directory, 'cartoon_' + file_name)
        cv2.imwrite(cartoon_image_path, cartoon_image)
        cartoon_images.append(cartoon_image_path)

# Create video from images
import moviepy.editor as mp

def create_video_from_images(image_paths, output_path, fps=24):
    clips = [mp.ImageClip(img).set_duration(2) for img in image_paths]
    video = mp.concatenate_videoclips(clips, method="compose")
    video.write_videofile(output_path, fps=fps)

create_video_from_images(cartoon_images, output_video_path)

# Add music to the video
def add_music_to_video(video_path, audio_path, output_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    final_clip = video_clip.set_audio(audio_clip)
    final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

add_music_to_video(output_video_path, audio_file_path, output_video_path)

print(f"Video created and saved as {output_video_path}")
