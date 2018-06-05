from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import DateTime

class Items(Base):
    """
    Items table
    """
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    quantity = Column(Integer)
    description = Column(String(256))
    date_added = Column(DateTime())

    """ String representation of an item
    """
    def __repr__(self):
        return '    '.join(['ID: ', str(self.id), 'Name: ', str(self.name), 'Qty: ', str(self.quantity), 'Descr: ', str(self.description)])
