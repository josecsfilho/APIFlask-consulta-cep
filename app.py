from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


@app.route('/endereco/<cep>', methods=['GET'])
def obter_endereco(cep):
    # Faz uma requisição GET para a API ViaCEP para obter os dados do endereço com base no CEP
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

    if response.status_code == 200:
        # Se a requisição for bem-sucedida (código de status 200), extrai os dados de endereço da resposta
        endereco = response.json()

        # Formata os dados do endereço de acordo com os campos desejados
        endereco_formatado = {
            'bairro': endereco.get('bairro'),
            'cep': endereco.get('cep'),
            'localidade': endereco.get('localidade'),
            'logradouro': endereco.get('logradouro'),
            'uf': endereco.get('uf')
        }

        # Imprime os dados do endereço formatado na tela sem {}
        print("\n".join([f"{key}: {value}" for key, value in endereco_formatado.items()]))

        # Retorna os dados do endereço formatado como resposta da API em formato JSON
        return jsonify(endereco_formatado)
    else:
        # Se a requisição não for bem-sucedida, retorna uma mensagem de erro
        print('CEP não encontrado')
        return jsonify({'error': 'CEP não encontrado'})


if __name__ == '__main__':
    app.run(debug=True)
