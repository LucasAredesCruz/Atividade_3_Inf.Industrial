import socket

HEADER_SIZE = 4 # Tamanho do header em bytes

def msgSend(sock: socket.socket, msg: bytes):
    """
    @brief Envia uma stream de bytes pelo soquete especificado.

    @param sock socket a ser utilizado para envio da mensagem.
    @param msg mensagem em bytes a ser enviada.
    """

    pass

def msgRecv(sock: socket.socket) -> bytes:
    """
    @brief Recebe uma stream de bytes pelo socket especificado.

    @param sock socket a ser utilizado para recepção da mensagem.

    @returns msg mensagem em bytes recebida.
    """

    return bytes()
