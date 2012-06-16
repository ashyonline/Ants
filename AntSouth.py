from AntsPairs import AntsPairs
from Ant import Ant

class AntSouth(Ant):
    def __init__(self, x, y):
        Ant.__init__(self, x, y , "S")
        
    def getMeetingAnts(self, ants):
        self._meetingAnts = []
        for ant in [ant for ant in ants if ant.direction != self.direction]:
            if ant.direction == "N":
                antMeeting = Ant.caseSN(self, ant)                
            if ant.direction == "E":
                antMeeting = Ant.caseSE(self, ant)
            if ant.direction == "W":
                antMeeting = Ant.caseSW(self, ant)
            if antMeeting.doTheyMeet:
                self._meetingAnts.append(AntsPairs(self, ant, antMeeting.distance))
        return self._meetingAnts

