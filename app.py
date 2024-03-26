import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
#import matplotlib.pyplot as plt

##############
st.sidebar.image("fondo_quimica1.png",
                 caption="Jesus Alvarado H, MSc, PhDc")

##############Pagina 1##############
def Home():
    st.markdown("# ")
    st.sidebar.markdown("# Química I")

    total1, total2 = st.columns(2, gap='large')
    with total1:
        st.info('Unidad 1: REACCIONES QUÍMICAS')
        st.write('''Generalidades sobre las reacciones químicas y ecuaciones químicas. 
                    Clasificación de las reacciones químicas. 
                    Reacciones endotérmicas y exotérmicas, cálculo de la entalpía de la reacción, 
                    entalpía de reacción estándar, ejercicios.
                    Métodos de balanceo de la reacciones químicas (redox – ion electrón).
                    Estequiometria I y las leyes ponderales, ley de conservación de la masa y de 
                    las proporciones definidas, problemas. 
                    Estequiometría II, ley de las relaciones sencillas, problemas con gases 
                    ideales, masa equivalente.''')
        
    with total2:
        st.info('Unidad 2: SOLUCIONES')
        st.write (pd.DataFrame({'Tema': ['Componentes y clasificación, ley de número equivalente',
                                          'Unidades de concentración, fracción molar, Molaridad', 
                                          'Normalidad y Molalidad, partes por millón',
                                          'Método de dilución y mezcla de soluciones',
                                          'problemas de estequiometria de soluciones',
                                          'titulación acido – base, uso del indicador',
                                          'Propiedades coligativas de las soluciones, ecuación de Vant Hoff'
                                        ], 
                                'Fecha': ["Semana", "Semana", 
                                           "Semana","Semana", "Semana", 
                                           "Semana","Semana",]}))
    
    total3, total4 = st.columns(2, gap='large')
    with total3:
        st.info('Unidad 3: CINÉTICA QUÍMICA')
        st.write('''Definición, generalidades / Cálculo de la velocidad de una reacción química / Velocidades de reacción de orden cero, de 1° y 2º orden, ejercicios / Cálculo de la vida media de una reacción química / Factores que modifican la velocidad de reacción (temperatura, presión, concentración y catalizador).''')
        
    with total4:
        st.info('Unidad 4: EQUILIBRIO QUÍMICO ')
        st.write ('''Definición, características / Cálculo de la constante de equilibrio químico Kp y Kc / Relación de las constantes Kp y Kc / Grado de reacción (a) y cociente de reacción (Q) / relaciones entre 𝛼, Q y Kc 1 teoría de ácidos y bases / teoría de constante de acides y basicidad, Ka y Kb, teoría de auto- ionización del agua, Kw / Potencial del ión hidrogeno (pH), problemas / hidrólisis (Kh), soluciones buffer o tampón /cálculo del pH / Producto de solubílidad (Kps), efecto del ion común, solubilidad molar/ precipitación selectiva de iones (cationes y aniones).''')

    
    
##############Pagina 2##############
def page2():
    st.markdown("# Actividad: 25/03/2024")
    st.sidebar.markdown("# ")
    
    st.info('Individual')
    st.write('''Tiempo estimado: 1 hora''')
    st.write('''Fecha de entrega: No aplica''')
    st.write ('''Repasar material introductorio sobre python en Google Colab''')
    st.write('Sugerencia: https://github.com/inefable12/CQCPE_2023_jesus/blob/main/1_ABC_Python_github.ipynb')
  
    st.info('Grupal')
    st.write('''Tiempo estimado: 1 hora''')
    st.write('''Por grupo resolver los ejercicios asignados (capítulo 3 de Brown) empleando python desde Google Colab. Se enviará''')
    st.write('''Fecha máxima de entrega: Domingo 31/03/2024 a las 23:59''')
    

##
def page3():
  st.header('Más información', divider='rainbow')
  
  st.link_button("Youtube", "https://www.youtube.com/channel/UCm6lcnfmNS2stsUYVvrFOzg")
   
  st.link_button("Github", "https://github.com/inefable12")
  
  #st.write('''S.''')

  #st.write('''texto1''')
  #st.markdown("<h1 style='text-align: center; color: purple;'>Texto 2</h1>", unsafe_allow_html=True)

##
page_names_to_funcs = {
  "Contenido del Curso": Home,
  "Actividad": page2,
  "Consultas": page3,
}

selected_page = st.sidebar.selectbox("Selecciona una página", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
