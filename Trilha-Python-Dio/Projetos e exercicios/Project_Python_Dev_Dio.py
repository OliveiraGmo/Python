"""
    Exercicio integrando SQlite e MongoDB, trilha python developer dio

"""
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

Base = declarative_base()


class Cliente(Base):
    """
        Esta classe representa a tabela Cliente dentro
        do SQlite.
    """
    __tablename__ = "Cliente"
    # atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    cpf = Column(Integer)

    conta = relationship(
        "Conta", back_populates="cliente", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Cliente(id={self.id}, name={self.name}, fullname={self.fullname})"


class Conta(Base):
    __tablename__ = "conta"
    id = Column(Integer, primary_key=True)
    nro_conta = Column(Integer(), nullable=False)
    cliente_id = Column(Integer, ForeignKey("Cliente.id"), nullable=False)

    cliente = relationship("Cliente", back_populates="conta")

    def __repr__(self):
        return f"Conta(id={self.id}, nro_conta={self.nro_conta})"

# conexão com o banco de dados
engine = create_engine("sqlite://")

# criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

with Session(engine) as session:
    janja = Cliente(
        name='Joaquina',
        fullname='Joaquina Damasceno',
        conta=[Conta(nro_conta='12345')]
    )

    jair = Cliente(
        name='jair',
        fullname='Jair de Jesus',
        conta=[Conta(nro_conta='67891'),
               Conta(nro_conta='12541'),
               Conta(nro_conta='21243')]
    )

    joaquim = Cliente(name='Joaquim',
                      fullname='Joaquim Miguel',
                      conta=[Conta(nro_conta='2233')]
                      )


    session.add_all([janja, jair, joaquim])

    session.commit()

stmt = select(Cliente).where(Cliente.name.in_(["Joaquina", 'Joaquim']))
print('Recuperando usuários a partir de condição de filtragem')
for cliente in session.scalars(stmt):
    print(cliente)


stmt_conta = select(Conta).where(Conta.cliente_id.in_([2]))
print('\nRecuperando os numeros de contas de Jair')
for conta in session.scalars(stmt_conta):
    print(conta)


stmt_order = select(Cliente).order_by(Cliente.fullname.desc())
print("\nRecuperando info de maneira ordenada")
for result in session.scalars(stmt_order):
    print(result)

stmt_join = select(Cliente.fullname, Conta.nro_conta).join_from(Conta, Cliente)
print("\n")
for result in session.scalars(stmt_join):
    print(result)

connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
print("\nExecutando statement a partir da connection")
for result in results:
    print(result)

stmt_count = select(func.count('*')).select_from(Cliente)
print('\nTotal de instâncias em Clientes')
for result in session.scalars(stmt_count):
    print(result)


# encerrando a session
session.close()
