import socket
import cv2
from img import imagem
from protocol import enviar_mensagem, receber_mensagem

def iniciar_cliente():
    host, port = '127.0.0.1', 9000
    caminho_imagem = 'faces/image_0001.jpg' 

    img = imagem()
    img.ler(caminho_imagem)
    
    if img.matriz is None:
        print(f"Imagem {caminho_imagem} não encontrada!")
        return

    dados_imagem = img.codificar()

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        tcp.connect((host, port))
        print("Conectado! Enviando imagem...")
        enviar_mensagem(tcp, dados_imagem)

        print("Aguardando resposta do servidor...")
        dados_resposta = receber_mensagem(tcp)

        if not dados_resposta:
            print("Nenhuma imagem recebida de resposta.")
            return

        img_resp = imagem()
        img_resp.decodificar(dados_resposta)
        
        if img_resp.matriz is not None:
            cv2.imshow('Imagem Processada', img_resp.matriz)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            
    except Exception as e:
        print(f"Erro na execução do cliente: {e}")
    finally:
        tcp.close()

if __name__ == "__main__":
    iniciar_cliente()