import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
#import matplotlib.pyplot as plt

##############
st.sidebar.image("fondo_quimica1.png",
                 caption="P")

##############Pagina 1##############
def Home():
    st.markdown("# ")
    #st.markdown("<h1 style='text-align: center; color: red;'>Juega a crear nuevas historias</h1>", unsafe_allow_html=True)
    st.sidebar.markdown("# Contenido del curso Química I")
    #image = Image.open("elprincipito.jpeg")
    #st.image(image, caption='El principito en Machupichu')

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
        st.write ('''Definición, características / Cálculo de la constante de equilibrio químico Kp y Kc / Relación de las constantes Kp y Kc / Grado de reacción (a) y cociente de reacción (Q) / relaciones entre 𝛼, Q y Kc 1 teoría de ácidos y bases / teoría de constante de acides y basicidad, Ka y Kb, teoría de auto- ionización del agua, Kw / Potencial del ión hidrogeno (pH), problemas / hidrólisis (Kh), soluciones buffer o tampón /cálculo del pH / Producto de solubílidad (Kps), efecto del ion común, solubilidad molar/ precipitación selectiva de iones (cationes y aniones).'''))

    #image = Image.open("DALL·E 2022-12-26 21.10.51 - Humberto Maturana head for 3D printing.png")
    #st.image(image, caption='Personaje ilustrado por IA para impresión 3D')
    
##############Pagina 2##############
def page2():
    st.markdown("# Ta")
    st.sidebar.markdown("# M")
    
    total5, total6 = st.columns(2, gap='large')
    with total5:
        st.info('Curso virtual (8 horas)')
        st.write('''E''')
        st.write (pd.DataFrame({'Temas': ['P',
                                  'P1', 
                                  'L','I'], 
                        'Horas': ["2", "2", 
                                   "2", "2"]}))
        st.write('N.')
    with total6:
        st.info('M')
        st.write('''P''')
        st.write('''C.''') 
        st.write('''C.''')
        st.write('''E''')
        st.write (pd.DataFrame({'Modalidad': ['General',
                                          'Estudiantes', 
                                          'Corporativo (grupos de 4)'], 
                                'Inversión': ["S", "S0", 
                                           "S1"]}))
    #image = Image.open("alberteinstein.jpeg")
    #st.image(image, caption='¿Recuerdas cuando Albert Einstein visitó Machupichu? Despierta historias alucinantes a través de la generación de imágenes con IA.')
  
    #image = Image.open("logPann_red.png")
    #st.image(image, caption='Descubre cómo las redes neuronales artificiales están revolucionando diversas áreas del conocimiento')


##
def page3():
  st.header('Más información', divider='rainbow')
  
  st.link_button("Youtube", "https://www.youtube.com/channel/UCm6lcnfmNS2stsUYVvrFOzg")
   
  st.link_button("Github", "https://github.com/inefable12")
  
  st.write('''S.''')

  st.write('''texto1''')
  st.markdown("<h1 style='text-align: center; color: purple;'>Texto 2</h1>", unsafe_allow_html=True)

##
page_names_to_funcs = {
  "Contenido del Curso": Home,
  "Actividad": page2,
  "Consultas": page3,
}

selected_page = st.sidebar.selectbox("Selecciona una página", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
