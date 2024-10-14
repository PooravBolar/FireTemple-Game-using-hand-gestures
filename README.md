# 🖐️ Hand Gesture-Controlled Keyboard Input 🖥️

This project allows you to control keyboard inputs using hand gestures. Utilizing computer vision and hand tracking, specific hand gestures trigger different keyboard keys, enabling touchless interaction with applications. It's perfect for gaming or controlling apps with simple hand movements!

---

## ✨ Features:

- **Real-time Hand Gesture Recognition**: Detects hand gestures and maps them to keyboard inputs.
- **Keyboard Control**: Control keypresses (e.g., 'W', 'A', 'D', arrow keys) with simple hand gestures.
- **Dual-Hand Support**: Detects gestures from one or both hands, offering versatile control.

---

## 🛠️ How it Works:

1. **Hand Detection**: The app uses `cvzone`'s `HandDetector` module to track hand landmarks in real-time.
2. **Gesture-to-Keyboard Mapping**: Hand gestures are mapped to specific key presses using the `pynput` library to simulate keyboard input.
3. **Dual-Hand Detection**: When two hands are detected, the gestures of both hands are independently mapped to different keyboard actions.

---

## 🧰 Requirements:

Before running the code, make sure to install the required libraries:

```bash
pip install opencv-python
pip install cvzone
pip install pynput
```

---

🚀 Running the App:
1) Start the Application: Ensure your webcam is connected, and run the script.
```bash
python gesture_control_keyboard.py
```

2) Control with Gestures: Use the following gestures to control the keyboard:

- Right Hand Gestures:
Thumb up : Press 'A',
Pinky up : Press 'D',
Index finger up : Press 'W',
- Left Hand Gestures:
Thumb up : Press right arrow,
Pinky up : Press left arrow,
Index finger up : Press up arrow,
3) Quit the App: Press q to exit the program.

---

## 🤝 Contribution:
Feel free to fork this repository, make your changes, and create a pull request. Any contributions or suggestions are welcome!

---

## 📧 Contact:
Have any questions or feedback? Feel free to reach out!
📩 Email: [pooravbolar3@gmail.com]

