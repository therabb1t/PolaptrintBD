import sqlite3
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')


def extrair_palavras_chave(descricao):
    stop_words = set(stopwords.words('portuguese'))  # Defina a linguagem desejada
    palavras = word_tokenize(descricao)
    palavras_chave = [palavra for palavra in palavras if palavra.isalpha() and palavra.lower() not in stop_words]
    return palavras_chave

# Conectar ao banco de dados (ou criar um novo arquivo)
conexao = sqlite3.connect('poetroid.db')
cursor = conexao.cursor()
# Criação da tabela para armazenar os poemas
cursor.execute('''
CREATE TABLE IF NOT EXISTS poemas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Identificador único para cada poema
    poema TEXT NOT NULL,                   -- Coluna para armazenar o poema
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Data e hora de criação do registro
)
''')
# Criação da tabela para armazenar as palavras-chave
cursor.execute('''
CREATE TABLE IF NOT EXISTS palavras_chave (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Identificador único para cada palavra-chave
    poema_id INTEGER,                      -- Relaciona a palavra-chave ao poema
    palavra TEXT NOT NULL,                 -- A palavra-chave em si
    FOREIGN KEY (poema_id) REFERENCES poemas(id) -- Chave estrangeira ligando ao poema
)
''')
conexao.commit()
conexao.close()
