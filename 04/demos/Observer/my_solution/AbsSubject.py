from abc import ABCMeta
from AbsObserver import AbsObserver


class AbsSubject(metaclass=ABCMeta):
    _observers = set()

    def attach(self, obs: AbsObserver):
        if not isinstance(obs, AbsObserver):
            raise Exception("Supplied class is not valid.")
        self._observers |= {obs}

    def detach(self, obs: AbsObserver):
        if not isinstance(obs, AbsObserver):
            raise Exception("Supplied class is not valid.")
        self._observers -= {obs}

    def notify(self, value):
        for obs in self._observers:
            obs.update(value)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Delete observer references for garbage collection.
        self._observers.clear()