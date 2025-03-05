import cv2
import numpy as np
import mediapipe as mp

# Initialiserer kamera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Konverterer til gråskala for enklere behandling
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Bruker en terskel for å finne lyse områder
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    
    # Finn konturer i det binære bildet
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Beregner arealet til konturen
        area = cv2.contourArea(contour)
        
        # Filtrerer ut veldig små områder (støy)
        if area > 50:
            # Tegner en boks rundt funnet område
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "LED Detected", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Viser resultatet
    cv2.imshow("Frame", frame)

    # Avslutt med 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
