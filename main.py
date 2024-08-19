    ###  بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ ###
from utils import *

p1=Player()
p2=Player()

g = Game(p1,p2)
g.start()
g.loop()
g.end()

