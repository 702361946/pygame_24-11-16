import sys

import pygame

from paths import *

if True:
    root_logger.name = 'configure'
    logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# 初始化自定义配置
if True:
    def sys_exit(message: str = ''):
        logging.info(f'sys_exit\\message:{message}')
        logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        sys.exit()

# 初始化pygame
if True:
    pygame.init()
    pygame.font.init()

    window = pygame.display.set_mode((640, 360))

    pygame.display.set_caption('game_bata')

    game_fps = 60
    pygame.time.Clock().tick(game_fps)

    # game_ico = pygame.image.load('pngs\\game.ico')
    # pygame.display.set_icon(game_ico)

    colors: dict = {
        '#000000': (0, 0, 0),
        '#ffffff': (255, 255, 255)
    }

    buttons: dict = {}
    """
    'name': {
        'rect': pygame.Rect,
        'color': (int, int, int),
        'png': pygame.Surface & None
    }
    """

    fonts: dict = {
        '12': pygame.font.Font(None, 12),
        '24': pygame.font.Font(None, 24),
        '36': pygame.font.Font(None, 36),
        '48': pygame.font.Font(None, 48),
        '60': pygame.font.Font(None, 60),
        'zh-12': pygame.font.Font(zh_font, 12),
        'zh-24': pygame.font.Font(zh_font, 24),
        'zh-36': pygame.font.Font(zh_font, 36),
        'zh-48': pygame.font.Font(zh_font, 48),
        'zh-60': pygame.font.Font(zh_font, 60)
    }

    pngs: dict = {}
    """
    'name': {
        'png': 这是图片
    }
    """

    def exit_pygame():
        logging.info('exit pygame')
        logging.info(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
        pygame.quit()

    def pygame_button(
            name: str,
            x: int,
            y: int,
            w: int,
            h: int,
            color: str = '#ffffff',
            png: str | None = None,
            _def = None
    ) -> None:
        """
        name: button名
        color: 应为16进制颜色,且要加#
        png: 应为图片名
        _def: 应lambda后传入
        """
        logging.info(f'button:{name}\\x{x}\\y{y}\\w{w}\\h{h}')
        buttons[name] = {
            'rect': pygame.Rect(x, y, w, h),
            'color': colors[color],
            'def': _def
        }
        if png:
            logging.info(f'png:{png}')
            buttons[name]['png'] = pygame.image.load(f'pngs\\{png}.png')

        else:
            logging.info('png:None')
            buttons[name]['png'] = None

    def pygame_png(
            png_name: str,
            x: int,
            y: int,
            as_name: str = None
    ) -> None:
        """
        用以加载图像并保存至pngs字典
        可以提供as_name来易名字典的key
        """
        if as_name:
            dict_name = as_name
        else:
            dict_name = png_name

        logging.info(f'png\\name:{dict_name}\\png:{png_name}\\x{x}\\y{y}')
        pngs[dict_name] = {
            'png': pygame.image.load(f'pngs\\{png_name}.png'),
            'x': x,
            'y': y
        }


logging.info('configure ok and exit')
logging.info(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
