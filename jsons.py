#  Copyright (c) 2024.
#  702361946@qq.com
#  github.com/702361946

import logging
from datetime import datetime

import json
from paths import log_path

if True:
    root_logger.name = 'jsons'
    logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def w_json(a, name: str, encoding: str = 'utf-8'):
    logging.info(f'w json\\name:{name}\nw:{a}')
    try:
        with open(f'json\\{name}.json', 'w+', encoding=encoding) as f:
            json.dump(a, f, indent=4, ensure_ascii=False)
            logging.info('ok')

    except Exception as e:
        print(e)
        logging.error(f'\n{e}\n')


def r_json(name: str, encoding: str = 'utf-8'):
    logging.info(f'r json\\{name}')
    try:
        with open(f'json\\{name}.json', 'r+', encoding=encoding) as f:
            a = json.load(f)
            logging.info(f'ok\nr:{a}')
            return a

    except FileNotFoundError:
        logging.error('未找到文件')
        return None

    except Exception as e:
        print(e)
        logging.error(f'\n{e}\n')
        return None


logging.info('json ok and exit')
logging.info(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
