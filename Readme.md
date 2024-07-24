
Python Scripts for Video Management
Description
This project contains Python scripts for creating and managing video content. The scripts include functionalities such as trimming videos, adding watermarks, merging clips, and converting formats. These tools are especially useful for creating YouTube Shorts and other short video formats from existing videos.

Features
Trim videos to specific lengths.
Add watermarks or text overlays.
Merge multiple video clips.
Convert video formats (e.g., MP4 to AVI).
Extract audio from videos.
Create YouTube Shorts from existing videos.
Requirements
Python 3.x
moviepy
opencv-python
ffmpeg
Install the dependencies using:

bash
Copy code
pip install moviepy opencv-python ffmpeg-python
Usage
Trimming a Video
Trim a video to a specified start and end time.

python
Copy code
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

input_video = "input.mp4"
start_time = 30  # in seconds
end_time = 60  # in seconds
output_video = "output_trimmed.mp4"

ffmpeg_extract_subclip(input_video, start_time, end_time, targetname=output_video)
Adding a Watermark
Add a watermark to a video.

python
Copy code
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

video = VideoFileClip("input.mp4")
watermark = TextClip("Watermark", fontsize=24, color='white').set_position(("right", "bottom")).set_duration(video.duration)
final = CompositeVideoClip([video, watermark])
final.write_videofile("output_watermarked.mp4")
Merging Video Clips
Merge multiple video clips into one.

python
Copy code
from moviepy.editor import concatenate_videoclips

clip1 = VideoFileClip("clip1.mp4")
clip2 = VideoFileClip("clip2.mp4")
final_clip = concatenate_videoclips([clip1, clip2])
final_clip.write_videofile("output_merged.mp4")
Scripts Explanation
trim_video.py
This script trims a video to a specified start and end time.

Arguments:
input_video: Path to the input video file.
start_time: Start time in seconds.
end_time: End time in seconds.
output_video: Path to the output video file.
add_watermark.py
This script adds a watermark to the video.

Arguments:
input_video: Path to the input video file.
watermark_text: Text to be used as a watermark.
output_video: Path to the output video file.
merge_clips.py
This script merges multiple video clips into one.

Arguments:
clip1: Path to the first video clip.
clip2: Path to the second video clip.
output_video: Path to the output video file.
Examples
To trim a video from 30 to 60 seconds:

bash
Copy code
python trim_video.py input.mp4 30 60 output_trimmed.mp4
To add a watermark to a video:

bash
Copy code
python add_watermark.py input.mp4 "Watermark" output_watermarked.mp4
To merge two video clips:

bash
Copy code
python merge_clips.py clip1.mp4 clip2.mp4 output_merged.mp4
Contributing
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -m 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.
License
This project is licensed under the MIT License - see the LICENSE file for details.
