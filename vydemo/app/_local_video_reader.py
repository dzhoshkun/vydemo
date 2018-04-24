import time
import threading
import cv2
from vydemo.giftgrab import (IObservable, VideoFrame, ColourSpace)


class LocalVideoReader(IObservable, threading.Thread):

    def __init__(self, filepath):
        IObservable.__init__(self)
        threading.Thread.__init__(self)
        self.filepath = filepath
        self.video = None
        self.running = False

    def stop(self):
        if self.running:
            self.running = False

    def run(self):
        if self.running:
            return
        self.running = True
        inter_frame_interval = 0.1
        if 'CAP_PROP_FPS' in dir(cv2):
            frame_rate_attribute = cv2.CAP_PROP_FPS
        elif 'cv' in dir(cv2):
            frame_rate_attribute = cv2.cv.CV_CAP_PROP_FPS
        while self.running:
            if self.video is None:
                self.video = cv2.VideoCapture(self.filepath)
                inter_frame_interval = 1.0 / self.video.get(frame_rate_attribute)
            if self.video:
                ret, data = self.video.read()
                if ret:
                    image = VideoFrame(ColourSpace.BGRA, data, data.shape[:2])
                    for observer in self.observers:
                        observer.update(image)
            time.sleep(inter_frame_interval)
        self.video = None
