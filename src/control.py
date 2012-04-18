#!/usr/bin/env python
import ConfigParser
import kivy
import projector
import sys

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.logger import Logger
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget


class ProjectorControlApp(App):
    """Main application to control projectors."""
    title = 'Projector Control'

    def parseConfiguration(self):
        """Looks for and parses a configuration file detailing the projectors
            available."""
        conf = ConfigParser.ConfigParser()
        try:
            conf.read('./projectors.ini')
            self.numProj = conf.getint('config', 'projector_count')
            self.proj = dict()
            for section in conf.sections():
                if section == 'config':
                    pass
                else:
                    id_ = conf.getint(section, 'id')
                    name = conf.get(section, 'name')
                    port = conf.get(section, 'port')
                    self.proj[id_] = {'name': name, 'port': port}
        except ConfigParser.Error:
            sys.stdout.write('Could not load configuration file!\n')
            sys.exit(1)

    def build(self):
        self.widgets = dict()
        self.parseConfiguration()
        parent = Widget()
        layout = GridLayout(cols=self.numProj,
                            size=(self.numProj * 100, 500),
                            row_default_height=10)
        for id_ in xrange(self.numProj):
            self.widgets[id_] = dict()
            self.widgets[id_]['lbl'] = Label(text=self.proj[id_]['name'],
                                             size=(100,25),
                                             size_hint_y=None)
            layout.add_widget(self.widgets[id_]['lbl'])
        for id_ in xrange(self.numProj):
            self.widgets[id_]['pwr'] = ToggleButton(text='Off',
                                                    size=(100, 25),
                                                    size_hint_y=None)
            layout.add_widget(self.widgets[id_]['pwr'])
        for id_ in xrange(self.numProj):
            self.widgets[id_]['hdmi'] = ToggleButton(text='HDMI',
                                                     state='down',
                                                     size=(100, 25),
                                                     size_hint_y=None,
                                                     group='video%s' % id_)
            layout.add_widget(self.widgets[id_]['hdmi'])
        for id_ in xrange(self.numProj):
            self.widgets[id_]['vga'] = ToggleButton(text='VGA',
                                                    state='normal',
                                                    size=(100, 25),
                                                    size_hint_y=None,
                                                    group='video%s' % id_)
            layout.add_widget(self.widgets[id_]['vga'])            
        parent.add_widget(layout)
        return parent


if __name__ == '__main__':
    ProjectorControlApp().run()

