import cv2
import cvzone
import pynput
from cvzone.HandTrackingModule import HandDetector
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

detector = HandDetector(staticMode=False,maxHands=2,detectionCon=0.6)

cap = cv2.VideoCapture(0)

while True:
    
    success, img = cap.read()
    
    hands,img = detector.findHands(img,draw=True)
    
    if hands:
        hand1 = hands[0]
        lmList1 = hand1['lmList']
        bbox1 = hand1['bbox']
        center1 = hand1['center']
        handType1 = hand1['type']
        
        fingers1 = detector.fingersUp(hand1)
        
        if fingers1 == [0,0,0,0,1]:
            keyboard.press('d')
            
        elif fingers1 == [1,0,0,0,0]:
            keyboard.press('a')
            
        
        elif fingers1 == [0,1,0,0,0]:
            keyboard.press('w')
        
        elif fingers1 == [0,1,0,0,1]:
            keyboard.press('w')
            keyboard.press('d')
        
        elif fingers1 == [1,1,0,0,0]:
            keyboard.press('w')
            keyboard.press('d')
            
        else:
            keyboard.release('w')
            keyboard.release('a')
            keyboard.release('d')
            
        if len(hands)==2:
            
            hand2 = hands[1]
            lmList2 = hand2['lmList']
            bbox2 = hand2['bbox']
            center2 = hand2['center']
            handType2 = hand2['type']
            
            fingers2 = detector.fingersUp(hand2)
            
            if fingers2 == [1,0,0,0,0]:
                keyboard.press(Key.right)
                
            elif fingers2 == [0,0,0,0,1]:
                keyboard.press(Key.left)
                
            
            elif fingers2 == [0,1,0,0,0]:
                keyboard.press(Key.up)
            
            elif fingers2 == [1,1,0,0,0]:
                keyboard.press(Key.up)
                keyboard.press(Key.right)
            
            elif fingers2 == [0,1,0,0,1]:
                keyboard.press(Key.up)
                keyboard.press(Key.left)
                
            else:
                keyboard.release(Key.up)
                keyboard.release(Key.left)
                keyboard.release(Key.right)
    
    cv2.imshow("Img",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break