# 💳 Credit Card Validator

Projeto desenvolvido em Python para validar números de cartões de crédito usando o algoritmo de **Luhn**, além de identificar a **bandeira do cartão** (Visa, Mastercard, etc.).

---

## 📦 Estrutura do Projeto

credit-card-validator/
├── src/
│ ├── init.py
│ ├── luhn.py # Validação com algoritmo de Luhn
│ └── validator.py # Identificação da bandeira do cartão
│
├── tests/
│ ├── init.py
│ └── test_validator.py # Testes unitários
│
├── requirements.txt
├── README.md
└── .gitignore


---

## ⚙️ Requisitos

- Python 3.10+ (recomendado 3.11 ou 3.12)
- `unittest` (já vem com o Python)

---

## 🚀 Como executar

### 1. Clone o repositório

git clone https://github.com/seu-usuario/credit-card-validator.git
cd credit-card-validator

### 2. Execute os testes
python -m unittest tests.test_validator

🧪 Testes implementados
Validação de número de cartão com algoritmo de Luhn

Identificação das bandeiras:

Visa

Mastercard

American Express

Discover

JCB

Diners Club

Casos inválidos

📌 Exemplo de uso futuro (em construção)
Você pode estender este projeto para incluir:

Interface Web (Flask/Streamlit)

Validação com entrada de usuário

Exportação para relatório ou logs

🧑‍💻 Autor
Feito com 💙 por [Matheus Sodré].
Projeto criado durante o Bootcamp - Microsoft 50 Anos - GitHub Copilot.