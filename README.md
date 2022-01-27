# openCV_HandDetection
Hand detection projects with mediapipe based on openCV python.


## Necessarry dependencies
<p> You can simply pip to install necessarry module. </p>

<code>pip install opencv-python</code>

<code>pip install mediapipe</code>

-----------------------------------
Project Hand Tracking
-----------------------------------
![Hand Tracking](https://drive.google.com/file/d/1xmTfzJQXtShpFspCmNGURYPowTIu-4Tb/view?usp=sharing)
'''python
import cv2
import mediapipe
import htm

cap = cv2.VideoCapture(0)
tracker = htm.handDetector()

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
'''
