import cv2
import mediapipe as mp
import pyautogui

# Initialize MediaPipe Hands.
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.5)

# Initialize MediaPipe Drawing utility.
mp_drawing = mp.solutions.drawing_utils

# Initialize webcam.
cap = cv2.VideoCapture(0)

# Get the screen size.
screen_width, screen_height = pyautogui.size()

# Function to convert hand landmark coordinates to screen coordinates.
def hand_landmarks_to_screen_coordinates(landmark, frame_width, frame_height):
    return int(landmark.x * frame_width), int(landmark.y * frame_height)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
    
    # Flip the frame horizontally for a later selfie-view display.
    frame = cv2.flip(frame, 1)
    
    # Convert the BGR image to RGB.
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the image and find hands.
    result = hands.process(rgb_frame)
    
    # Draw the hand annotations on the frame.
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Get the landmark coordinates.
            frame_height, frame_width, _ = frame.shape
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            
            # Convert to screen coordinates.
            index_finger_x, index_finger_y = hand_landmarks_to_screen_coordinates(index_finger_tip, frame_width, frame_height)
            screen_x, screen_y = int(screen_width * (index_finger_x / frame_width)), int(screen_height * (index_finger_y / frame_height))
            
            # Move the mouse.
            pyautogui.moveTo(screen_x, screen_y)
            
            # Calculate the distance between the index finger tip and thumb tip.
            index_finger_x, index_finger_y = hand_landmarks_to_screen_coordinates(index_finger_tip, frame_width, frame_height)
            thumb_x, thumb_y = hand_landmarks_to_screen_coordinates(thumb_tip, frame_width, frame_height)
            
            distance = ((thumb_x - index_finger_x) ** 2 + (thumb_y - index_finger_y) ** 2) ** 0.5
            
            # If the distance is small enough, perform a click.
            if distance < 40:
                pyautogui.click()

    # Display the resulting frame.
    cv2.imshow('Virtual Mouse', frame)
    
    if cv2.waitKey(5) & 0xFF == 27:
        break

# Release the resources.
cap.release()
cv2.destroyAllWindows()
hands.close()

