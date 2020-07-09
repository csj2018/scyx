from main import *
player = Player()
player.pos_init()
eyesight = cal_range(player,es)
eyesight.count('树')
print('视野里一共有'+str(eyesight.count('树'))+'颗树')
controlrange = cal_range(player,3)
print('身边里一共有'+str(controlrange.count('树'))+'颗树')