# pip install streamlit pandas matplotlib seaborn
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fonte de Dados
# https://www.kaggle.com/datasets/whenamancodes/student-performance

# Especificando o título da página e o ícone
st.set_page_config(page_title="Dashboard - Student Dataset", page_icon=":books:")

# sidebar
st.sidebar.title("Configurações de Exibição")

w = st.sidebar.multiselect('Buy', ['milk', 'apples', 'potatoes'])
st.write(w)

###
media_escola = st.sidebar.checkbox("1")
moda_endereco = st.sidebar.checkbox("2")
mediana_tempo_gp = st.sidebar.checkbox("3")
desvio_pad_ms = st.sidebar.checkbox("4")
media_tempo = st.sidebar.checkbox("5")
motivo = st.sidebar.checkbox("6")
mediana_falta = st.sidebar.checkbox("7")
nivel_saude = st.sidebar.checkbox("8")
extra_ok = st.sidebar.checkbox("9")
alcohol_c = st.sidebar.checkbox("10")
###
gsheets_show_id = st.sidebar.radio("Selecione o Dataset", ("Matemática", "Português"))

st.sidebar.subheader("Selecione o que deseja exibir")
show_dataset = st.sidebar.checkbox("Dados do Dataset")
show_dataset_description = st.sidebar.checkbox("Descrição do Dataset")

graph1_type = st.sidebar.selectbox("Gráfico 1: Selecione o tipo de gráfico", ("Barra", "Pizza", "Dispersão", "Histograma", "Boxplot"))

# Carregando o dataset
gsheets_math_id = "1392993996"
gsheets_portuguese_id = "0"

show_id = gsheets_math_id if gsheets_show_id == "Matemática" else gsheets_portuguese_id

gsheets_url = 'https://docs.google.com/spreadsheets/d/1pfqNNPJrB1QFcqUm5evvDeijycnuPFDztInZvl3nOyU/edit#gid=' + show_id
@st.cache_data(ttl=120)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

data = load_data(gsheets_url)

# Adicionando um título
st.title("Análise de Dados do Dataset de Estudantes")

# Descritivo do dataset
if show_dataset_description:
    st.subheader("Descrição do Dataset")

    st.markdown("""
| Column    | Description                                                                                        |
|-----------|----------------------------------------------------------------------------------------------------|
| school    | Student's school (binary: 'GP' - Gabriel Pereira or 'MS' - Mousinho da Silveira)                   |
| sex       | Student's sex (binary: 'F' - female or 'M' - male)                                               |
| age       | Student's age (numeric: from 15 to 22)                                                            |
| address   | Student's home address type (binary: 'U' - urban or 'R' - rural)                                  |
| famsize   | Family size (binary: 'LE3' - less or equal to 3 or 'GT3' - greater than 3)                         |
| Pstatus   | Parent's cohabitation status (binary: 'T' - living together or 'A' - apart)                       |
| Medu      | Mother's education (numeric: 0 - none, 1 - primary education (4th grade), 2 - 5th to 9th grade, 3 - secondary education or 4 - higher education) |
| Fedu      | Father's education (numeric: 0 - none, 1 - primary education (4th grade), 2 - 5th to 9th grade, 3 - secondary education or 4 - higher education) |
| Mjob      | Mother's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other') |
| Fjob      | Father's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other') |
| reason    | Reason to choose this school (nominal: close to 'home', school 'reputation', 'course' preference or 'other') |
| guardian  | Student's guardian (nominal: 'mother', 'father' or 'other')                                        |
| traveltime| Home to school travel time (numeric: 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - >1 hour) |
| studytime | Weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)   |
| failures  | Number of past class failures (numeric: n if 1<=n<3, else 4)                                       |
| schoolsup | Extra educational support (binary: yes or no)                                                      |
| famsup    | Family educational support (binary: yes or no)                                                     |
| paid      | Extra paid classes within the course subject (Math or Portuguese) (binary: yes or no)               |
| activities| Extra-curricular activities (binary: yes or no)                                                    |
| nursery   | Attended nursery school (binary: yes or no)                                                        |
| higher    | Wants to take higher education (binary: yes or no)                                                 |
| internet  | Internet access at home (binary: yes or no)                                                        |
| romantic  | With a romantic relationship (binary: yes or no)                                                   |
| famrel    | Quality of family relationships (numeric: from 1 - very bad to 5 - excellent)                       |
| freetime  | Free time after school (numeric: from 1 - very low to 5 - very high)                               |
| goout     | Going out with friends (numeric: from 1 - very low to 5 - very high)                               |
| Dalc      | Workday alcohol consumption (numeric: from 1 - very low to 5 - very high)                          |
| Walc      | Weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)                          |
| health    | Current health status (numeric: from 1 - very bad to 5 - very good)                                |
| absences  | Number of school absences (numeric: from 0 to 93)                                                  |
""")            

