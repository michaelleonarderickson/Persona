Project Viddorah aims to create a turnkey solution for Deepfakes to be harnessed ethically.

Here is the adjusted `README.md` file to include the OpenCV environment setup and video processing script:
The following README file is for a Frame Extractor.

# Frame Extractor
This repository contains scripts for extracting frames from a video file, preprocessing them (resize, convert to grayscale), saving them as image files, and a script for setting up the OpenCV environment and testing video processing by reading a video file and displaying its frames.

## Requirements
- Python 3.6 or higher
- pip 19.0 or higher
- OpenCV (cv2)

## Installation
Make sure you have Python and pip installed on your machine.

Install OpenCV by running the following command:

pip install opencv-python

## Usage
### Frame Extraction and Preprocessing
Edit the `extract_frames.pyw` script to specify the video file you want to extract frames from, the output directory where the frames will be saved, and the frame rate at which you want to extract the frames.

For example:

video_path = r'/path/to/directory/for/video.mp4'
output_path = r'/path/to/store/frames'
frame_rate = 10
extract_frames(video_path, output_path, frame_rate)

(Optional) If you want to preprocess the frames (resize, convert to grayscale), edit the `preprocess_frames` function call at the bottom of the `extract_frames.pyw` script.

frame_path = r'/path/to/store/frames/frame_0.png'
output_path = r'/path/to/store/preprocessed/frame_0.png'
resize_dims = (224, 224)
grayscale = True
preprocess_frames(frame_path, output_path, resize_dims, grayscale)

Make sure to adjust the paths and frame rate in the `extract_frames.pyw` script before running it. You can also adjust the `resize_dims` and `grayscale` parameters in the `preprocess_frames` function call to preprocess the frames as desired.

### OpenCV Environment Setup and Video Processing Test
Run the `opencv_environment.pyw` script to set up the OpenCV environment and test video processing. The script will check the OpenCV version, configure GPU support if available, read a video file, resize its frames, and display them in a window. Specify the path to the video file you want to test and the desired dimensions of the displayed frames as a percentage of the screen size in the `opencv_environment.pyw` script.

For example:

video_path = r'/path/to/directory/for/video.mp4'

Run the script, and it will set up the OpenCV environment, then read and display the video frames in a window. Press 'q' to close the video window at any time.

## Support This Project
If you find this project useful and would like to support its development, you can make a donation via

Bitcoin:
3Ba6FM8mVsiAkJwvoSR6KFPdfmd7JEHRMy

Solana:
3caiUBs8vtenHRP75D4xKzPWf6NWpzXe88m6jJFf9MDM

Ethereum on Optimism:
0x15A12D8432d4d0540D9f003Dfe0E0535f549eD77

Contact: viddorah@gmail.com

Your support is greatly appreciated and will help to maintain and improve the project.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

This `README.md` file provides instructions for both the frame extraction and preprocessing script, and the OpenCV environment setup and video processing test script. It includes sections for requirements, installation, usage, support, and license.
