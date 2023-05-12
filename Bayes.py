#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Definimos las probabilidades condicionales de los sintomas dado COVID-19
p_fatiga_given_covid = 0.90
p_tos_seca_given_covid = 0.70
p_dificultad_respirar_given_covid = 0.60
p_dolor_garganta_given_covid = 0.40
p_dolor_cabeza_given_covid = 0.70
p_dolor_cuerpo_given_covid = 0.30
p_escalofrios_given_covid = 0.20
p_secrecion_nasal_given_covid = 0.20
p_perdida_sentido_given_covid = 0.15
p_fiebre_given_covid = 0.50
p_dolor_pecho_given_covid = 0.10

# Definimos la prevalencia de COVID-19 en la población
p_covid = 0.10

# Definimos los sintomas observamos en el paciente
sintomas = ['Fatiga', 'Tos Seca', 'Dificultad para Respirar', 'Dolor de Garganta', 'Dolor de Cabeza', 'Dolor en el Cuerpo',
           'Escalofrios','Secreción', 'Perdida de Sentido','Fiebre','Dolor en el Pecho']

# Calculamos la probabilidad de que el paciente tenga COVID-19
p_sintomas_given_covid = p_fatiga_given_covid * p_tos_seca_given_covid * p_dificultad_respirar_given_covid * \
                        p_dolor_garganta_given_covid * p_dolor_cabeza_given_covid * p_dolor_cuerpo_given_covid * \
                        p_escalofrios_given_covid * p_secrecion_nasal_given_covid * p_perdida_sentido_given_covid * \
                        p_fiebre_given_covid * p_dolor_pecho_given_covid

p_sintomas_given_no_covid = 0.10 ** 11

p_sintomas = p_sintomas_given_no_covid * p_covid + p_sintomas_given_no_covid * (1 - p_covid)

p_covid_given_sintomas = p_sintomas_given_covid * p_covid / p_sintomas

print (f"La probabilidad de que el paciente tenga COVID-19 dados los sintomas es: {p_covid_given_sintomas}")


# In[ ]:




