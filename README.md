📂 Listar Arquivos e Exportar para Excel

Este script em Python percorre uma pasta e todas as suas subpastas, lista todos os arquivos encontrados e exporta o resultado para uma planilha Excel (.xlsx).
A ferramenta possui uma interface gráfica simples, construída com Tkinter, que permite ao usuário selecionar a pasta de origem e o nome/local do arquivo de saída.
Ao final do processo, é possível abrir automaticamente o arquivo gerado.

🚀 Funcionalidades
Busca recursiva em todas as subpastas.

Exporta a lista de arquivos para Excel.

Interface gráfica para seleção de pasta e arquivo de saída.

Compatível com Windows, macOS e Linux.

Pergunta se deseja abrir o Excel gerado.

📋 Requisitos
Python 3.8+

Bibliotecas Python:

pandas

tkinter (já incluída na instalação padrão do Python)

openpyxl (para salvar arquivos Excel)

Instale as dependências com:

bash
Copiar
Editar
pip install pandas openpyxl
📂 Estrutura de Arquivos
Copiar
Editar
listar_arquivos_excel.py
💻 Como Usar
Clone este repositório:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Execute o script:

bash
Copiar
Editar
python listar_arquivos_excel.py
Na interface:

Selecione a pasta de origem.

Escolha o nome e local do arquivo .xlsx de saída.

Aguarde o processamento e escolha se deseja abrir o Excel gerado.

📊 Exemplo de Saída
Arquivo
C:\Users\Lucas\Documentos\projeto\relatorio.docx
C:\Users\Lucas\Documentos\projeto\dados\tabela.csv
C:\Users\Lucas\Documentos\projeto\imagens\foto1.jpg

⚙️ Compatibilidade
Sistema Operacional	Suporte
Windows	✅
macOS	✅
Linux	✅

📜 Licença
Este projeto está sob a licença MIT – consulte o arquivo LICENSE para mais detalhes.# escavador_de_arquivos
Script em Python que percorre uma pasta (e todas as suas subpastas), lista todos os arquivos encontrados e exporta o resultado para uma planilha Excel
