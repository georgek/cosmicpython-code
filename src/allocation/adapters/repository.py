import abc
from allocation.domain import model

from sqlalchemy.exc import NoResultFound


class AbstractRepository(abc.ABC):
    def add(self, product: model.Product):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, sku) -> model.Product:
        raise NotImplementedError

    @abc.abstractmethod
    def list(self) -> list[model.Product]:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, product):
        self.session.add(product)

    def get(self, sku):
        try:
            return self.session.query(model.Product).filter_by(sku=sku).one()
        except NoResultFound:
            return None

    def list(self):
        return self.session.query(model.Product).all()
