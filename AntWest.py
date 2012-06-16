from AntsPairs import AntsPairs
from Ant import Ant

class AntWest(Ant):
    def __init__(self, x, y):
        Ant.__init__(self, x, y , "W")
        
    def getMeetingAnts(self, ants):
        self._meetingAnts = []
        for ant in [ant for ant in ants if ant.direction != self.direction]:
            if ant.direction == "N":
                antMeeting = Ant.caseWN(self, ant)                
            if ant.direction == "S":
                antMeeting = Ant.caseWS(self, ant)
            if ant.direction == "E":
                antMeeting = Ant.caseWE(self, ant)
            if antMeeting.doTheyMeet:
                self._meetingAnts.append(AntsPairs(self, ant, antMeeting.distance))
        return self._meetingAnts

