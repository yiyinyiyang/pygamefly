#导入pygame 和 初始化pygame相关接口 设置屏幕大小
import pygame
pygame.init()
screen=pygame.display.set_mode([1080,760])
#设置屏幕的标题
pygame.display.set_caption("小飞机")

#设置游戏窗口的小图标
#进入ICON的图标搜索网址 找到和程序相符的图标 或者自己喜欢的
#https://www.flaticon.com/

icon=pygame.image.load('project.png')
pygame.display.set_icon(icon)

#添加玩家小飞机在屏幕的下方正中
playerimage=pygame.image.load('player.png')
playerx = 540
playery = 650

#定义玩家函数
def player(x,y):
    screen.blit(playerimage,[x,y])

#设置游戏循环 和 退出机制
#game 循环

running = True

while running:
    # 设置屏幕的背景颜色
    screen.fill([0, 0, 0])
    playerx += 0.1  #横向坐标增加或减少可以让飞机自动横向运动
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False


    player(playerx,playery)
    pygame.display.update()

pygame.quit()
