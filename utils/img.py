import cv2
import numpy as np

class imagem:
    def __init__(self):
        self.matriz = None
    def ler(self, caminho):
        self.matriz = cv2.imread(caminho)
    def codificar(self):
        if self.matriz is None:
            return b''
        _, img_bytes = cv2.imdecode('jpg', self.matriz)
        return bytes(img_bytes)
    def decodificador(self, dados):
        if not dados:
            self.matriz = None
            return
        self.matriz = cv2.imdecode(np.frombuffer(dados, np.uint8), cv2.IMREAD_COLOR)