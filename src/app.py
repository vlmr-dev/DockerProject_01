import subprocess
import re
from flask import Flask, render_template

app = Flask(__name__)

def limpar_saida(output):
    linhas = output.splitlines()
    linhas_limpa = [re.sub(r'^#\d+\s*\[.*?\]\s*', '', linha) for linha in linhas if not linha.lstrip().startswith("#")]
    return "\n".join(linhas_limpa)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rodar-docker-compose', methods=['POST'])
def rodar_docker_compose():
    try:
        resultado = subprocess.check_output(
            ['docker-compose', 'up', '--build', '-d'],
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )
        limpo = limpar_saida(resultado)
        return render_template('success.html', sucesso=True, output=limpo)
    except subprocess.CalledProcessError as e:
        erro = e.stderr.decode()
        return render_template('error.html', erro=erro)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)