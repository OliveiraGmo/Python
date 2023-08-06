from tabelas import Programador,Habilidades

def cadastro():
    dev = Programador(nome='Lucas',id=18,idade=37,email='lucas@teste.com')
    dev.save()
    print(dev)

def consulta_dev():
    dev = Programador.query.all()
    filtro = input("Digite o numero do id que deseja buscar:")
    dev = Programador.query.filter_by(id=filtro).first()
    if dev == None:
        while Programador.query.filter_by(id=filtro).first() == None:
            filtro = int(input("Id não encontrado digite novamente:"))
    dev = Programador.query.filter_by(id=filtro).first()
    print(dev)


if __name__ == '__main__':
    #cadastro()
    consulta_dev()