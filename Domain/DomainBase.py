from abc import ABC, abstractmethod


class DomainBase(ABC):
    def __init__(self):
        pass

    def get_by_id(self, id):
        pass

    # @abstractmethod
    # def get_all(self):
    #     pass

    @abstractmethod
    def insert(self, item):
        pass

    # @abstractmethod
    # def delete(self, item):
    #     pass

    @abstractmethod
    def update(self, item):
        pass