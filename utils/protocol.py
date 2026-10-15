import socket
import struct
from typing import Optional

HEADER_SIZE = 4  # Tamanho do header em bytes (4 bytes = unsigned int de 32 bits)

def msgSend(sock: socket.socket, msg: bytes):
    """
    @brief Envia uma stream de bytes pelo soquete especificado precedida pelo seu tamanho.

    @param sock socket a ser utilizado para envio da mensagem.
    @param msg mensagem em bytes a ser enviada.
    """
    # Extrai o tamanho da mensagem e compacta tudo em big endian
    msg_size = len(msg)
    header = struct.pack("!I", msg_size)

    # Envia os dados com sendall para garantir que todos os bytes sejam enviados
    sock.sendall(header + msg)


def msgRecv(sock: socket.socket) -> bytes:
    """
    @brief Recebe uma stream de bytes pelo socket especificado.

    @param sock socket a ser utilizado para recepção da mensagem.

    @returns msg mensagem em bytes recebida ou bytes vazios se o socket for fechado.
    """
    # Lambda que garante a recepção de N bytes a partir do socket
    def recvExact(sizeToRead: int) -> Optional[bytes]:
        data = bytearray()
        while len(data) < sizeToRead:
            packet = sock.recv(sizeToRead - len(data))

            if not packet:
                # Impede erros se o soquete fechar enquanto uma mensagem é recebida
                return None

            data.extend(packet)
        return bytes(data)

    header = recvExact(HEADER_SIZE)
    if not header:
        return b"" 

    msgSize = struct.unpack("!I", header)[0]

    payload = recvExact(msgSize)
    if payload is None:
        raise ConnectionError("Conexão fechada antes do recebimento completo da mensagem.")

    return payload
