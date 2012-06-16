from AntsPairs import AntsPairs
from AntFactory import AntFactory

class World:
    def __init__(self, xs, ys, dirs, debug=False):
        assert len(xs) == len (ys) == len(dirs)
        """ prints ants status if setted in True """
        self._debugModeOn = debug
        
        # init data
        self.xs = [float(x) for x in xs]
        self.ys = [float(y) for y in ys]
        self.directions = list(dirs)
        self.antFactory = AntFactory()
        self.createAnts()
        self.createAntsPairsSimulation()
        self.orderAntsPairsByTime()
        self.filterAntsPairs()

    def antsThatStillExist(self):
        """ remove dead ants from ant's container and return size """
        for deadAnt in self.deadAnts:
            if deadAnt in self.ants:
                self.ants.remove(deadAnt)
                
        return len(self.ants)

    def createAnts(self):
        """ each ant uses an x, y position and a direction """
        self.ants = []
        for index in range(len(self.xs)):
            self.ants.append(self.antFactory.createAnt(self.xs[index], self.ys[index], self.directions[index]))
            if self._debugModeOn:
                print "({0}, {1}, {2})".format(self.ants[index].x, self.ants[index].y, self.ants[index].direction)
            
        if self._debugModeOn:
            print "Ants total: {0} \n".format(len(self.ants))
            
    def createAntsPairsSimulation(self):
        """ for each two ants, create a pair """
        self.antsPairs = []
        for fstIndex in range(len(self.ants)):
            fstAnt = self.ants[fstIndex]
            self.antsPairs.extend(fstAnt.getMeetingAnts(self.ants[fstIndex+1:]))

    def orderAntsPairsByTime(self):
        """ order pairs that meet by when do both ants meet """
        self.antsPairs.sort(key=lambda pair:pair.whenDoTheyMeet)
        if self._debugModeOn:
            print "Pairs filtered and ordered:"
            for pair in self.antsPairs:
                print "({0}, {1}, {2}), ({3}, {4}, {5}) --> time: {6}".format(pair.fstAnt.x, pair.fstAnt.y, pair.fstAnt.direction, pair.sndAnt.x, pair.sndAnt.y,pair.sndAnt.direction, pair.whenDoTheyMeet)
        
    def filterAntsPairs(self):
        """ check ants that meet by time and disappear those who didn't dissappear before """
        self.deadAnts = []
        auxDeadAnts = []
        currentTime = -1
        
        for pair in self.antsPairs:
            if currentTime != pair.whenDoTheyMeet:
                # save ants that dissappear for previous time
                if self._debugModeOn:
                    print "partially dead ants: {0}".format(len(auxDeadAnts))
                self.deadAnts.extend(auxDeadAnts)
                currentTime = pair.whenDoTheyMeet
                auxDeadAnts = []

            if self._debugModeOn:
                print "({0}, {1}, {2}), ({3}, {4}, {5}) --> time: {6}".format(pair.fstAnt.x, pair.fstAnt.y, pair.fstAnt.direction, pair.sndAnt.x, pair.sndAnt.y,pair.sndAnt.direction, pair.whenDoTheyMeet)

            # if none of the ants in the pair has previously dissapeared, store to make them disappear
            if (not pair.fstAnt in self.deadAnts and not pair.sndAnt in self.deadAnts):
                auxDeadAnts.extend([ant for ant in [pair.fstAnt, pair.sndAnt] if not ant in auxDeadAnts])

        if self._debugModeOn:
            print "partially dead ants: {0}".format(len(auxDeadAnts))

        # save ants that dissappear last time
        self.deadAnts.extend(auxDeadAnts)
        
        if self._debugModeOn:
            print "Total ants that disappeared: {0}".format(len(self.deadAnts))
            print "Total ants that still exist: {0}".format(self.antsThatStillExist())
            print "List:"
            for ant in self.ants:
                print "({0}, {1}, {2})".format(ant.x, ant.y, ant.direction)
