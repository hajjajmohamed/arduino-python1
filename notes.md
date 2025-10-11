# 🖐️ Control LED by Hand using Python and Arduino

## 👨‍💻 Project Overview
This project allows you to control an LED connected to an Arduino board using your **hand gestures** detected by a **camera**.  
Python uses **OpenCV** and **MediaPipe** to detect the position of your hand in real time, and **PyFirmata** sends the command to Arduino to turn the LED **ON** or **OFF**.

---

## 🧩 Components Required

| Component | Quantity | Description |
|------------|-----------|-------------|
| Arduino Uno | 1 | Main controller board |
| LED | 1 | Used to visualize ON/OFF |
| 220Ω Resistor | 1 | Current limiter for LED |
| Breadboard | 1 | For easy connections |
| Jumper wires | few | For wiring |
| USB Cable | 1 | To connect Arduino to PC |

---

## 💻 Software & Libraries
**Required Software:**
- Arduino IDE  
- Python 3.x  

**Install Python Libraries:**
```bash
pip install pyfirmata opencv-python mediapipe
