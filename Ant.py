from AntMeeting import AntMeeting

class Ant:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
    
    def caseNS(self, ant):
        return ant.caseSN(self)

    def caseSN(self, ant):
        distance = (self.y - ant.y)/2
        doTheyMeet = self.x == ant.x and self.y > ant.y
        return AntMeeting(doTheyMeet, distance)

    def caseWE(self, ant):
        return ant.caseEW(self)
    
    def caseEW(self, ant):
        distance = (ant.x - self.x)/2
        doTheyMeet = self.y == ant.y and self.x < ant.x
        return AntMeeting(doTheyMeet, distance)

    def caseSE(self, ant):
        return ant.caseES(self)
    
    def caseES(self, ant):
        distance = ant.x - self.x
        doTheyMeet = (ant.x - self.x == ant.y - self.y) and ant.x > self.x
        return AntMeeting(doTheyMeet, distance)

    def caseNE(self, ant):
        return ant.caseEN(self)
    
    def caseEN(self, ant):
        distance = ant.x - self.x
        doTheyMeet = (ant.x - self.x == self.y - ant.y) and ant.x > self.x
        return AntMeeting(doTheyMeet, distance)

    def caseSW(self, ant):
        return ant.caseWS(self)
    
    def caseWS(self, ant):
        distance = self.x - ant.x
        doTheyMeet = (self.x - ant.x == ant.y - self.y) and self.x > ant.x
        return AntMeeting(doTheyMeet, distance)

    def caseNW(self, ant):
        return ant.caseWN(self)
    
    def caseWN(self, ant):
        distance = self.x - ant.x
        doTheyMeet = (self.x - ant.x == self.y - ant.y) and self.x > ant.x
        return AntMeeting(doTheyMeet, distance)
    
        
    
        
