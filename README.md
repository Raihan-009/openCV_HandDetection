# openCV_HandDetection
Hand detection projects with mediapipe based on openCV python.


## Necessarry dependencies
<p> You can simply pip to install necessarry module. </p>

<code>pip install opencv-python</code>

<code>pip install mediapipe</code>

-----------------------------------
Project Hand Tracking
-----------------------------------

<p align = "center">
    <img src = "https://github.com/Raihan-009/openCV_HandDetection/blob/main/results/handTracking01.png">
</p>
<p align = "center">
    <img src = "https://github.com/Raihan-009/openCV_HandDetection/blob/main/results/handTracking02.png" width = "450" height = "350">
</p>

```python
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
```
-----------------------------------
Project Finger Counting
-----------------------------------

<p align = "center">
    <img src = "https://github.com/Raihan-009/openCV_HandDetection/blob/main/results/fingerCounting01.png" width = "450" height = "350">
</p>
<p align = "center">
    <img src = "https://github.com/Raihan-009/openCV_HandDetection/blob/main/results/fingerCounting02.png" width = "450" height = "350">
</p>

```python
import cv2
import mediapipe
import handTracker as ht

cap = cv2.VideoCapture(0)

tracker = ht.handDetector()
while True:
    ret, frame = cap.read()
    cv2.rectangle(frame, (10,10), (250,30), (255,255,255), cv2.FILLED)
    cv2.putText(frame, 'Project Finger Counting', (15,25), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 1)
    if ret:
        hands = tracker.findHands(frame, drawL = False)
        if hands:
            hand1 = hands[0]
            fingers1 = tracker.fingerCounter(hand1)

            if len(hands) ==2:
                hand2 = hands[1]
                fingers2 = tracker.fingerCounter(hand2)
                # print(fingers2 + fingers1)
                cv2.rectangle(frame, (10,50), (245,200), (55,245,10), cv2.FILLED)
                cv2.putText(frame, str(fingers2 + fingers1), (65,175), cv2.FONT_HERSHEY_COMPLEX, 4, (0,0,0), 20)
            else:
                # print(fingers1)
                cv2.rectangle(frame, (40,50), (200,200), (55,245,10), cv2.FILLED)
                cv2.putText(frame, str(fingers1), (75,175), cv2.FONT_HERSHEY_COMPLEX, 4, (0,0,0), 20)
                
        cv2.imshow("Framing", frame)
    else:
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
```

