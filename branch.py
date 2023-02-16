import streamlit as st
import pandas as pd

st.title('Streamlit - Search ranges')

data_url = ('https://firebasestorage.googleapis.com/v0/b/streamlit-2832e.appspot.com/o/csv%2Fdataset.csv?alt=media&token=96b49571-fa0e-41af-97c4-7b643257810e')

def load_data_byranges(startid, endid):
    data = pd.read_csv(data_url)
    filtered_data_byrange = data[ (data['index'] >= startid) & (data['index'] <= endid) ]
    
    return filtered_data_byrange

startid = st.text_input('Start index')
endid = st.text_input('End index')
btnRange = st.button('Search by range')

if (btnRange):
    filterbyrange = load_data_byranges(int(startid), int(endid))
    count_row = filterbyrange.shape[0]
    st.write(f"Total itema: {count_row}")
    
    st.dataframe(filterbyrange)