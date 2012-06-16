from AntsPairs import AntsPairs
from Ant import Ant

class AntNorth(Ant):
    def __init__(self, x, y):
        Ant.__init__(self, x, y , "N")
        
    def getMeetingAnts(self, ants):
        self._meetingAnts = []
        for ant in [ant for ant in ants if ant.direction != self.direction]:
            if ant.direction == "S":
                antMeeting = Ant.caseNS(self, ant)                
            if ant.direction == "E":
                antMeeting = Ant.caseNE(self, ant)
            if ant.direction == "W":
                antMeeting = Ant.caseNW(self, ant)
            if antMeeting.doTheyMeet:
                self._meetingAnts.append(AntsPairs(self, ant, antMeeting.distance))
        return self._meetingAnts

