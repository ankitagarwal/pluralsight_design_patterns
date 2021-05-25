from abc import ABCMeta, abstractmethod


class AbsObserver(metaclass=ABCMeta):
    _sub = None

    def __init__(self, sub):
        sub.attach(self)
        self._sub = sub

    @abstractmethod
    def update(self, value):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._sub.detach(self)
