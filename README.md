
# Gerenciador de Clientes – Projeto em Python

Este projeto foi desenvolvido com o objetivo de consolidar conhecimentos em **lógica de programação, manipulação de arquivos, estruturação de projetos em Python** e boas práticas de desenvolvimento.  

Ele simula um sistema simples de gestão de clientes via terminal, permitindo cadastro, armazenamento e análise de dados como saldos positivos e negativos.

---

## 📌 Funcionalidades

- Cadastro de clientes (nome e saldo)
- Armazenamento dos dados em arquivo `.txt`
- Leitura e exibição dos clientes cadastrados
- Filtro de clientes com saldo negativo
- Identificação do cliente com maior saldo
- Menu interativo com tratamento de erros

---

## 🧠 Tecnologias e conceitos aplicados

- **Python 3.x**
- Manipulação de arquivos (`open`, `read`, `write`)
- Estrutura de dados com listas e dicionários
- Tratamento de exceções (`try`, `except`)
- Estruturação de projetos com múltiplos arquivos Python (`main.py`, `cadastro.py`, `relatorios.py`)
- Separação de responsabilidades entre módulos
- Estilo de código limpo e legível

---

## 🗂️ Estrutura do Projeto

```
PythonProject/
├── data/                    # Arquivo de dados (clientes)
│   └── clientes.txt
├── src/                     # Lógica principal da aplicação
│   ├── main.py              # Menu e controle de fluxo
│   ├── cadastro.py          # Cadastro e salvamento
│   └── relatorios.py        # Geração de relatórios
├── README.md
└── .gitignore
```

---

## 💡 Por que este projeto importa?

Este projeto não usa frameworks ou bibliotecas externas — tudo foi feito com Python puro, focando no **entendimento completo da lógica e da estrutura do código**.

Além disso, foi construído passo a passo, com testes, validação e tratamento de erros reais que acontecem no dia a dia de qualquer sistema.

É um exemplo concreto da minha capacidade de:

- Escrever código limpo e funcional
- Pensar na organização de um projeto desde o início
- Criar soluções simples, diretas e confiáveis

---

## ▶️ Como executar

1. Clone o repositório:

```bash
git clone https://github.com/JovelinoMoraes/gerenciador-clientes-python.git
```

2. Acesse a pasta do projeto:

```bash
cd gerenciador-clientes-python/src
```

3. Execute o programa:

```bash
python3 main.py
```

O sistema abrirá um menu no terminal para interação.

---

## ✍️ Autor

**Jovelino Moraes** 
Apaixonado por tecnologia.
Estou construindo um portfólio sólido baseado em projetos práticos e bem estruturados, que demonstram o que realmente sei fazer.

> Este projeto representa meu domínio atual em Python e minha capacidade de entregar soluções organizadas, com foco em clareza, funcionalidade e boas práticas.

---

## 📫 Contato

- Email: jovelinodev@gmail.com 
- [LinkedIn](https://www.linkedin.com/in/jovelino-moraes/)
- [GitHub](https://github.com/JovelinoMoraes)

---

## ✅ Próximos Passos

- Exportação de dados para `.csv`
- Integração com interface gráfica (`tkinter`)
- Validação de clientes duplicados
- Versão com interface web (futuro)

---

> Obrigado por visitar meu repositório! 
> Estou aberto a feedbacks, conexões e oportunidades para evoluir ainda mais como desenvolvedor.
