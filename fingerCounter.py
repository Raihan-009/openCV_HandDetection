# openCV project one : Finger Counter


import cv2
import mediapipe
import handtracker as ht

cap = cv2.VideoCapture(0)
detector = ht.handDetector(detectionCon=0.5)

tipIds = [4,8,12,16,20]

while True:

    ret, frame = cap.read()

    cv2.rectangle(frame, (10,10), (250,30), (255,255,255), cv2.FILLED)
    cv2.putText(frame, 'Project Finger Counting', (15,25), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 1)

    img = detector.findHands(frame, draw=False)
    landmarksList = detector.getCordinates(img)
    #print(landmarksList)

    if len(landmarksList) != 0:
        fingers = []

        if landmarksList[tipIds[0]][1] > landmarksList[tipIds[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range (1,5):
            if landmarksList[tipIds[id]][2] < landmarksList[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        
        # print(fingers)
        totalFingers = fingers.count(1)
        print(fingers.count(1))


        cv2.rectangle(frame, (40,50), (200,200), (55,245,10), cv2.FILLED)
        cv2.putText(frame, str(totalFingers), (75,175), cv2.FONT_HERSHEY_COMPLEX, 4, (0,0,0), 20)



    cv2.imshow("Framing", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows