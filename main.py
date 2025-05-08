import streamlit as st

# Funções para cada menu
def inserir_menu():
    st.subheader("Inserir Registos")
    st.write("Aqui podes inserir novos registos no inventário.")
    # Adiciona os campos de inserção aqui, como textboxes ou selects
    # Exemplo de um campo:
    nome_item = st.text_input("Nome do Item")
    quantidade = st.number_input("Quantidade", min_value=1, max_value=100, step=1)
    if st.button("Inserir"):
        st.write(f"Item '{nome_item}' inserido com quantidade {quantidade}.")

def visualizar_menu():
    st.subheader("Visualizar Registos")
    st.write("Aqui podes visualizar os registos do inventário.")
    # Aqui, pode ser necessário integrar com a base de dados ou um arquivo
    # Exemplo:
    st.write("Registos disponíveis...")

def apagar_menu():
    st.subheader("Apagar Registos")
    st.write("Aqui podes apagar registos do inventário.")
    # Similarmente, podes permitir a pesquisa e a remoção de itens
    nome_item = st.text_input("Nome do Item a Apagar")
    if st.button("Apagar"):
        st.write(f"Item '{nome_item}' apagado.")

def alterar_menu():
    st.subheader("Alterar Registos")
    st.write("Aqui podes alterar os registos do inventário.")
    # Campos para alterar um registo
    nome_item = st.text_input("Nome do Item a Alterar")
    nova_quantidade = st.number_input("Nova Quantidade", min_value=1, max_value=100, step=1)
    if st.button("Alterar"):
        st.write(f"Item '{nome_item}' alterado para quantidade {nova_quantidade}.")

# Função principal que contém o menu inicial
def main_menu():
    st.title("Stockly - Gestão de Inventário")
    st.image('icon.png', use_container_width=False)
    
    # Layout com botões
    col1, col2 = st.columns(2)

    with col1:
        if st.button('INSERIR REGISTOS'):
            inserir_menu()

    with col2:
        if st.button('VISUALIZAR REGISTOS'):
            visualizar_menu()

    col3, col4 = st.columns(2)

    with col3:
        if st.button('APAGAR REGISTOS'):
            apagar_menu()

    with col4:
        if st.button('ALTERAR REGISTOS'):
            alterar_menu()

# Função principal
if __name__ == "__main__":
    main_menu()
