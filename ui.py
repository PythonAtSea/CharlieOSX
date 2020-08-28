import _thread
import time
import json
from profileHelper import ProfileHelper
from pybricks.parameters import Button, Color
from pybricks.media.ev3dev import Image, ImageFile, Font, SoundFile


class UI:
    def __init__(self, config, settings, brick, logger, settingsPath):
        logger.info(self, 'Starting UI initialisation')
        self.__config = config
        self.__settings = settings
        self.__settingsPath = settingsPath
        self.__click = 'assets/media/click.wav'
        self.__confirm = 'assets/media/confirm.wav'
        self.brick = brick
        self.logger = logger
        self.profileHelper = ProfileHelper(self.logger, self.__config)
        self.__sound_lock = _thread.allocate_lock()
        self.logger.info(self, 'UI initialized')
    # TODO

    def __repr__(self):
        return "TODO"
    # TODO

    def __str__(self):
        return "UI"

    def __sound(self, file):
        def __playSoundFile(soundFile):
            with self.__sound_lock:
                self.brick.speaker.play_file(soundFile)
        _thread.start_new_thread(__playSoundFile, (file, ))

    def mainLoop(self):
        self.menuState, self.position, self.oldPos = 0, 0, 0
        self.selected = False
        self.dataCache = []
        self.toAnimate = [10, 20, 30, 40, 50]
        loop, self.selected = True, False
        self.drawMenu(int(self.menuState))
        keys = list(self.__settings['options'].keys())
        self.__storeSettings(self.__settings, self.__settingsPath)
        while loop:
<<<<<<< HEAD
            #
            #
            # Would refactor if statements into different functions -> code mode readable
            #
            #
            if menuState == 10:
                if len(self.__config['profileNames']) > 99:
                    logger.error(
                        self, 'Maximum number of runs exceeded. Please lower your number of runs to a maximum of 99', '')
                    menuState = menuState / 10

            elif menuState > 100 and menuState < 200:
                pass

            elif menuState == 50:  # settings Menu
                if Button.UP in self.brick.buttons.pressed() and selected:
                    if self.__settings['options'][keys[position]] < self.__settings['values']['max'][keys[position]]:
                        self.__settings['options'][keys[position]] += 1
                    elif self.__settings['options'][keys[position]] == self.__settings['values']['max'][keys[position]]:
                        self.__settings['options'][keys[position]
                                                   ] = self.__settings['values']['min'][keys[position]]
                    self.__sound(self.__click)
                    self.drawSettings(position, self.__settings, selected)
                if Button.DOWN in self.brick.buttons.pressed() and selected:
                    if self.__settings['options'][keys[position]] > self.__settings['values']['min'][keys[position]]:
                        self.__settings['options'][keys[position]] -= 1
                    elif self.__settings['options'][keys[position]] == self.__settings['values']['min'][keys[position]]:
                        self.__settings['options'][keys[position]
                                                   ] = self.__settings['values']['max'][keys[position]]
=======
            if self.menuState == 10:
                if len(self.__config['profileNames']) > 99:
                    logger.error(self, 'Maximum of runs exceeded. Please lower your number of runs to a maximum of 99', '')
                    self.menuState = self.menuState / 10
                
            elif self.menuState > 100 and self.menuState < 200:
                if Button.CENTER in self.brick.buttons.pressed():
                    self.logger.debug(self, 'Center button pressed from %s' % self.selected)
                    if self.selected:
                        self.profileHelper.setProfileData(self.__config['profileNames'][menuState - 100], self.dataCache)
                    self.selected = not self.selected
                    self.drawMenu(menuState, position=self.position, selected=self.selected)
                    time.sleep(0.3)

            elif self.menuState == 50: #settings Menu
                if Button.UP in self.brick.buttons.pressed() and selected:
                    if self.__settings['options'][keys[self.position]] < self.__settings['values']['max'][keys[self.position]]:
                        self.__settings['options'][keys[self.position]] += 1
                    elif self.__settings['options'][keys[self.position]] == self.__settings['values']['max'][keys[self.position]]:
                        self.__settings['options'][keys[self.position]] = self.__settings['values']['min'][keys[self.position]]
                    self.__sound(self.__click)
                    self.drawSettings(self.position, self.__settings, self.selected)
                if Button.DOWN in self.brick.buttons.pressed() and self.selected:
                    if self.__settings['options'][keys[self.position]] > self.__settings['values']['min'][keys[self.position]]:
                        self.__settings['options'][keys[self.position]] -= 1
                    elif self.__settings['options'][keys[self.position]] == self.__settings['values']['min'][keys[self.position]]:
                        self.__settings['options'][keys[self.position]] = self.__settings['values']['max'][keys[self.position]]
