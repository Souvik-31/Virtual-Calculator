from flask import Flask, render_template, Response
import cv2
from cvzone.HandTrackingModule import HandDetector

app = Flask(__name__)




cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Set width
cap.set(4, 720)   # Set height
detector = HandDetector(detectionCon=0.8, maxHands=1)

@app.route('/')
def index():
    return render_template('index.html')  # Loads HTML UI

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
def gen_frames():
    from button import Button  # Import Button class here to avoid circular import
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
                        button.highlight(img)
                        myValue = button.value
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


        # Encode the frame to send it to the browser
        ret, buffer = cv2.imencode('.jpg', img)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

