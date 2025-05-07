import subprocess
import time
import webbrowser
import os

def start_flask_container():
    print("隣 Construindo imagem Docker do Flask...")
    subprocess.run(["docker", "build", "-t", "v1mr/flask:1.0.0", "src"], check=True)

    print(" Iniciando contêiner Flask...")
    subprocess.run([
        "docker", "run", "-d",
        "-p", "5000:5000",
        "--name", "painel",
        "-v", "/var/run/docker.sock:/var/run/docker.sock",  # Mapeia o socket do Docker
        "v1mr/flask:1.0.0"
    ], check=True)

if __name__ == "__main__":
    start_flask_container()
   
    print("✅ Servidor Flask iniciado! Acesse: http://localhost:5000")

    # Aguarda alguns segundos para o servidor iniciar
    time.sleep(10)
   
    # Abre o navegador
    webbrowser.open("http://localhost:5000")

    # Limpa o terminal
    os.system('cls' if os.name == 'nt' else 'clear')