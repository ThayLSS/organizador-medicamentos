**Organizador de Medicamentos**
Este projeto é um sistema para gerenciamento e organização de medicamentos desenvolvido em Python. O foco principal é a robustez do código, garantida por testes automatizados.

**Como Acessar e Rodar o Projeto**
Para avaliar a aplicação, você pode escolher entre as duas abordagens abaixo, conforme sua preferência de ambiente:

**Clone o repositório:**
git clone https://github.com/ThayLSS/organizador-medicamentos

**1. Via VS Code**
Abordagem sugerida para uma análise detalhada da arquitetura, pastas e lógica.

Abra o Visual Studio Code e vá em File > Open Folder.

Selecione a pasta organizador-medicamentos que foi clonada anteriormente.

Abra o Terminal Integrado do VS Code (Atalho: Ctrl + ' ou Ctrl + J).

Certifique-se de que o terminal está apontando para a raiz do projeto e execute a aplicação:
**python -m src.main**

**2. Via Terminal**
Ideal para verificar rapidamente se os testes e a aplicação estão operantes.

Entre na pasta raiz do projeto:
**cd organizador-medicamentos**

Instale as dependências necessárias:
**pip install -r requirements.txt**

Execute a suite de testes:
**python -m pytest**

Testes Automatizados
O projeto utiliza o Pytest para garantir a integridade de todas as funções de gerenciamento.

Comando para execução: **python -m pytest**

Localização dos arquivos: Pasta /tests

Cobertura: Inclui testes de fluxo principal e validações de lógica.

Qualidade de Código
Para garantir um código limpo e padronizado conforme a PEP 8, o projeto utiliza o Flake8. Para rodar a verificação de linting:
**python -m flake8 src/**

Licença
Este projeto está sob a licença MIT. Isso significa que você é livre para usar, copiar e modificar o software, desde que mantenha os créditos originais.

Informações Gerais
Versão Atual: 1.0.0

**Autora: Thaynara Lima Soares Sousa**

GitHub: https://github.com/ThayLSS

Link Direto do Repositório: https://github.com/ThayLSS/organizador-medicamentos