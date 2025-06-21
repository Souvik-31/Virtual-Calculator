import cv2
from cvzone.HandTrackingModule import HandDetector

class Button:
    def __init__(self,pos,width,height,value):

        self.pos = pos
        self.width = width
        self.height = height
        self.value = value

    def draw(self,img):
        cv2.rectangle(img,self.pos, (self.pos[0]+self.width,self.pos[1]+self.height),(225,225,225),cv2.FILLED)
        cv2.rectangle(img,self.pos, (self.pos[0]+self.width,self.pos[1]+self.height),(50,50,50),3)
        cv2.putText(img,self.value, (self.pos[0]+40,self.pos[1]+60),cv2.FONT_HERSHEY_PLAIN,2,(50,50,50),2)
    
    def checkClick(self, x, y):
        if self.pos[0] < x < self.pos[0] + self.width and self.pos[1] < y < self.pos[1] + self.height:
            cv2.rectangle(img,self.pos, (self.pos[0]+self.width,self.pos[1]+self.height),(255,255,255),cv2.FILLED)
            cv2.rectangle(img,self.pos, (self.pos[0]+self.width,self.pos[1]+self.height),(50,50,50),3)
            cv2.putText(img,self.value, (self.pos[0]+25,self.pos[1]+80),cv2.FONT_HERSHEY_PLAIN,5,(0,0,0),5)

            return True
        else:
            return False

cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Set width
cap.set(4, 720)   # Set height
detector = HandDetector(detectionCon=0.8, maxHands=1)

button_list_values = [['7', '8', '9', '^', '('],
                        ['4', '5', '6', '*', ')'],
                        ['1', '2', '3', '-', 'C'],
                        ['0', '.', '/', '+', '=']]

buttonList = []
for x in range(4):
    for y in range(5):
        xpos = x*100 + 150
        ypos = y*100 + 600
        buttonList.append(Button((ypos,xpos), 100, 100, button_list_values[x][y]))

myEquation = ''
delay = 0


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    hands, img = detector.findHands(img,flipType=False)

    cv2.rectangle(img,(600,40), (600+500,70+100),(225,225,225),cv2.FILLED)
    cv2.rectangle(img,(600,40),(600+500,70+100),(50,50,50),3)

    for button in buttonList:
        button.draw(img)
    

    if hands:
        lmlist = hands[0]['lmList']
        length, _, img = detector.findDistance(lmlist[8][:2], lmlist[12][:2], img)
        # print(length)
        x,y = lmlist[8][0:2]
        if(length <= 50):
            for i,button in enumerate(buttonList):
                if button.checkClick(x, y) and delay == 0:
                    myValue = (button_list_values[i // 5][i % 5])
                    if myValue == 'C':
                        if myEquation == 'error':
                            myEquation = ''
                        myEquation = ''
                        delay = 1
                    elif myValue == '^':
                        if myEquation == 'error':
                            myEquation = ''
                        myEquation += '**'
                        delay = 1
                    elif myValue == 'CLEAR':
                        if myEquation == 'error':
                            myEquation = ''
                        myEquation = ''
                        delay = 1
                    elif myValue == '=':
                        if myEquation == 'error':
                            myEquation = ''
                        if myEquation=='':
                            myEquation=''
                        else:
                            try:
                                myEquation = str(eval(myEquation))
                            except:
                                myEquation = 'error'
                        delay = 1
                    else:
                        if myEquation=='error':
                            myEquation = ''
                        myEquation = myEquation + myValue
                        delay = 1
            
    #Add a delay to prevent multiple clicks
    if delay:
        delay += 1
        if delay > 10:
            delay = 0
        
    #display result
    cv2.putText(img, myEquation, (610, 115), cv2.FONT_HERSHEY_PLAIN, 3, (100, 50, 50), 3)


    cv2.imshow("Image", img)
    cv2.waitKey(1)
