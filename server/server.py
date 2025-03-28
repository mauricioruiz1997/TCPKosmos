import socket
import logging
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.util import create_socket, HOST, PORT

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def run_server():
    with create_socket() as server_socket:
        server_socket.bind((HOST, PORT))
        # Escuchamos conexiones entrantes
        server_socket.listen()
        logging.info(f"Servidor escuchando en {HOST}:{PORT}")

        while True:
            # Aceptamos una nueva conexión
            client_socket, client_address = server_socket.accept()
            logging.info(f"Conexión establecida con {client_address}")

            with client_socket:
                while True:
                    try:
                        # Recibimos datos del cliente
                        data = client_socket.recv(1024)
                        if not data:
                            logging.info("Cliente desconectado inesperadamente.")
                            break

                        # Decodificamos el mensaje
                        message = data.decode("utf-8").strip()
                        logging.info(f"Mensaje recibido: {message}")

                        # Si el mensaje es "DESCONEXION", cerramos la conexión
                        if message.upper() == "DESCONEXION":
                            logging.info("Cliente solicitó la desconexión.")
                            break

                        # Respondemos al cliente en mayúsculas
                        response = message.upper()
                        client_socket.sendall(response.encode("utf-8"))
                        logging.info(f"Respuesta enviada: {response}")

                    # Manejamos Excepciones
                    except ConnectionResetError:
                        logging.info("Cliente cerró la conexión")
                        break

                logging.info(f"Conexión con {client_address} cerrada.")


if __name__ == "__main__":
    run_server()
