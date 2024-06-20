import cv2
import numpy as np
from tensorflow.keras.models import load_model
from Frames_Extraction import mediapipe_detection, extract_features
import mediapipe as mp
def method():
    # Load the pre-trained model
    model = load_model("action75a.h5")

    # Initialize MediaPipe holistic model
    mp_holistic = mp.solutions.holistic

    # Define the actions corresponding to the model output
    actions = np.array(['1. loud','2. quiet','3. happy','4. sad','5. Beautiful','6. Ugly','7. Deaf','8. Blind','9. Nice','10. Mean','11. rich','12. poor','13. thick','14. thin','15. expensive','16. cheap','17. flat','18. curved','19. male','20. female','21. tight','22. loose','23. high','24. low','25. soft','26. hard','27. deep','28. shallow','29. clean','30. dirty','31. strong','32. weak','33. dead','34. alive','35. heavy'])

    def prob_viz(predicted_action, input_frame):
        output_frame = input_frame.copy()
        cv2.putText(output_frame, predicted_action, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        return output_frame

    # 1. New detection variables
    sequence = []
    sentence = []
    predictions = []
    threshold = 0.5

    cap = cv2.VideoCapture(0)
    # Set mediapipe model 
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        while cap.isOpened():

            # Read feed
            ret, frame = cap.read()

            # Make detections
            image, results = mediapipe_detection(frame, holistic)
            
            # 2. Prediction logic
            keypoints = extract_features(results)
            sequence.append(keypoints)
            sequence = sequence[-40:]
            
            if len(sequence) == 40:
                res = model.predict(np.expand_dims(sequence, axis=0))[0]
                predicted_action = actions[np.argmax(res)].split()[1]
                #print(predicted_action)
                predictions.append(np.argmax(res))
                
                 #3. Viz logic
                if np.max(res) > threshold: 
                    if len(sentence) > 0: 
                        if predicted_action != sentence[-1]:
                             sentence.append(predicted_action)
                    else:
                         sentence.append(predicted_action)

                if len(sentence) > 5: 
                    sentence = sentence[-5:]

                # Viz probabilities
                image = prob_viz(predicted_action, image)

            # Show to screen
            cv2.imshow('OpenCV Feed', image)

            # Break gracefully
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
