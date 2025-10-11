import cv2
import mediapipe as mp
from pyfirmata import Arduino, util
import time

# Set Arduino Port
port = "COM8"  # Change this to your port (e.g., COM3, /dev/ttyUSB0)
board = Arduino(port)
led = board.get_pin("d:13:o")

# MediaPipe setup
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# Start camera
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lmList = []
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((id, cx, cy))
            
            # Check finger position
            if lmList:
                if lmList[8][2] < 200:  # Finger up
                    led.write(1)
                    cv2.putText(img, "LED ON", (10, 70),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)
                else:
                    led.write(0)
                    cv2.putText(img, "LED OFF", (10, 70),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)
            
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Hand LED Control", img)
    if cv2.waitKey(1) & 0xFF == 27:  # Press ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
board.exit()
