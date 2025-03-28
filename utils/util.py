import socket
import logging

# Configuración del logging para ver logs
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Definimos el host y puerto
HOST = "127.0.0.1"
PORT = 5000


def create_socket():
    """
    Crea y devuelve un socket TCP.
    """
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)
