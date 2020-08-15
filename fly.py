# 导入pygame 和 初始化pygame相关接口 设置屏幕大小
import pygame
pygame.init()
screen = pygame.display.set_mode([1080, 760])
# 设置屏幕的标题
pygame.display.set_caption("fly小飞机")

# 设置游戏窗口的小图标
# 进入ICON的图标搜索网址 找到和程序相符的图标 或者自己喜欢的
# https://www.flaticon.com/

icon = pygame.image.load("project.png")
pygame.display.set_icon(icon)

#添加玩家小飞机在屏幕的下方正中 载入玩家的图片 设置坐标
playerimage=pygame.image.load('player.png')
playerx = 540
playery = 650
#设置 X Y上的改变 变量值
playerx_change = 0
playery_change = 0

#定义玩家函数：使玩家图像显示在X Y 坐标上
def player(x,y):
    screen.blit(playerimage,[x,y])

# 设置游戏循环 和 退出机制
# game 循环

running = True

while running:
    # 设置屏幕的背景颜色
    screen.fill([0, 0, 0])

           

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #playerx += 0.1  #横向坐标增加或减少可以让飞机自动横向运动
    #如果按键keystroke按下 再确定是按的 左还是右 
    #if keystroke is pressed check whether its right or left
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerx_change = -0.3
        if event.key ==pygame.K_RIGHT:
            playerx_change = 0.3  
        if event.key == pygame.K_UP:
            playery_change = -0.3
        if event.key ==pygame.K_DOWN:
            playery_change = 0.3

            
    if event.type == pygame.KEYUP:        
        if event.key == pygame.K_LEFT or event.key ==pygame.K_RIGHT:
            playerx_change = 0  
        if event.key == pygame.K_UP or event.key ==pygame.K_DOWN:
            playery_change = 0             

#调用玩家函数 2个Parameter形参 传入到玩家函数Player 让玩家在屏幕的540 650 左边显示出来 
    playerx += playerx_change
    playery += playery_change   
    player(playerx,playery)
    pygame.display.update()#显示刷新

pygame.quit()
