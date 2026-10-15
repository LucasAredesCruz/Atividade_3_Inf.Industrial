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

1- O tamanho da imagem é enviado através de um cabeçalho de 4 bytes antes do envio dos dados principais (função enviar_mensagem em protocol.py). No lado da receção, o laço while (na função de leitura completa) sabe que recebeu tudo porque compara o tamanho total acumulado no bytearray com o valor numérico que foi extraído dos 4 bytes iniciais. O laço apenas pede os "bytes em falta" ao recv até que a contagem coincida exatamente.

2- A thread é criada no laço principal do ficheiro server.py, logo a seguir à linha de accept(), através da chamada threading.Thread(...) seguida de .start(). O servidor consegue atender outros clientes porque não foi utilizado o método join() neste laço. Sem o join(), a thread principal do servidor não bloqueia à espera que o atendimento da imagem termine, voltando imediatamente ao accept() para aguardar novas ligações.

3- Commit do(a) [Lucas]: [código que encontra o rosto na imagem e isola ele.] - Neste commit, adaptei a classe Imagem para ler e descodificar os ficheiros JPEG sem interagir com sockets.

Commit do(a) [Felipe]: [feat: adiciona protótipo das funções do protocolo] - Neste commit, implementei o envio de um protótipo para do arquivo protocol.py.
Diferença conceptual:Commit: Regista localmente as alterações feitas no código, criando um marco no histórico do repositório no computador pessoal.Push: Transmite esses commits locais para a ramificação (branch) correspondente no repositório remoto (ex.: GitHub).Integrar pelo PR (Pull Request): É o processo de fundir (merge) de forma segura as alterações feitas numa ramificação de trabalho (ex: branch cliente) para a ramificação principal (main) no repositório remoto, permitindo revisão de código antes da união definitiva.

usou o Gemini para empacotar inteiros no python e a resolver um problema no cabeçalho de protocol.py