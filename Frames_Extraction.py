import cv2
import os
import numpy as np
#from matplotlib import pyplot as plt
import mediapipe as mp
#from moviepy.video.io.VideoFileClip import VideoFileClip
from tensorflow.keras.models import load_model

#video_path = "C:\\Users\\Keerthi Mupparaju\\Downloads\\Adjectives_1of8\\Adjectives\\8. Blind\\MVI_9855.MOV"
#output_folder = "C:\\Users\\nanib\\Desktop\\New folder"
mp_holistic = mp.solutions.holistic  # Holistic model


def mediapipe_detection(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # COLOR CONVERSION BGR 2 RGB
    image.flags.writeable = False  # Image is no longer writeable
    results = model.process(image)  # Make prediction
    image.flags.writeable = True  # Image is now writeable
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # COLOR COVERSION RGB 2 BGR
    return image, results


def extract_features(results):
    pose = np.array([[res.x, res.y, res.z, res.visibility] for res in
                     results.pose_landmarks.landmark]).flatten() if results.pose_landmarks else np.zeros(33 * 4)
    face = np.array([[res.x, res.y, res.z] for res in
                     results.face_landmarks.landmark]).flatten() if results.face_landmarks else np.zeros(468 * 3)
    lh = np.array([[res.x, res.y, res.z] for res in
                   results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21 * 3)
    rh = np.array([[res.x, res.y, res.z] for res in
                   results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(
        21 * 3)
    return np.concatenate([pose,face,lh,rh])
    