if show_dataset:
    st.subheader("Conjunto de Dados")
    st.dataframe(data)




if media_escola:
    st.subheader("1. Qual é a média de idade dos alunos na escola GP?")
    m_idade_gp = sum(data[data.school == 'GP']['age']) / len(data[data.school == 'GP']['age'])
    m_idade_ms = sum(data[data.school == 'MS']['age']) / len(data[data.school == 'MS']['age'])
    
    st.line_chart(pd.Series(data[data.school == 'GP']['age']).rolling(window=3).mean())
    st.write(f"Media: {m_idade_gp}")



    

if moda_endereco:
    st.subheader("2. Qual é a moda do endereço dos alunos na escola MS?")
    #moda_gp = data[data.school == 'GP']['address'].mode()
    #
    #if moda_gp[0] == 'U':
    #    st.write("Urbano")
    #elif moda_gp[0] == 'R':
    #    st.write("Rural")

    moda_ms = data[data.school == 'MS']['address'].mode()

    if moda_ms[0] == 'U':
        st.write("Urbano")
    elif moda_ms[0] == 'R':
        st.write("Rural")   
    
    st.dataframe(data[data.school == 'MS']['address'])

    
    

    

if mediana_tempo_gp:
    st.subheader("3. Qual é a mediana do tempo de viagem dos alunos que estudam na escola GP?")
    mediana_gp = data[data.school == 'GP']['traveltime'].median()
    mediana_ms = data[data.school == 'GP']['traveltime'].median()
    st.write(mediana_gp)
    st.line_chart(pd.Series(mediana_gp))


if desvio_pad_ms:
        st.subheader("4. Qual é o desvio padrão da idade dos alunos que têm apoio educacional extra na escola MS?")
        ms_apoio = data[data.school == 'MS'][data.schoolsup == 'yes']
        desvio_p = ms_apoio['age'].std()
        st.write(desvio_p)

if media_tempo:
    st.subheader("5. Qual é a média do tempo semanal de estudo dos alunos cujos pais estão separados na escola GP?")
    dados_p_media = data[data.school == 'GP'][data.Pstatus =='A']
    media_dados = sum(dados_p_media['age']) / len(dados_p_media['age'])
    st.write(media_dados)

    

if motivo:
    st.subheader("6. Qual é a moda do motivo pelo qual os alunos escolheram a escola MS?")
    moda_motivo = data[data.school == 'MS']['reason'].mode()
    st.write(moda_motivo[0])

if mediana_falta:
    st.subheader("7. Qual é a mediana do número de faltas dos alunos que frequentam a escola GP?")
    mediana_f = data[data.school == 'GP']['absences'].median()
    st.write(mediana_f)
    

if nivel_saude:
    st.subheader("8. Qual é o desvio padrão do nível de saúde dos alunos que frequentam atividades extracurriculares na escola MS?")
    data_desvio = data[data.school == 'MS'][data.activities == 'yes']
    st.write(data_desvio['health'].std())
    st.line_chart(pd.Series(data_desvio['health']).rolling(window=3).mean())
    st.write(f"Desvio Pad.: {data_desvio['health'].std()}")



if extra_ok:
    st.subheader("9. Quantos alunos já cumpriram as horas extracurriculares?")
    ext = len(data[data.activities == 'yes'])
    st.write(ext)


if alcohol_c:
    st.subheader("10. Qual é a moda do consumo de álcool dos alunos da escola MS durante a semana de trabalho?")
    alc = data[data.school == 'MS']['Dalc'].mode()
    st.line_chart(pd.Series(data[data.school == 'MS']['Dalc']).rolling(window=3).mean())
    st.write(f"Media: {alc[0]}")

