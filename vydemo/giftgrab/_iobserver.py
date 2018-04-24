class IObserver(object):

    def update(self, image):
        raise NotImplementedError
