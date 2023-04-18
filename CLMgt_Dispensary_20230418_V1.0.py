if __SKLEARN_SETUP__:
    sys.stderr.write("Partial import of sklearn during the build process.\n")
    # We are not importing the rest of scikit-learn during the build
    # process, as it may not be compiled yet
else:
    # `_distributor_init` allows distributors to run custom init code.
    # For instance, for the Windows wheel, this is used to pre-load the
    # vcomp shared library runtime for OpenMP embedded in the sklearn/.libs
    # sub-folder.
    # It is necessary to do this prior to importing show_versions as the
    # later is linked to the OpenMP runtime to make it possible to introspect
    # it and importing it first would fail if the OpenMP dll cannot be found.
    from . import _distributor_init  # noqa: F401
    from . import __check_build  # noqa: F401
    from .base import clone
    from .utils._show_versions import show_versions

    __all__ = [
        "calibration",
        "cluster",
        "covariance",
        "cross_decomposition",
        "datasets",
        "decomposition",
        "dummy",
        "ensemble",
        "exceptions",
        "experimental",
        "externals",
        "feature_extraction",
        "feature_selection",
        "gaussian_process",
        "inspection",
        "isotonic",
        "kernel_approximation",
        "kernel_ridge",
        "linear_model",
        "manifold",
        "metrics",
        "mixture",
        "model_selection",
        "multiclass",
        "multioutput",
        "naive_bayes",
        "neighbors",
        "neural_network",
        "pipeline",
        "preprocessing",
        "random_projection",
        "semi_supervised",
        "svm",
        "tree",
        "discriminant_analysis",
        "impute",
        "compose",
        # Non-modules:
        "clone",
        "get_config",
        "set_config",
        "config_context",
        "show_versions",
    ]


def setup_module(module):
    """Fixture for the tests to assure globally controllable seeding of RNGs"""

    import numpy as np

    # Check if a random seed exists in the environment, if not create one.
    _random_seed = os.environ.get("SKLEARN_SEED", None)
    if _random_seed is None:
        _random_seed = np.random.uniform() * np.iinfo(np.int32).max
    _random_seed = int(_random_seed)
    print("I: Seeding RNGs with %r" % _random_seed)
    np.random.seed(_random_seed)
    random.seed(_random_seed)
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
