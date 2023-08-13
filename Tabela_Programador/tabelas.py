from sqlalchemy import Column , create_engine, Integer, String , ForeignKey
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker, relationship

engine = create_engine('sqlite:///tabelas.db')
db_session = scoped_session(sessionmaker(autocommit=False,bind=engine))


Base = declarative_base()
Base.query = db_session.query_property()

class Programador(Base):
    __tablename__='programador'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)
    email = Column(String(60))

    def __repr__(self):
        return f'<Programador {self.nome}, tem {self.idade} anos de idade, seu email é : {self.email}>'

    def save(self):
        db_session.add(self)
        db_session.commit()
class Habilidades(Base):
    __tablename__ = 'Habilidades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40))
    habilidades = Column(String(80))
    pessoa_id = Column(Integer,ForeignKey('programador.id'))
    pessoa = relationship("Programador")

    def __repr__(self):
        return '<Habilidades {}'.format(self.nome)


def init_db():
    Base.metadata.create_all(bind=engine)
if __name__ =='__main__':
    init_db()

