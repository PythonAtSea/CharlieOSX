import _thread

from profileHelper import ProfileHelper
from pybricks.parameters import Button, Color
from pybricks.media.ev3dev import Image, ImageFile, Font, SoundFile

from UI.UIObject import UIObject
from UI.tools import Menu, Box


class UIManager:
    def __init__(self, config, settings, brick, logger):
        # needed Stuff
        #logger.info(self, 'Starting UI initialisation')
        self.__config = config
        self.__settings = settings
        self.__click = 'assets/media/click.wav'
        self.__confirm = 'assets/media/confirm.wav'
        self.brick = brick
        self.logger = logger
        #self.profileHelper = ProfileHelper(self.logger, self.__config)
        self.__sound_lock = _thread.allocate_lock()
        #self.logger.info(self, 'UI initialized')

        # UI Stuff
        # self.UIObjects = []
        # self.UIIcons = [
        #     "./icons/1.png",
        #     "./icons/2.png",
        #     "./icons/3.png",
        #     "./icons/4.png",
        #     "./icons/5.png",
        # ]

        # for i in range(len(self.UIIcons)):
        #     self.addObject(UIIcon(self.brick, self.logger, i, self.UIIcons[i]))
        mainMenu = Menu('sidebar')
        #y = UIObject(self.brick, x, 'img', (0, 0), 'assets/graphics/menus/programmingMainMenu.png')
        mainMenu.addObject(UIObject('programming', self.brick, Box(0, 5, 20, 20), 'img', (0, 0), 'assets/graphics/menus/programmingMainMenu.png'))
        mainMenu.addObject(UIObject('testing', self.brick, Box(0, 25, 20, 20), 'img', (0, 0), 'assets/graphics/menus/testingMainMenu.png'))
        mainMenu.addObject(UIObject('remote', self.brick, Box(0, 45, 20, 20), 'img', (0, 0), 'assets/graphics/menus/remoteMainMenu.png'))
        mainMenu.addObject(UIObject('competition', self.brick, Box(0, 65, 20, 20), 'img', (0, 0), 'assets/graphics/menus/competitionMainMenu.png'))
        mainMenu.addObject(UIObject('settings', self.brick, Box(0, 85, 20, 20), 'img', (0, 0), 'assets/graphics/menus/settingsMainMenu.png'))
        print(mainMenu.rasterize())
        mainMenu.draw()

        testSubmenu = Menu('normal')
        testSubmenu.addObject(UIObject('testObject1', self.brick, Box(0, 85, 20, 20), 'img', (0, 0), 'assets/graphics/menus/settingsMainMenu.png'))
        testSubmenu.addObject(UIObject('testObject2', self.brick, Box(0, 5, 20, 20), 'img', (0, 0), 'assets/graphics/menus/programmingMainMenu.png'))
        testSubmenu.addObject(UIObject('testObject3', self.brick, Box(40, 5, 20, 20), 'img', (0, 0), 'assets/graphics/menus/programmingMainMenu.png'))
        print(testSubmenu.rasterize())


    def __sound(self, file):
        '''
        This private method is used for playing a sound in a separate thread so that other code can be executed simultaneously.

        Args:
            file (str / SoundFile): The path to the soundfile to play
        '''
        def __playSoundFile(soundFile):
            with self.__sound_lock:
                self.brick.speaker.play_file(soundFile)
        _thread.start_new_thread(__playSoundFile, (file, ))

    def addObject(self, UIObject):
        self.UIObjects.append(UIObject)

    def draw(self):
        for UIObject in self.UIObjects:
            UIObject.draw()
