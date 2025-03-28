import logging
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.util import create_socket, HOST, PORT


def run_client():
    with create_socket() as client_socket:
        client_socket.connect((HOST, PORT))
        logging.info(f"Conectado al servidor en {HOST}:{PORT}")

        while True:
            message = input("Ingresa un mensaje (DESCONEXION para salir): ").strip()

            if not message:
                logging.warning("Por favor ingresa un mensaje válido.")
                continue

            client_socket.sendall(message.encode("utf-8"))
            logging.info(f"Mensaje enviado: {message}")

            if message.upper() == "DESCONEXION":
                logging.info("Desconectado del servidor.")
                break

            response = client_socket.recv(1024).decode("utf-8")
            logging.info(f"Respuesta del servidor: {response}")


if __name__ == "__main__":
    run_client()