>>>>>>> 394fd1dbca5130a236ef9750288d293b97f4c709
                    self.__sound('assets/media/click.wav')
                    self.drawSettings(self.position, self.__settings, self.selected)
                if Button.CENTER in self.brick.buttons.pressed():
<<<<<<< HEAD
                    self.logger.debug(
                        self, 'Center button pressed from %s' % selected)
                    if selected:
                        self.__storeSettings(
                            self.__settings, self.__settingsPath)
                        self.__applySettings(self.__settings)
                    selected = not selected
                    self.drawMenu(menuState, position=position,
                                  selected=selected)
                    time.sleep(0.3)

            if Button.RIGHT in self.brick.buttons.pressed() and not selected:
                self.logger.debug(
                    self, 'Right button triggered at %s' % menuState)
                menuState = menuState * 10
                if menuState in self.toAnimate:
                    self.__sound(self.__confirm)
                    time.sleep(0.08)
                    position = 0
                    self.animate(menuState, True)
                if menuState == 100:
                    self.__sound(self.__click)
                    menuState += position + 1
                else:
                    self.__sound(self.__click)
                self.drawMenu(menuState, position=position, selected=selected)
                time.sleep(0.4)

            if Button.LEFT in self.brick.buttons.pressed() and not selected:
                self.logger.debug(
                    self, 'Left button triggered at %s' % menuState)
                if menuState in self.toAnimate:
                    self.__sound(self.__confirm)
                    time.sleep(0.08)
                    self.animate(menuState, False)
                elif menuState > 100 and menuState < 200:
                    self.__sound(self.__click)
                    menuState = 100
                else:
                    self.__sound(self.__click)
                menuState = int(menuState / 10)
                self.drawMenu(menuState, position=position, selected=selected)
                time.sleep(0.4)

            if Button.UP in self.brick.buttons.pressed() and not selected:
                self.logger.debug(
                    self, 'Up button triggered at %s with position of %s' % (menuState, position))
                self.__sound(self.__click)
                if menuState == 50 and position == 0:
                    position = len(self.__settings['options']) - 1
                elif menuState == 50:
                    position -= 1
                elif (menuState == 10 or (menuState > 100 and menuState < 200)) and position == 0:
                    position = len(self.__config['profileNames']) - 1
                elif menuState == 10 or (menuState > 100 and menuState < 200):
                    position -= 1
                elif menuState in [0, 1]:
                    menuState = 5
                else:
                    menuState -= 1
                self.drawMenu(menuState, position=position, selected=selected)
                time.sleep(0.3)

            if Button.DOWN in self.brick.buttons.pressed() and not selected:
                self.logger.debug(
                    self, 'Down button triggered at %s with position of %s' % (menuState, position))
                self.__sound(self.__click)
                if menuState == 50 and position == len(self.__settings['options']) - 1:
                    position = 0
                elif menuState == 50:
                    position += 1
                elif (menuState == 10 or (menuState > 100 and menuState < 200)) and position == len(self.__config['profileNames']) - 1:
                    position = 0
                elif menuState == 10 or (menuState > 100 and menuState < 200):
                    position += 1
                elif menuState in [0, 5]:
                    menuState = 1
                else:
                    menuState += 1
                self.drawMenu(menuState, position=position, selected=selected)
                time.sleep(0.3)
