#  Copyright (c) 2024.
#  702361946@qq.com
#  github.com/702361946

import logging
import os
from datetime import datetime

# 获取当前用户的AppData路径
log_path = os.path.expanduser('~\\AppData')

if os.name == 'nt':
    # windows
    log_path = os.path.join(log_path, 'LocalLow\\702361946\\game_bata\\game.log')
    # windows字体库路径
    # font_path = 'C:\\Windows\\Fonts'
    zh_font = 'C:\\Windows\\Fonts\\simfang.ttf'
else:
    # 鬼知道是什么系统
    log_path = '.\\game.log'

# 目录补全
os.makedirs(os.path.dirname(log_path), exist_ok=True)

if True:
    logging.basicConfig(filename=log_path, filemode='w', level=logging.DEBUG, encoding='UTF-8')
    # 获取root logger
    root_logger = logging.getLogger()
    # 修改root logger的名称
    root_logger.name = 'paths'
    logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    logging.info(log_path)

logging.info('paths ok and exit')
logging.info(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
