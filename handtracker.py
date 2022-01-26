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
    
    def findHands(self, img, draw = True):
        rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(rgbImg)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:

                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

        return img
    def getCordinates(self, img, handNo=0, draw = True):
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x*w), int(lm.y*h)
                    # print(id, cx, cy)
                    lmList.append([id, cx, cy])

        return lmList

        
def main():

    cap = cv2.VideoCapture(0)
    tracker = handDetector()
    while True:
        ret, frame = cap.read()
        if ret:
            frame = tracker.findHands(frame)
            landmarksList = tracker.getCordinates(frame)
            if len(landmarksList) !=0 :
                print(landmarksList)
            
            cv2.imshow("Framing", frame)
        else:
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
