# SpeakEazy

## Project Overview

*SpeakEazy* is a website designed to bridge the gap between Deaf and Dumb individuals and the hearing community. This platform leverages advanced machine learning techniques and web development technologies to enable communication between individuals who use sign language and those who do not. The core idea of the project is to provide three main features that convert gestures into text, convert voice into text, and convert text into voice, enabling seamless communication across various modalities.

## Features

1. *Gesture to Text*  
   This feature translates sign language gestures into text using a combination of computer vision and machine learning techniques. It involves:
   - *OpenCV*: Utilized for dividing video into frames for efficient gesture recognition.
   - *MoviePy*: Implemented for data augmentation to improve model performance.
   - *MediaPipe*: Used to extract key points or coordinates from gestures in real-time.
   - *LSTM Model*: Trained on the pre-processed data, which gave us an accuracy of 75%.

2. *Voice to Text*  
   This feature converts spoken words into text to help hearing individuals communicate with Deaf and Dumb individuals. It is developed using *JavaScript* for real-time voice recognition.

3. *Text to Voice*  
   This feature takes the text input and converts it into speech, allowing Deaf and Dumb individuals to communicate their responses audibly. It is also developed using *JavaScript* for real-time text-to-speech conversion.

## Tech Stack

- *Frontend*:
  - HTML, CSS, JavaScript
  - Web technologies used for Voice to Text and Text to Voice features

- *Backend*:
  - Python (for Gesture to Text feature)
  - Django (to integrate the ML model into the website)

- *Machine Learning*:
  - MediaPipe (for key point extraction from gestures)
  - OpenCV (for video frame processing)
  - MoviePy (for data augmentation)
  - LSTM Model (for gesture recognition)

## Installation

1. Clone the repository:
   bash
   git clone https://github.com/MupparajuKeerthi/SpeakEazy.git
   

2. Navigate to the project directory:
   bash
   cd SpeakEazy
   

3. Install dependencies:
   bash
   pip install -r requirements.txt
   

4. Run the application:
   bash
   django-admin startproject SpeakEazy
   

## How to Use

1. *Gesture to Text*: The website captures real-time video or video file of gestures and converts them to text using machine learning. Users need to allow camera access to enable this feature.
   
2. *Voice to Text*: Users can speak directly into their device’s microphone, and the website will convert their voice into text in real-time.

3. *Text to Voice*: Users can input text in a text box, and the website will convert the text into speech, which can be played back using the browser's audio system or can be downloded into one's local system.

## Future Improvements

- Improve gesture recognition accuracy with additional training data.
- Add support for more languages and dialects.
- Implement more sophisticated voice recognition and text-to-speech systems.

## Contributors

- Mupparaju Keerthi(https://github.com/MupparajuKeerthi)
- Mancineella Sai Lokesh
- P.V.Lokesh
- Manchala Nandini
- Kamal Vardhan
- A.Mohama Sangeetha
- Ganesh
- Vardhan
- Varun
- Sruthi
- Kyathi
- Triveni
- Mahipathi Siva Naga Raju

