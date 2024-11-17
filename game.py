from configure import *

if True:
    root_logger.name = 'game'
    logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def open_game_page():
    pass


def game_page():
    pass


def exit_game_page():
    logging.info('user exit')

    pygame_button('exit_yes', 0, 180, 320, 180, png = 'exit_yes', _def=lambda: sys_exit('user exit yes'))
    pygame_button('exit_no', 320, 180, 320, 180, png = 'exit_no')
    page_buttons = [
        'exit_yes',
        'exit_no'
    ]

    pygame_png('exit_why', 0, 0)
    page_png = ['exit_why']

    while_open = True
    while while_open:
        for event in pygame.event.get():
            event_type = event.type
            if event_type == pygame.QUIT:
                sys_exit('User Forced Exit')

            elif event_type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                button = event.button
                if button == 1:
                    for key in page_buttons:
                        if buttons[key]['rect'].collidepoint(pos):
                            if buttons[key]['def']:
                                buttons[key]['def']()
                            while_open = False

        window.fill(colors['#ffffff'])

        if True:
            for png in page_png:
                window.blit(pngs[png]['png'], (pngs[png]['x'], pngs[png]['y']))

            for key in page_buttons:
                _dict = buttons[key]
                if _dict['png']:
                    window.blit(_dict['png'], (buttons[key]['rect'].topleft))

        pygame.display.flip()


if __name__ == "__main__":
    # 测试时应单独行注释
    _game: list = [
        # lambda : open_game_page(),
        # lambda : game_page(),
        # lambda : exit_game_page()
    ]
    _open: bool = True
    
    for _def in _game:
        if _open:
            _def()

        else:
            break

    logging.info('game exit')
    logging.info(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
