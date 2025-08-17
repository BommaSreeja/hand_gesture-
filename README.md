# hand_gesture Controlled virtual mouse
This project implements a Virtual Mouse using Python, OpenCV, MediaPipe, and PyAutoGUI.
It allows you to control the computer cursor with hand gestures captured via a webcam — no physical mouse needed! 
**Features**
Move cursor by tracking your index finger tip
Click action by bringing the thumb and index finger close together
Real-time hand tracking using MediaPipe Hands
Works on any screen size (auto-calibrated with PyAutoGUI)
Smooth tracking with continuous video feed from your webcam
**Technologies Used**
Python
OpenCV (for video processing)
MediaPipe (for hand landmark detection & tracking)
PyAutoGUI (for controlling the mouse pointer and clicks)
**How It Works**
The webcam captures the live video feed.
MediaPipe Hands detects 21 landmarks on your hand.
The index finger tip is mapped to screen coordinates for cursor movement.
When the thumb tip comes close to the index finger tip, a click event is triggered.
