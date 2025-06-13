# 📁 Python DevOps Exercises

Este repositório contém **exercícios práticos com Python voltados para DevOps**, organizados em diferentes níveis de dificuldade e cobrindo tarefas comuns do dia a dia de quem trabalha com automação, infraestrutura e CI/CD.

---

## 📌 Objetivo

Ajudar iniciantes (ou transicionando de suporte ou desenvolvimento) a praticar Python com foco em tarefas reais de DevOps, como monitoramento, deploy automatizado, manipulação de logs, automação com Docker e muito mais.

---

## 🗂️ Estrutura

```
python-devops-exercises/
├── 01_backup_logs/             # Script de backup de arquivos .log
├── 02_process_monitor/         # Verificação de processo em execução
├── 03_log_reader/              # Leitura e filtragem de logs
├── 04_git_docker_deploy/       # Automação de deploy com Git e Docker Compose
├── 05_tcp_port_check/          # Verificação de porta TCP
├── 06_system_monitor_post/     # Envio de uso de CPU/RAM/DISCO via POST
├── 07_create_linux_users/      # Criação de usuários Linux via CSV
├── 08_healthcheck_loop/        # Verificação contínua de healthcheck HTTP
├── 09_symlink_deploy/          # Simulação de deploy azul-verde com symlink
└── 10_auto_deploy_project/     # Pipeline simples de auto deploy
├── requirements.txt            # Dependências do projeto
└── .gitignore                  # Arquivos ignorados pelo Git
```

---

## 🚀 Como usar

1. Clone este repositório:
```bash
git clone https://github.com/vasconceloseverton/python-devops-exercises.git
cd python-devops-exercises
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute os scripts com:
```bash
python3 nome_da_pasta/main.py
```
> ⚠️ Alguns scripts exigem permissões de administrador (ex: criar usuários Linux) ou ferramentas como Docker instaladas.

---

## 📅 Sugestão de cronograma de estudo

| Semana | Foco                                 | Pastas sugeridas                   |
|--------|--------------------------------------|------------------------------------|
| 1      | Fundamentos de automação e logs      | 01, 02, 03                         |
| 2      | Deploy local e monitoramento simples | 04, 05, 06                         |
| 3      | Scripts com sudo e loops reais       | 07, 08                            |
| 4      | Deploy avançado e integração         | 09, 10                            |

---

## ✅ Requisitos
- Python 3.8+
- Docker (para alguns exercícios)
- Linux ou WSL recomendado
- Bibliotecas: `psutil`, `requests`

### requirements.txt
```
psutil
requests
```

### .gitignore
```
__pycache__/
*.pyc
.env
*.log
.vscode/
.idea/
```

---

## 👨‍💻 Autor
Desenvolvido como parte do estudo de carreira DevOps por Everton Vasconcelos.

---

## 🧠 Contribua
Se quiser contribuir com mais exercícios DevOps em Python, sinta-se à vontade para abrir um PR! 💻

---

## 📎 Licença
MIT License. Sinta-se livre para usar e adaptar!
