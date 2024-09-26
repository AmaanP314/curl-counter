import cv2
import numpy as np
import mediapipe as mp
import base64
from io import BytesIO
from PIL import Image
import re

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Initialize rep counters and stages for both arms
right_reps = 0
left_reps = 0
stage_right = None
stage_left = None

# Function to calculate the angle between points
def calculate_angle(point1, point2, point3):
    a = np.array(point1)
    b = np.array(point2)
    c = np.array(point3)
    
    ab = a - b
    bc = c - b
    
    angle = np.arctan2(np.linalg.norm(np.cross(ab, bc)), np.dot(ab, bc))
    return np.degrees(angle)

frames = 0
# Function to process each frame
def processor_frame(image_data):
    global right_reps, left_reps, stage_right, stage_left, frames
    frames += 1

    # Initialize reps and stages
    reps = {"right": right_reps, "left": left_reps}
    stages = {"right": stage_right, "left": stage_left}

    if frames % 5 != 0:
        return reps, stages
    
    # Decode base64 image
    image_data = re.sub('^data:image/.+;base64,', '', image_data)
    image = Image.open(BytesIO(base64.b64decode(image_data)))

    # Convert image to OpenCV format
    frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Process the frame with MediaPipe Pose
    results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark
        
        # Right arm
        right_shoulder = (landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y)
        right_elbow = (landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y)
        right_wrist = (landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y)

        right_angle = calculate_angle(right_shoulder, right_elbow, right_wrist)

        if right_angle > 150:
            stage_right = 'Relaxed'
        if right_angle < 80 and stage_right == 'Relaxed':
            stage_right = 'FLEX!'
            right_reps += 1

        # Left arm
        left_shoulder = (landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y)
        left_elbow = (landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y)
        left_wrist = (landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y)

        left_angle = calculate_angle(left_shoulder, left_elbow, left_wrist)

        if left_angle > 150:
            stage_left = 'Relaxed'
        if left_angle < 80 and stage_left == 'Relaxed':
            stage_left = 'FLEX!'
            left_reps += 1

    # Update reps and stages to return
    reps = {"right": right_reps, "left": left_reps}
    stages = {"right": stage_right, "left": stage_left}

    return reps, stages