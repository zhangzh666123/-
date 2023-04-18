1import pygame,sys,time,random
  2from pygame.locals import *
  3# 定义颜色变量
  4redColour = pygame.Color(255,0,0)
  5blackColour = pygame.Color(0,0,0)
  6whiteColour = pygame.Color(255,255,255)
  7greyColour = pygame.Color(150,150,150)
  8def gameOver(playSurface,score):
  9    gameOverFont = pygame.font.SysFont('arial.ttf',54)
 10    gameOverSurf = gameOverFont.render('Game Over!', True, greyColour)
 11    gameOverRect = gameOverSurf.get_rect()
 12    gameOverRect.midtop = (300, 10)
 13    playSurface.blit(gameOverSurf, gameOverRect)
 14    scoreFont = pygame.font.SysFont('arial.ttf',54)
 15    scoreSurf = scoreFont.render('Score:'+str(score), True, greyColour)
 16    scoreRect = scoreSurf.get_rect()
 17    scoreRect.midtop = (300, 50)
 18    playSurface.blit(scoreSurf, scoreRect)
 19    pygame.display.flip()
 20    time.sleep(5)
 21    pygame.quit()
 22    sys.exit()
 23def main():
 24    # 初始化pygame
 25    pygame.init()
 26    fpsClock = pygame.time.Clock()
 27    # 创建pygame显示层
 28    playSurface = pygame.display.set_mode((600,460))
 29    pygame.display.set_caption('Snake Game')
 30    # 初始化变量
 31    snakePosition = [100,100] #贪吃蛇 蛇头的位置
 32    snakeSegments = [[100,100]] #贪吃蛇 蛇的身体，初始为一个单位
 33    raspberryPosition = [300,300] #树莓的初始位置
 34    raspberrySpawned = 1 #树莓的个数为1
 35    direction = 'right' #初始方向为右
 36    changeDirection = direction
 37    score = 0 #初始得分
 38    while True:
 39        # 检测例如按键等pygame事件
 40        for event in pygame.event.get():
 41            if event.type == QUIT:
 42                pygame.quit()
 43                sys.exit()
 44            elif event.type == KEYDOWN:
 45                # 判断键盘事件
 46                if event.key == K_RIGHT or event.key == ord('d'):
 47                    changeDirection = 'right'
 48                if event.key == K_LEFT or event.key == ord('a'):
 49                    changeDirection = 'left'
 50                if event.key == K_UP or event.key == ord('w'):
 51                    changeDirection = 'up'
 52                if event.key == K_DOWN or event.key == ord('s'):
 53                    changeDirection = 'down'
 54                if event.key == K_ESCAPE:
 55                    pygame.event.post(pygame.event.Event(QUIT))
 56        # 判断是否输入了反方向
 57        if changeDirection == 'right' and not direction == 'left':
 58            direction = changeDirection
 59        if changeDirection == 'left' and not direction == 'right':
 60            direction = changeDirection
 61        if changeDirection == 'up' and not direction == 'down':
 62            direction = changeDirection
 63        if changeDirection == 'down' and not direction == 'up':
 64            direction = changeDirection
 65        # 根据方向移动蛇头的坐标
 66        if direction == 'right':
 67            snakePosition[0] += 20
 68        if direction == 'left':
 69            snakePosition[0] -= 20
 70        if direction == 'up':
 71            snakePosition[1] -= 20
 72        if direction == 'down':
 73            snakePosition[1] += 20
 74        # 增加蛇的长度
 75        snakeSegments.insert(0,list(snakePosition))
 76        # 判断是否吃掉了树莓
 77        if snakePosition[0] == raspberryPosition[0] and snakePosition[1] == raspberryPosition[1]:
 78            raspberrySpawned = 0
 79        else:
 80            snakeSegments.pop()
 81        # 如果吃掉树莓，则重新生成树莓
 82        if raspberrySpawned == 0:
 83            x = random.randrange(1,30)
 84            y = random.randrange(1,23)
 85            raspberryPosition = [int(x*20),int(y*20)]
 86            raspberrySpawned = 1
 87            score += 1
 88        # 绘制pygame显示层
 89        playSurface.fill(blackColour)
 90        for position in snakeSegments:
 91            pygame.draw.rect(playSurface,whiteColour,Rect(position[0],position[1],20,20))
 92            pygame.draw.rect(playSurface,redColour,Rect(raspberryPosition[0], raspberryPosition[1],20,20))
 93        # 刷新pygame显示层
 94        pygame.display.flip()
 95        # 判断是否死亡
 96        if snakePosition[0] > 600 or snakePosition[0] < 0:
 97            gameOver(playSurface,score)
 98        if snakePosition[1] > 460 or snakePosition[1] < 0:
 99            gameOver(playSurface,score)
100        for snakeBody in snakeSegments[1:]:
101            if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
102                gameOver(playSurface,score)
103        # 控制游戏速度
104        fpsClock.tick(5)
105
106if __name__ == "__main__":
107    main()