=======
                    self.logger.debug(self, 'Center button pressed from %s' % self.selected)
                    if self.selected:
                        self.__storeSettings(self.__settings, self.__settingsPath)
                        self.__applySettings(self.__settings)
                    self.selected = not self.selected
                    self.drawMenu(self.menuState, position=self.position, selected=self.selected)
                    time.sleep(0.3)
            
            self._buttonActions()
>>>>>>> 394fd1dbca5130a236ef9750288d293b97f4c709

            if self.logger.getScreenRefreshNeeded() == 1:
                self.logger.setScreenRefreshNeeded(0)
                self.menuState = self.menuState / 10

    def drawMenu(self, menuState, **kwargs):
        menus = {0: 'assets/graphics/menus/mainMenu.png',
                 1: 'assets/graphics/menus/programmingMainMenu.png',
                 2: 'assets/graphics/menus/testingMainMenu.png',
                 3: 'assets/graphics/menus/remoteMainMenu.png',
                 4: 'assets/graphics/menus/competitionMainMenu.png',
                 5: 'assets/graphics/menus/settingsMainMenu.png'
                 }
        try:
            if menuState in range(0, 6):
                self.brick.screen.draw_image(
                    0, 0, menus[menuState], transparent=Color.RED)
            elif menuState == 10:
                self.drawList(kwargs['position'],
                              self.__config['profileNames'])
            elif menuState == 50:
                self.drawSettings(kwargs['position'],
                                  self.__settings, kwargs['selected'])
            elif menuState > 100 and menuState < 200:
                self.drawExtendableList(kwargs['position'], self.profileHelper.getProfileData(
                    self.__config['profileNames'][menuState - 100]))
        except Exception as exception:
            self.logger.error(self, "Could not draw menu: %s:" %
                              type(exception).__name__, exception)

    def drawScrollBar(self, totalLength, pos):
        self.brick.screen.draw_box(
            171, 25, 177, 127, r=2, fill=False, color=Color.BLACK)
        self.brick.screen.draw_box(
            172, 26, 176, 126, r=2, fill=True, color=Color.WHITE)
        self.brick.screen.draw_box(173, 27 + 102 / totalLength * pos, 175,
                                   23 + 102 / totalLength * (pos + 1), r=1, fill=True, color=Color.BLACK)

    def drawSettings(self, pos, settings, selected):
        def drawOptions(value, *args):
            '''Subfunction that draws the 5 current options on the screen'''
            for i in range(5):
                if value + i == pos:
                    if selected:
                        self.brick.screen.draw_box(
                            26, 29 + i * 20, 168, 46 + i * 20, r=3, fill=True, color=Color.BLACK)
                        self.brick.screen.draw_text(29, 30 + i * 20, '%s: %s' % (keys[value + i], settings['options'][keys[value + i]]), text_color=Color.WHITE, background_color=None) if settings['types'][keys[value + i]] == 'int' else self.brick.screen.draw_text(
                            29, 30 + i * 20, '%s: %s' % (keys[value + i], bool(settings['options'][keys[value + i]])), text_color=Color.WHITE, background_color=None)
                    else:
                        self.brick.screen.draw_box(
                            26, 29 + i * 20, 168, 46 + i * 20, r=3, fill=True, color=Color.WHITE)
                        self.brick.screen.draw_box(
                            26, 29 + i * 20, 168, 46 + i * 20, r=3, fill=False, color=Color.BLACK)
                        self.brick.screen.draw_text(29, 30 + i * 20, '%s: %s' % (keys[value + i], settings['options'][keys[value + i]]), text_color=Color.BLACK, background_color=None) if settings['types'][keys[value + i]] == 'int' else self.brick.screen.draw_text(
                            29, 30 + i * 20, '%s: %s' % (keys[value + i], bool(settings['options'][keys[value + i]])), text_color=Color.BLACK, background_color=None)
                else:
                    self.brick.screen.draw_box(
                        26, 29 + i * 20, 170, 46 + i * 20, fill=True, color=Color.WHITE)
                    self.brick.screen.draw_text(29, 30 + i * 20, '%s: %s' % (keys[value + i], settings['options'][keys[value + i]]), text_color=Color.BLACK, background_color=Color.WHITE) if settings['types'][keys[value + i]
                                                                                                                                                                                                                ] == 'int' else self.brick.screen.draw_text(29, 30 + i * 20, '%s: %s' % (keys[value + i], bool(settings['options'][keys[value + i]])), text_color=Color.BLACK, background_color=Color.WHITE)

        keys = list(settings['options'].keys())
        self.brick.screen.set_font(Font(family='arial', size=13))

        self.drawScrollBar(len(settings['options']), pos)

        if pos > 1 and pos < (len(settings['options']) - 2):
            drawOptions(pos - 2)
        elif pos == 0:
            drawOptions(pos)
        elif pos == 1:
            drawOptions(pos - 1)
        elif pos == len(settings['options']) - 2:
            drawOptions(pos - 3)
        elif pos == len(settings['options']) - 1:
            drawOptions(pos - 4)

    def animate(self, state, direction):
        menus = {10: 'mainProgram',
                 20: 'mainTest',
                 30: 'mainRemote',
                 40: 'mainCompetition',
                 50: 'mainSettings'}
        if direction:
            try:
                for i in range(1, 11):
                    self.brick.screen.draw_image(
                        0, 0, 'assets/graphics/animations/%s/%s.png' % (menus[state], i), transparent=Color.RED)
            except Exception as exception:
                self.logger.error(
                    self, "Could not animate menu: ", str(exception))
        else:
            try:
                for i in reversed(range(1, 11)):
                    self.brick.screen.draw_image(
                        0, 0, 'assets/graphics/animations/%s/%s.png' % (menus[state], i), transparent=Color.RED)
            except Exception as exception:
                self.logger.error(
                    self, "Could not animate menu: ", str(exception))

    def drawDictlist(self, pos, dictlist, selected):
        def drawOptions(value, *args):
            '''Subfunction that draws the 5 current options on the screen'''
            for i in range(5):
                if value + i == pos:
                    if selected:
                        self.brick.screen.draw_box(
                            26, 29 + i * 20, 168, 46 + i * 20, r=3, fill=True, color=Color.BLACK)
                        self.brick.screen.draw_text(29, 30 + i * 20, '%s: %s' % (
                            keys[value + i], dictlist[keys[value + i]]), text_color=Color.WHITE, background_color=None)
                    else:
                        self.brick.screen.draw_box(
                            26, 29 + i * 20, 168, 46 + i * 20, r=3, fill=True, color=Color.WHITE)
                        self.brick.screen.draw_box(
                            26, 29 + i * 20, 168, 46 + i * 20, r=3, fill=False, color=Color.BLACK)
                        self.brick.screen.draw_text(29, 30 + i * 20, '%s: %s' % (
                            keys[value + i], dictlist[keys[value + i]]), text_color=Color.BLACK, background_color=None)
                else:
                    self.brick.screen.draw_box(
                        26, 29 + i * 20, 170, 46 + i * 20, fill=True, color=Color.WHITE)
                    self.brick.screen.draw_text(29, 30 + i * 20, '%s: %s' % (
                        keys[value + i], dictlist[keys[value + i]]), text_color=Color.BLACK, background_color=Color.WHITE)

        keys = list(dictlist.keys())
        self.brick.screen.set_font(Font(family='arial', size=13))

        self.drawScrollBar(len(dictlist), pos)

        if pos > 1 and pos < (len(dictlist) - 2):
            drawOptions(pos - 2)
        elif pos == 0:
            drawOptions(pos)
        elif pos == 1:
            drawOptions(pos - 1)
        elif pos == len(dictlist) - 2:
            drawOptions(pos - 3)
        elif pos == len(dictlist) - 1:
            drawOptions(pos - 4)

    def drawList(self, pos, llist):
        def drawOptions(value, *args):
            '''Subfunction that draws the 5 current options on the screen'''
            for i in range(5):
                if value + i == pos:
                    self.brick.screen.draw_box(
                        26, 29 + i * 20, 168, 46 + i * 20, r=3, fill=True, color=Color.WHITE)
                    self.brick.screen.draw_box(
                        26, 29 + i * 20, 168, 46 + i * 20, r=3, fill=False, color=Color.BLACK)
                    self.brick.screen.draw_text(
                        29, 30 + i * 20, llist[value + i], text_color=Color.BLACK, background_color=None)
                else:
                    self.brick.screen.draw_box(
                        26, 29 + i * 20, 170, 46 + i * 20, fill=True, color=Color.WHITE)
                    self.brick.screen.draw_text(
                        29, 30 + i * 20, llist[value + i], text_color=Color.BLACK, background_color=Color.WHITE)

        self.brick.screen.set_font(Font(family='arial', size=13))

        self.drawScrollBar(len(llist), pos)

        if pos > 1 and pos < (len(llist) - 2):
            drawOptions(pos - 2)
        elif pos == 0:
            drawOptions(pos)
        elif pos == 1:
            drawOptions(pos - 1)
        elif pos == len(llist) - 2:
            drawOptions(pos - 3)
        elif pos == len(llist) - 1:
            drawOptions(pos - 4)

    def drawExtendableList(self, pos, llist):
        def drawOptions(value, *args):
            '''Subfunction that draws the 5 current options on the screen'''
            self.brick.screen.draw_box(
                26, 29, 168, 46 + 5 * 20, fill=True, color=Color.WHITE)
            for i in range(5):
                if value + i > len(llist):
                    pass
                elif value + i == pos:
