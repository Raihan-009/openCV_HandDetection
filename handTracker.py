from re import L
import cv2
import mediapipe as mp


class handDetector():
    def __init__(self, 
                mode=False, 
                maxHands = 2, 
                modelComplexity=1, 
                detectionCon = 0.5, 
                trackCon = 0.5):
                
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplexity = modelComplexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplexity, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

        self.tipIds = [4,8,12,16,20]
    
    def findHands(self, img, drawL = True, drawB = True, mirror = True):
        rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(rgbImg)
        allHands = []
        h,w,c = img.shape

        if self.results.multi_hand_landmarks:
            for handType, handLms in zip(self.results.multi_handedness,self.results.multi_hand_landmarks):
                myHand = {}
                lmList = []
                xList = []
                yList = [] 
                for id, lm in enumerate(handLms.landmark):
                    cx, cy = int(lm.x*w), int(lm.y*h)
                    lmList.append([id, cx, cy])
                    xList.append(cx)
                    yList.append(cy)

                #bounding box
                xmin, xmax = min(xList), max(xList)
                ymin, ymax = min(yList), max(yList)

                box_W = xmax - xmin
                box_H = ymax - ymin

                bbox = xmin, ymin, box_W, box_H
                myHand["landmarksList"] = lmList
                myHand["bbox"] = bbox
                
                if mirror:
                    if handType.classification[0].label == "Right":
                        myHand["hand_type"] = "Left Hand"
                    else:
                        myHand["hand_type"] = "Right Hand"
                else:
                    myHand["hand_type"] = handType.classification[0].label
                allHands.append(myHand)

                #draw utils
                if drawL:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

                if drawB:
                    cv2.rectangle(img, (bbox[0] - 20, bbox[1] - 20),
                                  (bbox[0] + bbox[2] + 20, bbox[1] + bbox[3] + 20),
                                  (255, 0, 255), 2)
        return allHands
    def fingerCounter(self, myHand):
        myHandType = myHand["hand_type"]
        myLandmarksList = myHand["landmarksList"]
        if self.results.multi_hand_landmarks:
            fingers = []

            #Thumb finger
            if myHandType == "Right Hand":
                if myLandmarksList[self.tipIds[0]][1] > myLandmarksList[self.tipIds[0]-1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            else:
                if myLandmarksList[self.tipIds[0]][1] < myLandmarksList[self.tipIds[0]-1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            # rest of the fingers

            for id in range (1,5):
                if myLandmarksList[self.tipIds[id]][2] < myLandmarksList[self.tipIds[id]-2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
        return fingers.count(1)

def main():

    cap = cv2.VideoCapture(0)
    tracker = handDetector()
    while True:
        ret, frame = cap.read()
        if ret:
            hands = tracker.findHands(frame, drawL = False)
            if hands:
                hand1 = hands[0]
                fingers1 = tracker.fingerCounter(hand1)

                if len(hands) ==2:
                    hand2 = hands[1]
                    fingers2 = tracker.fingerCounter(hand2)
                    print(fingers2 + fingers1)
                else:
                    print(fingers1)
                    
            cv2.imshow("Framing", frame)
        else:
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
