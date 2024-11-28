# Oi krammie!! juntei tudo num código só pra te ajudar e explicar melhor (pedi ajuda do GPT pra ele corrigir a sintaxe ja que a ana paula não fez isso), ficou um pouco grande mas o que importa é que funciona!! (eu acho)
# Primeiramente, abaixo tem oq cada um dos arquivos separados faz ok?? 
# BD.PY -> inserção de poemas e palavras via sqlite
# CONEXAO.PY -> armazenamento e conexão com as descs da Polaprint
# EXECUTAR.PY -> print
# POLABRINTBD.PY -> armazenamento e print juntos pq tava testando na época

#SOBRE AS BIBLIOTECAS:
# NLTK: lê as descrições e analisa as palavras   
# SQLITE3: BANCO DE DADOS (mais fácil de se relacionar com python)

import sqlite3  
import nltk  
from nltk.corpus import stopwords  
from nltk.tokenize import word_tokenize  
nltk.download('punkt')  # divisor
nltk.download('stopwords')  # identificador de palavras

# Extrai as palavras da desc sem erros (até onde sei)
def extrair_palavras_chave(descricao):
    stop_words = set(stopwords.words('portuguese'))
    palavras = word_tokenize(descricao)
    palavras_chave = [palavra for palavra in palavras if palavra.isalpha() and palavra.lower() not in stop_words]
    return palavras_chave

