import sqlite3
conexao = sqlite3.connect('poetroid.db')
cursor = conexao.cursor()
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