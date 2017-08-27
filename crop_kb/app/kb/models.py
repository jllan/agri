from sqlalchemy import Column, String, Integer, Text, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

class Crop(Base):
    __tablename__ = 'crop'

    crop_id = Column(Integer, primary_key=True)
    crop = Column(String(20))


class Ftime(Base):
    __tablename__ = 'ftime'

    ftime_id = Column(Integer, primary_key=True)
    ftime = Column(String(20))


class Ftype(Base):
    __tablename__ = 'ftype'

    ftype_id = Column(Integer, primary_key=True)
    ftype = Column(String(20))


class Farming(Base):
    __tablename__ = 'farming'

    fid = Column(Integer, primary_key=True)
    crop_id = Column(Integer, ForeignKey('crop.crop_id', ondelete="CASCADE"))
    ftime_id = Column(Integer, ForeignKey('ftime.ftime_id', ondelete="CASCADE"))
    ftype_id = Column(Integer, ForeignKey('ftype.ftype_id', ondelete="CASCADE"))
    fdetail = Column(Text)


# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:cbj@localhost:3306/farm_operation')
# 创建DBSession类型:
Session = sessionmaker(bind=engine)



def create_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)


from contextlib import contextmanager

@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

if __name__ == '__main__':
    # drop_db()
    create_db()