# Criador do banco e tabelas, por precaução, mesmo já tendo sido criadas (acredito que não pese no código apesar de já existir no poetroid.db)
conexao = sqlite3.connect('poetroid.db')
cursor = conexao.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS poemas (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    poema TEXT NOT NULL                   
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS palavras_chave (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    poema_id INTEGER,                      
    palavra TEXT NOT NULL,                 
    FOREIGN KEY (poema_id) REFERENCES poemas(id) 
)
''')
conexao.commit() 

# Inserção de palavras e poemas (também sem peso)
def inserir_poema_e_palavras(poema, palavras_chave):
    cursor.execute('INSERT INTO poemas (poema) VALUES (?)', (poema,))
    poema_id = cursor.lastrowid  
    for palavra in palavras_chave:
        cursor.execute('INSERT INTO palavras_chave (poema_id, palavra) VALUES (?, ?)', (poema_id, palavra))
    conexao.commit()


poemas_palavras = [
    (
        """Nesta sala cheia, as pessoas estão sentadas
        Cada uma com sua história, com vida marcada.
        Olhares cruzados, conversas se iniciam,
        Com expressões faciais que suavemente se revelam.
        As janelas abertas deixam a brisa passar,
        Mas não há pressa, todos esperam o dia findar,
        Tudo se acalma no fim,
        Quando cada um encontra seu próprio jardim.""", 
        ['sala']
    ),
    (
        """As janelas abertas deixam o mundo entrar, 
        Pessoas se sentam, prontas para partilhar. 
        Cada sorriso é uma ponte entre corações, 
        Onde palavras se perdem em canções.
        As mesas estão postas, aguardando as mãos,
        Que em breve criarão laços tão firmes quanto o chão,
        Tudo estará calmo,
        Quando o sol se pôr no horizonte calado.""",
        ['janela', 'janelas']
    ),
    (
        """As cortinas esvoaçam, criando sombras no chão,
        Pessoas que se movem, com passos de indecisão.
        Algumas sorriem, outras apenas observam,
        Mas todas, de alguma forma, se preservam.
        As luzes filtradas trazem paz ao ambiente,
        E o tempo passa, quase transparente,
        Tudo se aquieta,
        Quando cada um encontra seu próprio planeta.""", 
        ['cortinas', 'cortina']
    ),
    (
        """Computadores ligados, olhos atentos,
        Na sala de aula, o foco é discreto,
        Linhas de código, números dispersos,
        Tudo avança em ritmo concreto.

        Palavras digitadas, sem eco,
        O aprendizado é prático, sem rodeios,
        Os alunos e as máquinas, sem afeto,
        Conectados apenas pelos meios.""", 
        ['computador', 'laptop']
    ),
    (
        """Câmeras em silêncio, atentas,
        Capturam o instante, sem hesitar,
        O mundo filtrado em lentes precisas,
        Fragmentos de tempo, sem se revelar.

        Enxergam o que passa despercebido,
        Guardam o que o olho não vê,
        Registram, mas nunca sentem,
        Apenas observam o que é.""",
        ['camera', 'câmeras', 'câmera']
    ),
    (
        """Óculos no rosto, ampliando o olhar,
        Pessoas que se encontram, prontas para conversar.
        Entre as mesas, as palavras se soltam,
        E em cada gesto, os corações se envolvem.
        As cortinas filtram a luz do dia,
        Mas a calma na sala é pura harmonia,
        Tudo estará bem,
        Quando o descanso vier também.""",
        ['oculos', 'óculos']
    ),
    (
        """Cadeiras ocupadas, histórias sendo contadas,
        Pessoas que se encontram, prontas para as jornadas.
        Entre as mesas, sorrisos surgem,
        E em cada gesto, novas amizades fluem.
        As cortinas filtram a luz suave do sol,
        E a calma se espalha como um lençol,
        Tudo estará em paz,
        Quando o descanso vier, trazendo a tranquilidade que jaz.""",
        ['cadeiras', 'sentado', 'sentada']
    ),
    (
        """Em volta das mesas, pessoas se reúnem,
        Com mãos entrelaçadas, sentimentos se assumem.
        Conversas silenciosas, olhares trocados,
        São histórias partilhadas em gestos delicados.
        As janelas observam, atentas ao que acontece,
        Mas a paz entre elas permanece,
        E no final do dia,
        Tudo se dissolve na luz que guia.""",
        ['mesa', 'mesas']
    ),
    (
        """Nesta sala abarrotada, há muitas pessoas,
        Cada uma carregando suas verdades preciosas.
        Algumas com sorrisos, outras com olhares cansados,
        Mas todas compartilham gestos apaixonados.
        As cadeiras estão cheias, a tensão é evidente,
        Mas a conexão entre elas é persistente,
        E tudo ficará bem,
        Quando a noite chegar, trazendo paz também.""",
        ['lotada', 'muitas pessoas']
    ),
    (
        """Sorrisos espalhados, iluminam o lugar,
        Pessoas que se encontram, prontas para começar.
        Entre as mesas, gestos de compreensão,
        Em cada movimento, uma nova conexão.
        As cortinas velam o que está por vir,
        Mas a tensão do início começa a sumir,
        Tudo estará bem,
        Quando o descanso finalmente vier também.""",
        ['sorriso', 'sorrindo']
    ),
    (
        """Mãos que se estendem, prontas para ajudar,
        Pessoas que se reúnem, cada uma com seu par.
        Em volta das cadeiras, risos ecoam,
        E as palavras ditas suavemente ressoam.
        As janelas abertas deixam o ar circular,
        E o ambiente começa a desanuviar,
        Tudo estará tranquilo,
        Quando a noite cair como um lenço sutil.""",
        ['mãos', 'gestos']
    )
]

for poema, palavras in poemas_palavras:
    palavras_chave = extrair_palavras_chave(poema) 
    inserir_poema_e_palavras(poema, palavras_chave)  

cursor.execute('''
SELECT p.id, p.poema, GROUP_CONCAT(pc.palavra, ', ') AS palavras_chave
FROM poemas p
LEFT JOIN palavras_chave pc ON p.id = pc.poema_id
GROUP BY p.id;
''')

resultados = cursor.fetchall()
for row in resultados:
    print(f"ID: {row[0]}, Poema: {row[1]}, Palavras-Chave: {row[2]}")
conexao.close()
