import os.path
from pkg_resources import resource_filename
from vydemo.gui import (VideoPlayer, App)
from vydemo.giftgrab import ColourSpace
from ._local_video_reader import LocalVideoReader


def main():
    let_the_sun_shine()


def let_the_sun_shine():
    filepath = resource_filename(__name__,
                                 os.path.join('data', 'sunny-river.mp4'))
    video_reader = LocalVideoReader(filepath)
    video_player = VideoPlayer(color=ColourSpace.RGB, size=(480, 720))
    video_reader.attach(video_player)
    video_reader.start()
    App(video_player).run()
    video_reader.stop()
    video_reader.detach(video_player)
