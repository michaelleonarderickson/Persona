import cv2
import os

def extract_frames(video_path, output_path, frame_rate=30):

    # Open the video file
    video = cv2.VideoCapture(video_path)

    # Check if video opened successfully
    if not avideo.isOpened():
        print("Error: Could not open video file.")
        return

    # Frame count
    frame_count = 0

    while True:
        ret, frame = video.read()

        # Break the loop if the video is ended
        if not ret:
            break

        # Save frame at specified rate
        if frame_count % frame_rate == 0:
            frame_path = f"{output_path}/frame_{frame_count}.png"
            cv2.imwrite(frame_path, frame)
            print(f"Saved {frame_path}")

        frame_count += 1

    # Release the video object and close windows
    video.release()
    cv2.destroyAllWindows()
    print("Frame extraction completed.")

# Call extract_frames function
video_path = r'/path/to/directory/for/video.mp4' # PATH TO THE VIDEO THAT NEEDS FRAME(S) EXTRACTED
output_path = r'/path/to/store/frames' # PATH TO STORE FRAME(S)
frame_rate = 10 # ADJUST THIS TO CHOOSE HOW MANY FRAMES ARE CREATED PER SECOND | USE THE VIDEO FRAME RATE OVER THIS NUMBER
extract_frames(video_path, output_path, frame_rate)

# Choose to run the function below if you want to resize the extracted frames and/or make grayscale or you may delete if preprocessing is not necessary
def preprocess_frames(frame_path, output_path, resize_dims=(224, 224), grayscale=True):

    # Read the frame
    frame = cv2.imread(frame_path)

    # Resize the frame
    frame_resized = cv2.resize(frame, resize_dims)

    # Convert to grayscale if required
    if grayscale:
        frame_resized = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)

    # Save the preprocessed frame
    cv2.imwrite(output_path, frame_resized)
    print(f"Preprocessed and saved frame at {output_path}")

# Call preprocess_frames function for each extracted frame
frame_path = r'/path/to/store/frames/frame_0.png' # ADJUST THIS TO MATCH output_path/frame_0.png
output_path = r'/path/to/store/preprocessed/frame_0.png' # PATH TO STORE THE PREPROCESSED FRAME(S)
frames_dir = r'/path/to/store/frames'
preprocessed_dir = r'/path/to/store/preprocessed'
resize_dims = (224, 224)
grayscale = True

for frame_name in os.listdir(frames_dir):
    frame_path = os.path.join(frames_dir, frame_name)
    output_path = os.path.join(preprocessed_dir, frame_name)
    preprocess_frames(frame_path, output_path, resize_dims, grayscale)
