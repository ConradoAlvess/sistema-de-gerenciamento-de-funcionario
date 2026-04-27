# 💼 Sistema de Gerenciamento de Funcionários (Python)

## 📌 Descrição

Este projeto é um sistema de gerenciamento de funcionários desenvolvido em Python no terminal (CLI).

O sistema permite realizar operações completas de CRUD (Create, Read, Update, Delete), além de persistência de dados em arquivo JSON, garantindo que as informações não sejam perdidas ao encerrar o programa.

---

## 🚀 Funcionalidades

✔ Cadastrar funcionário
✔ Buscar funcionário por CPF
✔ Listar todos os funcionários
✔ Editar dados (nome, cargo e salário)
✔ Excluir funcionário com confirmação
✔ Validação de dados de entrada
✔ Persistência de dados em arquivo JSON

---

## 🛠️ Tecnologias utilizadas

* Python 3
* JSON (armazenamento de dados)
* Estruturas de dados (listas e dicionários)
* Tratamento de exceções (`try/except`)

---

## 🧠 Conceitos aplicados

* Programação estruturada
* Funções
* Laços de repetição (`while`, `for`)
* Condicionais (`if`, `elif`, `else`)
* Validação de entrada de usuário
* Manipulação de arquivos (`json.load` / `json.dump`)

---

## 📂 Estrutura do projeto

```
📁 sistema-funcionarios
 ├── main.py
 ├── funcionario.json
 └── README.md
```

---

## ▶️ Como executar o projeto

1. Clone o repositório:

```
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Acesse a pasta:

```
cd sistema-funcionarios
```

3. Execute o programa:

```
python main.py
```

---

## 💡 Exemplo de uso

```
=== SISTEMA DE FUNCIONÁRIOS ===

1 - Cadastrar Funcionário
2 - Procurar Funcionário
3 - Listar Funcionários
4 - Editar Funcionário
5 - Excluir Funcionário
6 - Sair
```

---

## 🔒 Validações implementadas

* Nome não pode ser vazio
* Nome deve conter apenas letras
* CPF deve conter 11 dígitos numéricos
* CPF não pode ser duplicado
* Salário deve ser um número válido e não negativo


---

## 👨‍💻 Autor

Desenvolvido por **Gustavo Alves Conrado de Lima**

---

## ⭐ Observação

Este projeto foi desenvolvido com foco em aprendizado e prática de lógica de programação, sendo um passo importante na evolução para desenvolvimento de sistemas mais complexos.

