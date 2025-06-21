import cv2

class Button:
    def __init__(self, pos, width, height, value):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value

    def draw(self, img):
        cv2.rectangle(img, self.pos,
                      (self.pos[0] + self.width, self.pos[1] + self.height),
                      (225, 225, 225), cv2.FILLED)
        cv2.rectangle(img, self.pos,
                      (self.pos[0] + self.width, self.pos[1] + self.height),
                      (50, 50, 50), 3)
        cv2.putText(img, self.value,
                    (self.pos[0] + 30, self.pos[1] + 60),
                    cv2.FONT_HERSHEY_PLAIN, 2, (50, 50, 50), 2)

    def checkClick(self, x, y):
        return self.pos[0] < x < self.pos[0] + self.width and self.pos[1] < y < self.pos[1] + self.height

    def highlight(self, img):
        cv2.rectangle(img, self.pos,
                      (self.pos[0] + self.width, self.pos[1] + self.height),
                      (255, 255, 255), cv2.FILLED)
        cv2.rectangle(img, self.pos,
                      (self.pos[0] + self.width, self.pos[1] + self.height),
                      (50, 50, 50), 3)
        cv2.putText(img, self.value,
                    (self.pos[0] + 25, self.pos[1] + 80),
                    cv2.FONT_HERSHEY_PLAIN, 5, (0, 0, 0), 5)
