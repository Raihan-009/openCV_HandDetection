import cv2
import mediapipe
import handTracker as ht

cap = cv2.VideoCapture(0)
tracker = ht.handDetector()

while True:
    ret, frame = cap.read()
    cv2.rectangle(frame, (10,10), (250,30), (255,255,255), cv2.FILLED)
    cv2.putText(frame, 'Project Hand Tracking', (15,25), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 1)
    if ret:
        detector = tracker.findHands(frame)
        cv2.imshow("Framing", frame)
    else:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()