<<<<<<< HEAD
                    # self.brick.screen.draw_box(26, 29 + i * 20, 168, 46 + i * 20, r = 3, fill = True, color = Color.WHITE)
                    self.brick.screen.draw_box(
                        26, 29 + i * 20, 168, 46 + i * 20, r=3, fill=False, color=Color.BLACK)
                    self.brick.screen.draw_text(29, 30 + i * 20, llist[value + i], text_color=Color.BLACK, background_color=None) if (value + i != len(
                        llist)) else self.brick.screen.draw_image(90, 30 + i * 20, 'assets/graphics/misc/plus-button_selected.png', transparent=Color.RED)
                else:
                    # self.brick.screen.draw_box(26, 29 + i * 20, 170, 46 + i * 20, fill = True, color = Color.WHITE)

                    #
                    #
                    # WThat does the if-else-statement do?
                    #
                    #
                    self.brick.screen.draw_text(
                        29, 30 + i * 20, llist[value + i], text_color=Color.BLACK, background_color=Color.WHITE) if (value + i != len(llist)) else self.brick.screen.draw_image(
                        80, 30 + (i - 1) * 20, 'assets/graphics/misc/plus-button.png', transparent=Color.RED)
=======
                    self.brick.screen.draw_box(26, 29 + i * 20, 168, 46 + i * 20, r = 3, fill = False, color = Color.BLACK)
                    self.brick.screen.draw_text(29, 30 + i * 20, llist[value + i], text_color = Color.BLACK, background_color = None) if (value + i != len(llist)) else self.brick.screen.draw_image(90, 30 + i * 20, 'assets/graphics/misc/plus-button_selected.png', transparent = Color.RED)
                else:
                    self.brick.screen.draw_text(29, 30 + i * 20, llist[value + i], text_color = Color.BLACK, background_color = Color.WHITE) if (value + i != len(llist)) else self.brick.screen.draw_image(80, 30 + (i - 1) * 20, 'assets/graphics/misc/plus-button.png', transparent = Color.RED)
                i += 1
