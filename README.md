# hand_gesture Controlled virtual mouse
<br>
This project implements a Virtual Mouse using Python, OpenCV, MediaPipe, and PyAutoGUI.
It allows you to control the computer cursor with hand gestures captured via a webcam — no physical mouse needed! 
<br>
**Features**
<br>
Move cursor by tracking your index finger tip
<br>
Click action by bringing the thumb and index finger close together
<br>
Real-time hand tracking using MediaPipe Hands
<br>
Works on any screen size (auto-calibrated with PyAutoGUI)
<br>
Smooth tracking with continuous video feed from your webcam
<br>
**Technologies Used**
<br>
Python
<br>
OpenCV (for video processing)
<br>
MediaPipe (for hand landmark detection & tracking)
<br>
PyAutoGUI (for controlling the mouse pointer and clicks)
<br>
**How It Works**
<br>
The webcam captures the live video feed.
<br>
MediaPipe Hands detects 21 landmarks on your hand.
<br>
The index finger tip is mapped to screen coordinates for cursor movement.
<br>
When the thumb tip comes close to the index finger tip, a click event is triggered.
