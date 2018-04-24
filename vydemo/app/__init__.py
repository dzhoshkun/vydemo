import os.path
from pkg_resources import resource_filename


def let_the_sun_shine():
    filepath = resource_filename(__name__,
                                 os.path.join('data', 'sunny-river.mp4'))
    print('Let the sun shine on {}'.format(filepath))