>>>>>>> 394fd1dbca5130a236ef9750288d293b97f4c709
        llist.append('')

        self.brick.screen.set_font(Font(family='arial', size=12))

        self.drawScrollBar(len(llist), pos)

        if pos > 1 and pos < (len(llist) - 2):
            drawOptions(pos - 2)
        elif pos == 0:
            drawOptions(pos)
        elif pos == 1:
            drawOptions(pos - 1)
        elif pos == len(llist) - 2:
            drawOptions(pos - 3)
        elif pos == len(llist) - 1:
            drawOptions(pos - 4)
        llist.pop()

    def __storeSettings(self, data, path):
        try:
            with open(path, 'w') as f:
                f.write(json.dumps(data, sort_keys=False))
            self.logger.info(self, 'Successfully stored settings')
        except Exception as exception:
            self.logger.error(
                self, 'Failed to store settings to %s' % path, exception)

    def __applySettings(self, settings):
        self.brick.speaker.set_volume(
            settings['options']['Audio-Volume'] * 0.9, 'Beep')
        self.brick.speaker.set_volume(
            settings['options']['EFX-Volume'] * 0.9, 'PCM')
        self.logger.debug(self, 'Applied settings')

    def _buttonActions(self):
        if not self.selected:
            if Button.RIGHT in self.brick.buttons.pressed():
                self.logger.debug(self, 'Right button triggered at %s' % self.menuState)
                self.menuState = self.menuState * 10
                if self.menuState in self.toAnimate:
                    self.__sound(self.__confirm)
                    time.sleep(0.08)
                    self.position = 0
                    self.animate(self.menuState, True)
                elif self.menuState == 100:
                    self.__sound(self.__click)
                    self.menuState += self.position + 1
                    self.position = 0
                    self.dataCache = self.profileHelper.getProfileData(self.__config['profileNames'][self.menuState - 100])
                else:
                    self.__sound(self.__click)
                self.drawMenu(self.menuState, position=self.position, selected=self.selected)
                time.sleep(0.4)

            if Button.LEFT in self.brick.buttons.pressed():
                self.logger.debug(self, 'Left button triggered at %s' % self.menuState)
                if self.menuState in self.toAnimate:
                    self.__sound(self.__confirm)
                    time.sleep(0.08)
                    self.animate(self.menuState, False)
                elif self.menuState > 100 and self.menuState < 200:
                    self.__sound(self.__click)
                    self.menuState = 100
                else:
                    self.__sound(self.__click)
                self.menuState = int(self.menuState / 10)
                self.drawMenu(self.menuState, position=self.position, selected=self.selected)
                time.sleep(0.4)

            if Button.UP in self.brick.buttons.pressed():
                self.logger.debug(self, 'Up button triggered at %s with position of %s' % (self.menuState, self.position))
                self.__sound(self.__click)
                if self.menuState == 50 and position == 0:
                    self.position = len(self.__settings['options']) - 1
                elif self.menuState == 50:
                    self.position -= 1
                elif (self.menuState == 10 or (self.menuState > 100 and self.menuState < 200)) and self.position == 0:
                    self.position = len(self.__config['profileNames']) - 1
                elif self.menuState == 10 or (self.menuState > 100 and self.menuState < 200):
                    self.position -= 1
                elif self.menuState in [0, 1]:
                    self.menuState = 5
                else:
                    self.menuState -= 1
                self.drawMenu(self.menuState, position=self.position, selected=self.selected)
                time.sleep(0.3)

            if Button.DOWN in self.brick.buttons.pressed():
                self.logger.debug(self, 'Down button triggered at %s with position of %s' % (self.menuState, self.position))
                self.__sound(self.__click)
                if self.menuState == 50 and self.position == len(self.__settings['options']) - 1:
                    self.position = 0
                elif self.menuState == 50:
                    self.position += 1
                elif self.menuState == 10 and self.position == len(self.__config['profileNames']) - 1:
                    self.position = 0
                elif (self.menuState > 100 and self.menuState < 200) and self.position == len(self.profileHelper.getProfileData(self.__config['profileNames'][self.menuState - 100])):
                    self.position = 0
                elif self.menuState == 10 or (self.menuState > 100 and self.menuState < 200):
                    self.position += 1
                elif self.menuState in [0, 5]:
                    self.menuState = 1
                else:
                    self.menuState += 1
                self.drawMenu(self.menuState, position=self.position, selected=self.selected)
                time.sleep(0.3)