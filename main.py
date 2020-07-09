import random

def randplus(n):
    r = random.randint(0,n-1)
    return r
def randcoord():
    global x,y,z
    x = randplus(xmax)
    y = randplus(ymax)
    z = randplus(zmax)

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
    def pos_init(self):
        self.x = randplus(xmax)
        self.y = randplus(ymax)
        self.z = randplus(zmax)

#生成世界坐标
xmax = 200
ymax = 200
zmax = 60
coord =[]
for x in range(xmax):
    coord.append([])
    for y in range(ymax):
        coord[x].append([])
        for z in range(zmax):
            coord[x][y].append('')
for i in range(100000):
    randcoord()
    coord[x][y][z] = '树'

#角色坐标
# pos = []
# for i in range(3):
#     x = randplus(xmax)
#     y = randplus(ymax)
#     z = randplus(zmax)
#     pos.append([x,y,z])

#视野8
es = 8
def cal_range(player,long):
    range_temp = []
    xl = player.x - long
    yl = player.y - long
    zl = player.z - long
    xh = player.x + long
    yh = player.y + long
    zh = player.z + long
    if xl < 0:
        xl = 0
    if xh > xmax:
        xh = xmax
    if yl - long < 0:
        yl = 0
    if yh + long > ymax:
        yh = ymax
    if zl - long < 0:
        zl = 0
    if zh + long > zmax:
        zh = zmax
    for x in range(xl, xh):
        for y in range(yl, yh):
            for z in range(zl, zh):
                if coord[x][y][z] != '':
                    range_temp.append(coord[x][y][z])
    return range_temp

