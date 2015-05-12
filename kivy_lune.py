# -*- coding: utf-8 -*-

import sys
import signal

import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

from models.settings.user_settings import UserSettings
from models.library import Library
from models.song_queue import SongQueue
from views.main_window import MainWindow
from views.player import Player
from controllers.arg_parser import argParser
from models.gui_operation_queue import GuiOperationQueue

class luneApp(App):

    def goto_settings(self, event):
        self.transition.direction = 'left'
        self.screen_m.current = 'settings'

    def goto_main(self, event):
        self.transition.direction = 'right'
        self.screen_m.current = 'main'

    def build(self):
        self.transition = SlideTransition(duration=.35)
        self.screen_m = ScreenManager(transition=self.transition)

        main_screen = Screen(name="main")

        layout = BoxLayout(orientation="vertical")
        layout.add_widget(Label(text="main"))
        layout.add_widget(Button(text="settings",
                                 on_press=self.goto_settings))

        main_screen.add_widget(layout)
        self.screen_m.add_widget(main_screen)

        settings_screen = Screen(name="settings")

        layout2 = BoxLayout(orientation="vertical")
        layout2.add_widget(Label(text="settings"))
        layout2.add_widget(Button(text="back to main",
                                  on_press=self.goto_main))

        settings_screen.add_widget(layout2)
        self.screen_m.add_widget(settings_screen)

        return self.screen_m


def main():
    '''
    app = QtGui.QApplication(sys.argv)

    signal.signal(signal.SIGINT, signal.SIG_DFL)
    '''
    operation_queue = GuiOperationQueue()

    library = Library()
    settings = UserSettings(operation_queue, library)
    player = Player()

    '''if len(sys.argv) > 1:
        argsongs = argParser.get_queue(sys.argv)
        player.setQueue(SongQueue(argsongs))
        player.play()

    if sys.platform == 'win32':
        import ctypes
        myappid = 'Lune.Atlas'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    view = MainWindow(library, player, settings, operation_queue)
    view.show()


    app.exec_()
    '''

if __name__ == '__main__':
    luneApp().run()
    #main()
