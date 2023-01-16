from abc import ABC, abstractmethod


class Importer(ABC):
    @abstractmethod
    def importer_data(self, path):
        raise NotImplementedError
