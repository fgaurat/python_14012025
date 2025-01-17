import streamlit as st
from CustomerDAO import CustomerDAO


def main():
    dao = CustomerDAO("customers_db.db")
    st.set_page_config(layout="wide")
    st.markdown('# Test de streamlit')
    name = st.text_input("Name", "")
    if st.button("Say hello"):
        st.write('Bonjour',name)

    st.table(dao.find_all())

if __name__=='__main__':
     # streamlit run main_streamlit.py
    main()
