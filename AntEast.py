from AntsPairs import AntsPairs
from Ant import Ant

class AntEast(Ant):
    def __init__(self, x, y):
        Ant.__init__(self, x, y , "E")
        
    def getMeetingAnts(self, ants):
        self._meetingAnts = []
        for ant in [ant for ant in ants if ant.direction != self.direction]:
            if ant.direction == "N":
                antMeeting = Ant.caseEN(self, ant)                
            if ant.direction == "S":
                antMeeting = Ant.caseES(self, ant)
            if ant.direction == "W":
                antMeeting = Ant.caseEW(self, ant)
            if antMeeting.doTheyMeet:
                self._meetingAnts.append(AntsPairs(self, ant, antMeeting.distance))
        return self._meetingAnts

