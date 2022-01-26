import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands() #creating a object
mpDraw =  mp.solutions.drawing_utils

while True:
    ret, frame = cap.read()
    #print(ret)
    if ret:

        rgbImg = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgbImg)
        #print(results.multi_hand_landmarks)
        if results.multi_hand_landmarks:
            for handlms in results.multi_hand_landmarks:
                for id, lm in enumerate(handlms.landmark):
                    #print(id,lm)
                    h, w, c = frame.shape
                    cx,cy = int(lm.x*w), int(lm.y*h)
                    print(id,cx,cy)
                mpDraw.draw_landmarks(frame, handlms, mpHands.HAND_CONNECTIONS)

        cv2.imshow("Framing", frame)
    else:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()