from pkg_resources import resource_string


def let_the_sun_shine():
    filepath = resource_string(__name__, 'sunny-river.mp4')
    print('Let the sun shine on {}'.format(filepath))
