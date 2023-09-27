# import cv2
# import tensorflow as tf

# # Load the face detection model
# model = tf.keras.applications.resnet50.ResNet50(weights='imagenet')
# model = tf.keras.models.Sequential([
#     model,
#     tf.keras.layers.Dense(128, activation='relu'),
#     tf.keras.layers.Dense(64, activation='relu'),
#     tf.keras.layers.Dense(2)
# ])

# # Open the video file
# cap = cv2.VideoCapture("video.mp4")

# # Create a video writer object
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

# # out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# # Loop over the video frames
# while True:

#     # Read the next frame
#     ret, frame = cap.read()

#     # If the frame is empty, break out of the loop
#     if not ret:
#         break

#     # Convert the frame to a TensorFlow tensor
#     frame = tf.expand_dims(frame, axis=0)
#     frame = tf.cast(frame, dtype=tf.float32)

#     # Detect faces in the frame
#     predictions = model.predict(frame)

#     # Count the number of faces detected
#     num_faces = len(predictions[0])

#     # Draw a bounding box around each face
#     for i in range(num_faces):
#         box = predictions[0][i]
#         cv2.rectangle(frame, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (0, 255, 0), 2)

#     # Display the number of faces detected in the corner of the frame
#     cv2.putText(frame, "Face detected: {}".format(num_faces), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

#     # Write the frame to the output video
#     out.write(frame)

# # Release the video capture and video writer objects
# cap.release()
# out.release()

# # Close all windows
# cv2.destroyAllWindows()

# -----------------------------------------------------------------------------------

# import cv2

# # Load the pre-trained face detection model from OpenCV
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# # Open a video capture object (you can replace 'your_video.mp4' with your video file)
# cap = cv2.VideoCapture('video.mp4')

# # Get the width and height of the video frames
# width = int(cap.get(3))
# height = int(cap.get(4))

# # Define the font and text settings for displaying face count
# font = cv2.FONT_HERSHEY_SIMPLEX
# font_scale = 1
# font_color = (255, 255, 255)
# line_type = 2

# # Initialize variables for counting faces
# total_faces = 0

# while True:
#     # Read a frame from the video
#     ret, frame = cap.read()
    
#     # Check if a frame was successfully read
#     if not ret:
#         break
    
#     # Convert the frame to grayscale for face detection
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
#     # Detect faces in the frame
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    
#     # Draw rectangles around the detected faces
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
#     # Update the total faces count
#     total_faces = len(faces)
    
#     # Display the face count on the frame
#     text = f"Face Detected: {total_faces}, Total Faces: {total_faces}"
#     cv2.putText(frame, text, (width - 300, 30), font, font_scale, font_color, line_type)
    
#     # Display the frame with face detection results
#     cv2.imshow('Video with Face Detection', frame)
    
#     # Exit the loop if the 'q' key is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the video capture object and close all OpenCV windows
# cap.release()
# cv2.destroyAllWindows()

# --------------------------------------------------------------------------------

# import cv2

# # Load the pre-trained face detection model from OpenCV
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# # Open a video capture object (you can replace 'your_video.mp4' with your video file)
# cap = cv2.VideoCapture('video.mp4')

# # Initialize a set to store unique faces
# unique_faces = set()

# # Initialize variables for counting faces
# total_faces = 0
# font = cv2.FONT_HERSHEY_SIMPLEX
# font_scale = 1
# font_color = (255, 255, 255)
# line_type = 2

# while True:
#     # Read a frame from the video
#     ret, frame = cap.read()
    
#     # Check if a frame was successfully read
#     if not ret:
#         break
    
#     # Convert the frame to grayscale for face detection
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
#     # Detect faces in the frame
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    
#     # Draw rectangles around the detected faces
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#         unique_faces.add(tuple((x, y, w, h)))  # Add detected faces to the set
    
#     # Update the real-time face detection count
#     total_faces = len(faces)
    
#     # Display the real-time face detection count and total unique faces count in the upper right corner
#     text = f"Face Detected: {total_faces}, Total Faces: {len(unique_faces)}"
#     cv2.putText(frame, text, (frame.shape[1] - 300, 30), font, font_scale, font_color, line_type)
    
#     # Display the frame with face detection results
#     cv2.imshow('Video with Face Detection', frame)
    
#     # Exit the loop if the 'q' key is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the video capture object and close all OpenCV windows
# cap.release()
# cv2.destroyAllWindows()

# -------------------------------------------------------------------------------------
# import cv2

# # Load the pre-trained face detection model from OpenCV
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# # Open a video capture object (you can replace 'your_video.mp4' with your video file)
# cap = cv2.VideoCapture('video.mp4')

# # Get the width and height of the video frames
# width = int(cap.get(3))
# height = int(cap.get(4))

# # Define the font and text settings for displaying face count
# font = cv2.FONT_HERSHEY_SIMPLEX
# font_scale = 1
# font_color = (255, 255, 255)
# line_type = 2

# # Initialize variables for counting faces
# total_faces = 0

# while True:
#     # Read a frame from the video
#     ret, frame = cap.read()
    
#     # Check if a frame was successfully read
#     if not ret:
#         break
    
#     # Convert the frame to grayscale for face detection
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
#     # Detect faces in the frame
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    
#     # Draw rectangles around the detected faces
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
#     # Update the total faces count
#     total_faces = len(faces)
    
#     # Display the face count on the frame
#     text = f"Face Detected: {total_faces}, Total Faces: {total_faces}"
#     cv2.putText(frame, text, (width - 300, 30), font, font_scale, font_color, line_type)
    
#     # Display the frame with face detection results
#     cv2.imshow('Video with Face Detection', frame)
    
#     # Exit the loop if the 'q' key is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the video capture object and close all OpenCV windows
# cap.release()
# cv2.destroyAllWindows()

import cv2
import torch
import torchvision

# Load the face detection model
model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)

# Open the video file
cap = cv2.VideoCapture("video.mp4")

# Create a video writer object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

# out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# Loop over the video frames
while True:

    # Read the next frame
    ret, frame = cap.read()

    # If the frame is empty, break out of the loop
    if not ret:
        break

    # Convert the frame to a PyTorch tensor
    frame = torch.from_numpy(frame).permute(2, 0, 1).float()

    # Detect faces in the frame
    detections = model(frame)[0]

    # Count the number of faces detected
    num_faces = len(detections["boxes"])

    # Draw a bounding box around each face
    for i in range(num_faces):
        box = detections["boxes"][i].int()
        cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)

    # Display the number of faces detected in the corner of the frame
    cv2.putText(frame, "Face detected: {}".format(num_faces), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Write the frame to the output video
    out.write(frame)

# Release the video capture and video writer objects
cap.release()
out.release()

# Close all windows
cv2.destroyAllWindows()