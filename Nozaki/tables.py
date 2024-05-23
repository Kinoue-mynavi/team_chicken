import sys
from sqlalchemy import Column, String, Integer, Numeric, Date
from database import Base
from database import ENGINE

#テーブル：Holidayの定義
class Stations(Base):
    __tablename__ = 'stations'
    seq = Column('seq', Integer, primary_key = True)
    name = Column('name', String(20))
    kilo = Column('kilo', Numeric(6,2))
    
# テーブル：transportの定義
class transport(Base):
    __tablename__ = 'transport'
    date = Column('date', Date, primary_key = True)
    seq = Column('seq', Integer, primary_key = True)
    departure = Column('departure', String(20) )
    arrival = Column('arrive', String(20))
    via = Column('via', String(40))
    amount = Column('amount', Integer)
    
def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
        main(sys.argv)