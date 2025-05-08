import streamlit as st
import sqlite3

# Criar ou ligar à base de dados
conn = sqlite3.connect("inventario.db", check_same_thread=False)
cursor = conn.cursor()

# Criar tabela se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS stock (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    quantidade INTEGER NOT NULL
)
""")
conn.commit()

# Funções de menu
def inserir_menu():
    st.subheader("Inserir Registos")
    nome = st.text_input("Nome do Item")
    quantidade = st.number_input("Quantidade", min_value=1, step=1)

    if st.button("Inserir"):
        cursor.execute("INSERT INTO stock (nome, quantidade) VALUES (?, ?)", (nome, quantidade))
        conn.commit()
        st.success(f"Item '{nome}' inserido com sucesso!")

def visualizar_menu():
    st.subheader("Visualizar Registos")
    cursor.execute("SELECT * FROM stock")
    registos = cursor.fetchall()
    if registos:
        for reg in registos:
            st.write(f"🟦 ID: {reg[0]} | Nome: {reg[1]} | Quantidade: {reg[2]}")
    else:
        st.info("Ainda não existem registos.")

def apagar_menu():
    st.subheader("Apagar Registos")
    cursor.execute("SELECT id, nome FROM stock")
    itens = cursor.fetchall()
    if itens:
        opcoes = [f"{id} - {nome}" for id, nome in itens]
        escolha = st.selectbox("Seleciona o item a apagar:", opcoes)
        if st.button("Apagar"):
            id_a_apagar = int(escolha.split(" - ")[0])
            cursor.execute("DELETE FROM stock WHERE id = ?", (id_a_apagar,))
            conn.commit()
            st.success("Registo apagado com sucesso!")
    else:
        st.info("Não há registos para apagar.")

def alterar_menu():
    st.subheader("Alterar Registos")
    cursor.execute("SELECT id, nome, quantidade FROM stock")
    itens = cursor.fetchall()
    if itens:
        opcoes = [f"{id} - {nome} (qtd: {qtd})" for id, nome, qtd in itens]
        escolha = st.selectbox("Seleciona o item a alterar:", opcoes)
        novo_nome = st.text_input("Novo nome")
        nova_quantidade = st.number_input("Nova quantidade", min_value=1, step=1)

        if st.button("Alterar"):
            id_a_alterar = int(escolha.split(" - ")[0])
            cursor.execute("UPDATE stock SET nome = ?, quantidade = ? WHERE id = ?", (novo_nome, nova_quantidade, id_a_alterar))
            conn.commit()
            st.success("Registo alterado com sucesso!")
    else:
        st.info("Não há registos para alterar.")

# Menu principal
def main_menu():
    st.set_page_config(page_title="Stockly", layout="centered")
    st.title("📦 Stockly - Gestão de Inventário")

    # Guardar estado da página atual
    menu = st.sidebar.radio("Menu", ("Início", "Inserir", "Visualizar", "Apagar", "Alterar"))

    if menu == "Início":
        st.write("Bem-vindo ao sistema de gestão de inventário. Usa o menu à esquerda para navegar.")

    elif menu == "Inserir":
        inserir_menu()

    elif menu == "Visualizar":
        visualizar_menu()

    elif menu == "Apagar":
        apagar_menu()

    elif menu == "Alterar":
        alterar_menu()

# Executar
if __name__ == "__main__":
    main_menu()
