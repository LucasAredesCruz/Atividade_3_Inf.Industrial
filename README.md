# Atividade_3_Inf.Industrial

## Estrutura de arquivos
```
/
├── README.md
├── requirements.txt
├── client/
│   ├── client.py
│   └── main.py
├── server/
│   ├── main.py
│   └── server.py
├── utils/
│   ├── img.py
│   └── protocol.py
└── test/
```


## Organização

### Felipe
Responsável pelo desenvolvimento da arquitetura do *servidor* e do *protocolo*.

### Lucas
Responsável pelo desenvolvimento da arquitetura do *cliente* e da *imagem*.

## Instalação
Para instalar o repositório na sua máquina, você deve criar um ambiente virtual e instalar os módulos necessários para a
execução do projeto:

```bash
python -m venv .venv

source .venv/bin/activate # Linux
# .venv\Scripts\Activate.ps1 # Windows (PowerShell)
# .venv\Scripts\Activate.bat # Windows (CMD)

pip install --upgrade pip
pip install -r requirements.txt
```
Caso você use `uv`:
```bash
uv venv

uv pip install -r requirements.txt
```
*Nota: você ainda deve ativar o ambiente virtual posteriormente para executar o código.*
