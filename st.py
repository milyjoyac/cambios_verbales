import streamlit as st #LIBRERIA DE STREAMLIT
import pandas as pd    #LIBRERIA DE PANDAS PARA MANEJO DE EXCEL
from PIL import Image  
import base64          #LIBRERIA PARA TRABAJAR CON LOS FONDOS

#Hola MUNDO: Iremos paso por paso en la creación de esta app:

####1 ER PASO: Debemos extraer las tablas de datos de nuestra hoja EXCEL 'mapudungun.xlsx'
#TABLA PARA CONSONANTE:
datos_kon=pd.read_excel('mapudungun.xlsx',sheet_name='kon')
#TABLA PARA TERMINACIÓN EN 'AEOU':
datos_tripa=pd.read_excel('mapudungun.xlsx',sheet_name='tripa')
#TABLA PARA TERMINACIÓN EN 'I':
datos_pi=pd.read_excel('mapudungun.xlsx',sheet_name='pi')
####2 DO PASO: Ahora debemos crear diccionarios para poder acceder a cada una de las combinaciones, en este caso tomaremos la columna
####'persona' como índice
#CREANDO DICCIONARIO PARA TERMINACIÓN EN CONSONANTE:
D_kon=datos_kon.set_index('persona').to_dict(orient='index')
#CREANDO DICCIONARIO PARA TERMINACIÓN EN 'AEOU':
D_tripa=datos_tripa.set_index('persona').to_dict(orient='index')
#CREANDO DICCIONARIO PARA TERMINACIÓN EN 'I':
D_pi=datos_pi.set_index('persona').to_dict(orient='index')
#3 ER PASO: 
st.title("¡Bienvenidos al conjugador de verbos en Mapudungun! :smile:")

#i=Image.open('DICT.png')
#st.image(i)

#####4 TO PASO: Estableciendo FONDO DE LA APP:
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('GIBLI.jpg')    

####5 TO PASO: LÓGICA DEL PROGRAMA
palabra=st.text_input("Ingresar verbo a conjugar")
numero=st.selectbox("Seleccionar una opción:", ["singular","dual","plural"])
persona=st.selectbox("Seleccionar una opción:",[1,2,3])
if palabra== '': 
    palabra='hola'
else:
    palabra=palabra
ultima_letra=palabra[-1]
if ultima_letra not in 'aeiou':
    palabra_transformada=palabra+' '+D_kon[persona][numero]
elif ultima_letra in "aeou":
    palabra_transformada=palabra+' '+D_tripa[persona][numero]
elif ultima_letra == 'i':
    palabra_transformada=palabra+' '+D_pi[persona][numero]

if st.button('Conjugar'):
    st.write(palabra_transformada)
