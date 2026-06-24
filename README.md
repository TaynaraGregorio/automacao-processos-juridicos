# 🔍 Automação de Consulta de Processos Jurídicos

Automação web desenvolvida em Python com Selenium para consulta de processos jurídicos por estado, preenchimento automático de formulários e registro dos resultados em planilha Excel.

## 💡 O que o projeto faz

- Lê uma planilha Excel com dados de processos (nome, advogado, número e cidade)
- Acessa automaticamente o site de busca jurídica para cada registro
- Seleciona o estado correto via menu dropdown
- Preenche o formulário de pesquisa automaticamente
- Captura o resultado (encontrado ou não encontrado) via alerta do navegador
- Atualiza a coluna `Status` na planilha com o resultado de cada consulta

## 🛠️ Tecnologias utilizadas

- Python 3
- Selenium
- Pandas
- openpyxl

## 📁 Estrutura do projeto