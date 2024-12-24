from picamera2 import Picamera2
import cv2
import mediapipe as mp

import gpiozero as GPIO
import time
import threading

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Initialize Pi Camera
picam2 = Picamera2()
picam2.preview_configuration.main.size = (640, 480)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.controls.FrameRate = 30
picam2.configure("preview")
picam2.start()


led = GPIO.LED(18)
drc = GPIO.LED(23)


def test(i):
    for p in range(i):
        led.on()
        time.sleep(0.0000001)
        led.off()
        time.sleep(0.0000001)
        print(p)
        
threading.Thread(target=lambda: test(128000)).start()

while True:
    # Capture frame from Pi Camera
    frame = picam2.capture_array()

    # Process frame with MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Analyze landmarks for thumbs up/down
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            thumb_ip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
            wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]

            if thumb_tip.y < wrist.y:
                cv2.putText(frame, "Thumbs Up", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                drc.on()
            elif thumb_tip.y > wrist.y:
                cv2.putText(frame, "Thumbs Down", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                drc.off()


  
    #cv2.imshow("Thumbs Detection", frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


picam2.stop()
cv2.destroyAllWindows()
