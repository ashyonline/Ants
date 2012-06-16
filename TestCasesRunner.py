from World import World
class TestCasesRunner:
    def __init__(self):
        debug = False
        w = World([],[],"", debug)
        assert w.antsThatStillExist() == 0
        w = World([0,0,-1,1],[-1,1,0,0],"NSEW", debug)
        assert w.antsThatStillExist() == 0
        w = World([0,0,-1,1,0],[-1,1,0,0,0],"NSEWN", debug)
        assert w.antsThatStillExist() == 0
        w = World([0,0,-1,1,0],[-1,1,0,0,0],"NNEWN", debug)
        assert w.antsThatStillExist() == 2
        w = World([0,10,20,30],[0,10,20,30],"NWNE", debug)
        assert w.antsThatStillExist() == 2
        w = World([-10,0,0,10],[0,-10,10,0],"NEWS", debug)
        assert w.antsThatStillExist() == 0
        w = World([-1,-1,-1,0,0,0,1,1,1],[-1,0,1,-1,0,1,-1,0,1],"ESEWNNEWW", debug)
        assert w.antsThatStillExist() == 4
        w = World([4,7,6,2,6,5,7,7,8,4,7,8,8,8,5,4,8,9,1,5,9,3,4,0,0,1,0,7,2,6,9,6,3,0,5,5,1,2,0,4,9,7,7,1,8,1,9,2,7,3],[2,3,0,6,8,4,9,0,5,0,2,4,3,8,1,5,0,7,3,7,0,9,8,1,9,4,7,8,1,1,6,6,6,2,8,5,1,9,0,1,1,1,7,0,2,5,4,7,5,3],"SSNWSWSENSWSESWEWSWSENWNNNESWSWSWWSSWEEWWNWWWNWENN", debug)
        assert w.antsThatStillExist() == 25
        w = World([478,-664,759,434,-405,513,565,-396,311,-174,56,993,251,-341,993,-112,242,129,383,513,-78,-341,-148,129,423,493,434,-405,478,-148,929,251,56,242,929,-78,423,-664,802,251,759,383,-112,-591,-591,-248,660,660,735,493],[-186,98,948,795,289,-678,948,-170,-195,290,-354,-424,289,-157,-166,150,706,-678,684,-294,-234,36,36,-294,-216,-234,427,945,265,-157,265,715,275,715,-186,337,798,-170,427,706,754,961,286,-216,798,286,961,684,-424,337],"WNSNNSSWWWEENWESNSWSWSEWWEWEWWWNWESNSSNNSNNWWWNESE", debug)
        assert w.antsThatStillExist() == 44

        print "Hello World!"
