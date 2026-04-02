import sqlite3

def criar_banco():
    """Cria o arquivo do banco de dados e a tabela de leads, se não existirem."""
    conexao = sqlite3.connect('agencia_marketing.db')
    
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER,
            email TEXT,
            endereco TEXT,
            trabalho TEXT,
            graduacao TEXT
        )
    ''')

    conexao.commit()
    conexao.close()
    print("Banco de dados e tabela 'leads' criados com sucesso!\n")

def cadastrar_lead(nome, idade, email, endereco, trabalho, graduacao):
    """Insere um novo lead no banco de dados."""
    conexao = sqlite3.connect('agencia_marketing.db')
    cursor = conexao.cursor()
    
    cursor.execute('''
        INSERT INTO leads (nome, idade, email, endereco, trabalho, graduacao)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (nome, idade, email, endereco, trabalho, graduacao))
    
    conexao.commit()
    conexao.close()
    print(f"Lead '{nome}' cadastrado com sucesso no banco de dados!")

def listar_leads():
    """Busca e exibe todos os leads cadastrados no banco de dados."""
    conexao = sqlite3.connect('agencia_marketing.db')
    cursor = conexao.cursor()
    
    cursor.execute('SELECT * FROM leads')
    leads_encontrados = cursor.fetchall() # Captura todos os resultados
    
    conexao.close()
    
    print("\n--- Lista de Leads da Agência ---")
    if not leads_encontrados:
        print("Nenhum lead cadastrado ainda.")
    else:
        for lead in leads_encontrados:
            
            print(f"ID: {lead[0]} | Nome: {lead[1]} | E-mail: {lead[3]} | Trabalho: {lead[5]}")
    print("---------------------------------\n")

if __name__ == "__main__":
    criar_banco()
    
    cadastrar_lead("Ana Silva", 28, "ana.silva@email.com", "Rua A, 123 - SP", "Gerente de Projetos", "Administração")
    cadastrar_lead("Carlos Mendes", 34, "carlos.m@email.com", "Av B, 456 - RJ", "Desenvolvedor Web", "Ciência da Computação")
    
    listar_leads()