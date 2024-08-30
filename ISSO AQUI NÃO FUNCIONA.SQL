CREATE DATABASE poetroid;
USE poetroid;

CREATE TABLE poemas (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Identificador único para cada poema
    poema TEXT NOT NULL,                -- Coluna para armazenar o poema
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Data e hora de criação do registro
);

-- Criação da tabela para armazenar as palavras-chave
CREATE TABLE palavras_chave (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Identificador único para cada palavra-chave
    poema_id INT,                       -- Relaciona a palavra-chave ao poema
    palavra TEXT NOT NULL,              -- A palavra-chave em si
    FOREIGN KEY (poema_id) REFERENCES poemas(id) -- Chave estrangeira ligando ao poema
);

INSERT INTO poemas (poema) 
VALUES ('Nesta sala cheia, as pessoas estão sentadas\nCada uma com sua história, com vida marcada.\nOlhares cruzados, conversas se iniciam,\nCom expressões faciais que suavemente se revelam.\nAs janelas abertas deixam a brisa passar,\nMas não há pressa, todos esperam o dia findar,\nTudo se acalma no fim,\nQuando cada um encontra seu próprio jardim.');
VALUES ('As janelas abertas deixam o mundo entrar, \nPessoas se sentam, prontas para partilhar. \nCada sorriso é uma ponte entre corações, \nOnde palavras se perdem em canções.\nAs mesas estão postas, aguardando as mãos,\nQue em breve criarão laços tão firmes quanto o chão,\nTudo estará calmo,\nQuando o sol se pôr no horizonte calado.')
VALUES ('As cortinas esvoaçam, criando sombras no chão,\nPessoas que se movem, com passos de indecisão.\nAlgumas sorriem, outras apenas observam,\nMas todas, de alguma forma, se preservam.\nAs luzes filtradas trazem paz ao ambiente,\nE o tempo passa, quase transparente,\nTudo se aquieta,\nQuando cada um encontra seu próprio planeta.')
VALUES ('Computadores ligados, olhos atentos,\nNa sala de aula, o foco é discreto,\nLinhas de código, números dispersos,\nTudo avança em ritmo concreto.\n\nPalavras digitadas, sem eco,\nO aprendizado é prático, sem rodeios,\nOs alunos e as máquinas, sem afeto,\nConectados apenas pelos meios.')
VALUES ('Câmeras em silêncio, atentas,\nCapturam o instante, sem hesitar,\nO mundo filtrado em lentes precisas,\nFragmentos de tempo, sem se revelar.\n\nEnxergam o que passa despercebido,\nGuardam o que o olho não vê,\nRegistram, mas nunca sentem,\nApenas observam o que é.')
VALUES ('Óculos no rosto, ampliando o olhar,\nPessoas que se encontram, prontas para conversar.\nEntre as mesas, as palavras se soltam,\nE em cada gesto, os corações se envolvem.\nAs cortinas filtram a luz do dia,\nMas a calma na sala é pura harmonia,\nTudo estará bem,\nQuando o descanso vier também.')
VALUES ('Cadeiras ocupadas, histórias sendo contadas,\nPessoas que se encontram, prontas para as jornadas.\nEntre as mesas, sorrisos surgem,\nE em cada gesto, novas amizades fluem.\nAs cortinas filtram a luz suave do sol,\nE a calma se espalha como um lençol,\nTudo estará em paz,\nQuando o descanso vier, trazendo a tranquilidade que jaz.')
VALUES ('Em volta das mesas, pessoas se reúnem,\nCom mãos entrelaçadas, sentimentos se assumem.\nConversas silenciosas, olhares trocados,\nSão histórias partilhadas em gestos delicados.\nAs janelas observam, atentas ao que acontece,\nMas a paz entre elas permanece,\nE no final do dia,\nTudo se dissolve na luz que guia.')
VALUES ('Nesta sala abarrotada, há muitas pessoas,\nCada uma carregando suas verdades preciosas.\nAlgumas com sorrisos, outras com olhares cansados,\nMas todas compartilham gestos apaixonados.\nAs cadeiras estão cheias, a tensão é evidente,\nMas a conexão entre elas é persistente,\nE tudo ficará bem,\nQuando a noite chegar, trazendo paz também.')
VALUES ('Sorrisos espalhados, iluminam o lugar,\nPessoas que se encontram, prontas para começar.\nEntre as mesas, gestos de compreensão,\nEm cada movimento, uma nova conexão.\nAs cortinas velam o que está por vir,\nMas a tensão do início começa a sumir,\nTudo estará bem,\nQuando o descanso finalmente vier também.')
VALUES ('Mãos que se estendem, prontas para ajudar,\nPessoas que se reúnem, cada uma com seu par.\nEm volta das cadeiras, risos ecoam,\nE as palavras ditas suavemente ressoam.\nAs janelas abertas deixam o ar circular,\nE o ambiente começa a desanuviar,\nTudo estará tranquilo,\nQuando a noite cair como um lenço sutil.')        


INSERT INTO palavras_chave (poema_id, palavra) VALUES (1, 'sala');
INSERT INTO palavras_chave (poema_id, palavra) VALUES (1, 'janela');
INSERT INTO palavras_chave (poema_id, palavra) VALUES (1, 'janelas');
INSERT INTO palavras_chave (poema_id, palavra) VALUES (1, 'cortina');
INSERT INTO palavras_chave (poema_id, palavra) VALUES (1, 'cortinas');
INSERT INTO palavras_chave (poema_id, palavra) VALUES (1, 'computador');
INSERT INTO palavras_chave (poema_id, palavra) VALUES (1, 'laptop');
INSERT INTO palavras_chave (poema_id, palavra) VALUES (1, 'camera');
INSERT INTO palavras_chave (poema_id, palavra) VALUES (1, 'oculos');
INSERT INTO palavras_chave (poema_id, palavra) VALUES (1, 'cadeira');
INSERT INTO palavras_chave (poema_id, palavra) VALUES (1, 'cadeiras');
INSERT INTO palavras_chave (poema_id, palavra) VALUES (1, 'sentado');
INSERT INTO palavras_chave (poema_id, palavra) VALUES (1, 'sentada');
INSERT INTO palavras_chave (poema_id, palavra) VALUES (1, 'mesa');
INSERT INTO palavras_chave (poema_id, palavra) VALUES (1, 'mesas');
INSERT INTO palavras_chave (poema_id, palavra) VALUES (1, 'lotada');
INSERT INTO palavras_chave (poema_id, palavra) VALUES (1, 'muitas pessoas');
INSERT INTO palavras_chave (poema_id, palavra) VALUES (1, 'sorriso');
INSERT INTO palavras_chave (poema_id, palavra) VALUES (1, 'jsorrindo');
INSERT INTO palavras_chave (poema_id, palavra) VALUES (1, 'mãos');
INSERT INTO palavras_chave (poema_id, palavra) VALUES (1, 'gestos');


SELECT 
    p.id,
    p.poema,
    GROUP_CONCAT(pc.palavra
        ORDER BY pc.palavra ASC
        SEPARATOR ', ') AS palavras_chave
FROM
    poemas p
        LEFT JOIN
    palavras_chave pc ON p.id = pc.poema_id
GROUP BY p.id;

SELECT p.poema
FROM poemas p
JOIN palavras_chave pc ON p.id = pc.poema_id
