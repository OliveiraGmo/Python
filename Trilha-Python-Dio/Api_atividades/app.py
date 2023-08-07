from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades, Usuarios


app = Flask(__name__)
api = Api(app)

class Pessoa(Resource):

    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome':pessoa.nome,
                'idade':pessoa.idade,
                'id':pessoa.id
            }
        except AttributeError:
            response = {
                'status':'error',
                'mensagem':'Pessoa nao encontrada'
            }
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id':pessoa.id,
            'nome':pessoa.nome,
            'idade':pessoa.idade
        }
        return response

api.add_resource(Pessoa, '/pessoa/<string:nome>/')


if __name__ == '__main__':
    app.run(debug=True)