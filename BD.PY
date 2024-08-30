import sqlite3
conexao = sqlite3.connect('poetroid.db')
cursor = conexao.cursor()
# Função para inserir um poema e suas palavras-chave
def inserir_poema_e_palavras(poema, palavras_chave):
    # Inserir o poema na tabela `poemas`
    cursor.execute('INSERT INTO poemas (poema) VALUES (?)', (poema,))
    poema_id = cursor.lastrowid  # Recupera o ID do poema recém-inserido
    for palavra in palavras_chave:
        cursor.execute('INSERT INTO palavras_chave (poema_id, palavra) VALUES (?, ?)', (poema_id, palavra))
    conexao.commit()

poema = 'Nesta sala cheia, as pessoas estão sentadas\nCada uma com sua história, com vida marcada.\nOlhares cruzados, conversas se iniciam,\nCom expressões faciais que suavemente se revelam.\nAs janelas abertas deixam a brisa passar,\nMas não há pressa, todos esperam o dia findar,\nTudo se acalma no fim,\nQuando cada um encontra seu próprio jardim.'
palavras_chave = ['sala']
inserir_poema_e_palavras(poema, palavras_chave)

poema= 'As janelas abertas deixam o mundo entrar, \nPessoas se sentam, prontas para partilhar. \nCada sorriso é uma ponte entre corações, \nOnde palavras se perdem em canções.\nAs mesas estão postas, aguardando as mãos,\nQue em breve criarão laços tão firmes quanto o chão,\nTudo estará calmo,\nQuando o sol se pôr no horizonte calado.'
palavras_chave = ['janela', 'janelas']
inserir_poema_e_palavras(poema, palavras_chave)

poema = 'As cortinas esvoaçam, criando sombras no chão,\nPessoas que se movem, com passos de indecisão.\nAlgumas sorriem, outras apenas observam,\nMas todas, de alguma forma, se preservam.\nAs luzes filtradas trazem paz ao ambiente,\nE o tempo passa, quase transparente,\nTudo se aquieta,\nQuando cada um encontra seu próprio planeta.'
palavras_chave = ['cortinas', 'cortina']
inserir_poema_e_palavras(poema, palavras_chave)

poema = "Computadores ligados, olhos atentos,\nNa sala de aula, o foco é discreto,\nLinhas de código, números dispersos,\nTudo avança em ritmo concreto.\n\nPalavras digitadas, sem eco,\nO aprendizado é prático, sem rodeios,\nOs alunos e as máquinas, sem afeto,\nConectados apenas pelos meios."
palavras_chave = ['computador', 'laptop']
inserir_poema_e_palavras(poema, palavras_chave)

poema= "Câmeras em silêncio, atentas,\nCapturam o instante, sem hesitar,\nO mundo filtrado em lentes precisas,\nFragmentos de tempo, sem se revelar.\n\nEnxergam o que passa despercebido,\nGuardam o que o olho não vê,\nRegistram, mas nunca sentem,\nApenas observam o que é."
palavras_chave = ['camera', 'câmeras', 'câmera']
inserir_poema_e_palavras(poema, palavras_chave)

poema = 'Óculos no rosto, ampliando o olhar,\nPessoas que se encontram, prontas para conversar.\nEntre as mesas, as palavras se soltam,\nE em cada gesto, os corações se envolvem.\nAs cortinas filtram a luz do dia,\nMas a calma na sala é pura harmonia,\nTudo estará bem,\nQuando o descanso vier também.'
palavras_chave = ['oculos', 'óculos']
inserir_poema_e_palavras(poema, palavras_chave)

poema ='Cadeiras ocupadas, histórias sendo contadas,\nPessoas que se encontram, prontas para as jornadas.\nEntre as mesas, sorrisos surgem,\nE em cada gesto, novas amizades fluem.\nAs cortinas filtram a luz suave do sol,\nE a calma se espalha como um lençol,\nTudo estará em paz,\nQuando o descanso vier, trazendo a tranquilidade que jaz.'
palavras_chave = ['cadeiras', 'sentado', 'sentada']
inserir_poema_e_palavras(poema, palavras_chave)

poema = 'Em volta das mesas, pessoas se reúnem,\nCom mãos entrelaçadas, sentimentos se assumem.\nConversas silenciosas, olhares trocados,\nSão histórias partilhadas em gestos delicados.\nAs janelas observam, atentas ao que acontece,\nMas a paz entre elas permanece,\nE no final do dia,\nTudo se dissolve na luz que guia.'
palavras_chave = ['mesa', 'mesas']
inserir_poema_e_palavras(poema, palavras_chave)

poema = 'Nesta sala abarrotada, há muitas pessoas,\nCada uma carregando suas verdades preciosas.\nAlgumas com sorrisos, outras com olhares cansados,\nMas todas compartilham gestos apaixonados.\nAs cadeiras estão cheias, a tensão é evidente,\nMas a conexão entre elas é persistente,\nE tudo ficará bem,\nQuando a noite chegar, trazendo paz também.'
palavras_chave = ['lotada', 'muitas pessoas']
inserir_poema_e_palavras(poema, palavras_chave)

poema = 'Sorrisos espalhados, iluminam o lugar,\nPessoas que se encontram, prontas para começar.\nEntre as mesas, gestos de compreensão,\nEm cada movimento, uma nova conexão.\nAs cortinas velam o que está por vir,\nMas a tensão do início começa a sumir,\nTudo estará bem,\nQuando o descanso finalmente vier também.'
palavras_chave = ['sorriso', 'sorrindo']
inserir_poema_e_palavras(poema, palavras_chave)

poema = 'Mãos que se estendem, prontas para ajudar,\nPessoas que se reúnem, cada uma com seu par.\nEm volta das cadeiras, risos ecoam,\nE as palavras ditas suavemente ressoam.\nAs janelas abertas deixam o ar circular,\nE o ambiente começa a desanuviar,\nTudo estará tranquilo,\nQuando a noite cair como um lenço sutil.'
palavras_chave = ['mãos', 'gestos']
inserir_poema_e_palavras(poema, palavras_chave)
conexao.close()