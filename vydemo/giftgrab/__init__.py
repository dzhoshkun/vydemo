"""GIFT-Grab wrapper for systems where GIFT-Grab is not installed."""
try:
    from pygiftgrab import ColourSpace
    from pygiftgrab import IObserver
    from pygiftgrab import IObservable
    from pygiftgrab import VideoFrame
except ImportError:
    from ._colour_space import ColourSpace
    from ._iobserver import IObserver
    from ._iobservable import IObservable
    from ._video_frame import VideoFrame
