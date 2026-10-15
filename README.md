# Portscan

Uma ferramenta em Python desenvolvida para analisar e escanear portas abertas em um determinado endereço IP, contando com uma suíte de testes automatizados utilizando `pytest`.

## Tecnologias Utilizadas

* **Python 3**
* **Pytest** (para testes automatizados)
* **Rich** (para saídas coloridas e estilizadas no terminal)

## Estrutura do Projeto

```text
portscan/
├── src/
│   ├── portscan.py      Script principal (gerenciamento de argumentos)
│   └── connect.py       Lógica de conexão de rede (tryConnection)
├── tests/
│   └── test_portscan.py 
├── pyproject.toml       
└── .gitignore           
```

## Como Instalar e Rodar

### 1. Clonar o repositório
```bash
git clone https://github.com/tatucode/portscan
cd portscan
```

### 2. Criar e ativar o ambiente virtual (Recomendado)
```bash
python -m venv venv
source venv/bin/activate   # No Linux/macOS
ou
venv\Scripts\activate     # No Windows
```

### 3. Instalar as dependências
```bash
pip install pytest rich
```

### 4. Executar o Portscan
Para escanear todas as portas de um IP:
```bash
python src/portscan.py -a <IP ALVO>
```

Para escanear portas específicas:
```bash
python src/portscan.py -p 80,443 <IP ALVO>
```

## Autor:
Pedro Victor
