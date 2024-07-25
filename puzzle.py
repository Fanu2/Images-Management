from moviepy.editor import VideoFileClip, ImageSequenceClip, AudioFileClip, CompositeVideoClip, concatenate_videoclips
from PIL import Image
import os


def main():
    # Paths
    bg_video_path = '/home/jasvir/Music/Movie work/Movie with background layer/1.mp4'
    audio_path = '/home/jasvir/Music/Movie work/Movie with background layer/1.mp3'

    # Prompt user for input
    images_dir = input("Enter the path to the directory containing resized images: ")
    output_path = os.path.join(images_dir, "output.mp4")

    # Load the background video
    bg_video = VideoFileClip(bg_video_path)

    # Load the audio
    audio = AudioFileClip(audio_path)

    # Define maximum duration
    max_duration = 5 * 60  # 5 minutes in seconds

    # Trim the audio to the maximum duration if needed
    audio_duration = min(max_duration, audio.duration)
    audio = audio.subclip(0, audio_duration)

    # Trim the background video to match the audio duration
    bg_video = bg_video.subclip(0, audio_duration)

    # Get image files from the directory
    image_files = [os.path.join(images_dir, img) for img in os.listdir(images_dir) if
                   img.endswith(('.png', '.jpg', '.jpeg'))]

    # Sort image files to maintain order
    image_files.sort()

    # Calculate the duration each image should be displayed
    num_images = len(image_files)
    if num_images == 0:
        raise ValueError("No images found in the specified directory.")

    image_duration = audio_duration / num_images

    # Create a video clip for each image with the calculated duration
    image_clips = []
    for img_path in image_files:
        img_clip = ImageSequenceClip([img_path], fps=24).set_duration(image_duration)
        image_clips.append(img_clip)

    # Concatenate the image clips to form the final image sequence
    images_clip = concatenate_videoclips(image_clips)

    # Set the size of the images to match the background video
    images_clip = images_clip.resize(newsize=bg_video.size)

    # Create a composite video clip with the background video and image video
    final_video = CompositeVideoClip([bg_video, images_clip])

    # Set the audio to the final video
    final_video = final_video.set_audio(audio).set_duration(audio_duration)

    # Write the output video file
    final_video.write_videofile(output_path, codec='libx264', audio_codec='aac')

    print(f"Video saved to {output_path}")


if __name__ == "__main__":
    main()
