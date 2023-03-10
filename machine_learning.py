# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 21:34:05 2023

@author: Sara
"""
#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize.treebank import TreebankWordDetokenizer
import zipfile
from pathlib import Path
from joblib import dump, load
import joblib
from skimage import io



def machine_learning_function():    
    #st.set_option('deprecation.showPyplotGlobalUse', False)
    img = io.imread('Resources/machine-learning-tout-savoir-une.jpg')  
    st.image(img, width=250)

    prod_vege_2018 = pd.read_csv("Resources/2018_donneesgrandescultures.csv", sep=';', header = [0,1])
    prod_vege_2018.iloc[:,1:] = prod_vege_2018.iloc[:,1:].astype(float)
    prod_vege_2018.rename({'Unnamed: 0_level_0':''}, axis=1, inplace = True)
    prod_vege_2018.iloc[:,1:] = prod_vege_2018.iloc[:,1:].round(2)
    
    prod_vege_2018.fillna(0, inplace = True)
    prod_vege_2018 = prod_vege_2018.sort_values(by=('', 'Cultures'))
    prod_vege_2018.reset_index(drop=True, inplace=True)
    prod_vege_2018.insert(0, "Année", '2018')
    prod_vege_2018['Année'] = prod_vege_2018['Année'].apply(lambda x: pd.to_datetime(str(x),format='%Y%'))
    
    
    
 
    prod_vege_2019 = pd.read_csv("Resources/2019_donneesgrandescultures.csv", sep=';', header = [0,1])
    
    prod_vege_2019.iloc[:,1:] = prod_vege_2019.iloc[:,1:].astype(float)
    prod_vege_2019.rename({'Unnamed: 0_level_0':''}, axis=1, inplace = True)
    prod_vege_2019.iloc[:,1:] = prod_vege_2019.iloc[:,1:].round(2)
    
    
    prod_vege_2019.fillna(0, inplace=True)
    prod_vege_2019 = prod_vege_2019.sort_values(by=('', 'Cultures'))
    prod_vege_2019.reset_index(drop=True, inplace=True)
    prod_vege_2019.insert(0, "Année", '2019')
    prod_vege_2019['Année'] =prod_vege_2019['Année'].apply(lambda x: pd.to_datetime(str(x),format='%Y%'))
    
    
    # In[4]:
    
    
    prod_vege_2020 = pd.read_csv("Resources/2020_donneesgrandescultures.csv", sep=';', header=[0,1])
    
    
    prod_vege_2020.iloc[:,1:] = prod_vege_2020.iloc[:,1:].astype(float)
    prod_vege_2020.rename({'Unnamed: 0_level_0':''}, axis=1, inplace = True)
    prod_vege_2020.iloc[:,1:] = prod_vege_2020.iloc[:,1:].round(2)
    
    
    prod_vege_2020.fillna(0, inplace=True)
    
    prod_vege_2020 = prod_vege_2020.sort_values(by=('', 'Cultures'))
    prod_vege_2020.reset_index(drop=True, inplace=True)
    prod_vege_2020.insert(0, "Année", '2020')
    prod_vege_2020['Année'] =prod_vege_2020['Année'].apply(lambda x: pd.to_datetime(str(x),format='%Y%'))
    
    
    
    # In[5]:
    
    
    prod_vege_2021 = pd.read_csv("Resources/2021_donneesgrandescultures (1).csv", sep=';', header=[0,1])
    
    prod_vege_2021.iloc[:,1:] = prod_vege_2021.iloc[:,1:].astype(float)
    prod_vege_2021.rename({'Unnamed: 0_level_0':''}, axis=1, inplace = True)
    prod_vege_2021.iloc[:,1:] = prod_vege_2021.iloc[:,1:].round(2)
    
    
    prod_vege_2021.fillna(0, inplace=True)
    
    prod_vege_2021.replace({'Rendement(q/h)': 'Rendement(q/ha)'}, inplace=True)
    
    prod_vege_2021 = prod_vege_2021.sort_values(by=('', 'Cultures'))
    prod_vege_2021.reset_index(drop=True, inplace=True)
    prod_vege_2021.insert(0, "Année", '2021')
    prod_vege_2021['Année'] =prod_vege_2021['Année'].apply(lambda x: pd.to_datetime(str(x),format='%Y%'))
    
    
    
    
    
    
    # In[9]:
    
    
    moyenne_2019 = prod_vege_2019.iloc[:,2:].drop(prod_vege_2019.index[5]).mean()
    moyenne_2018 = prod_vege_2018.iloc[:,2:].drop(prod_vege_2018.index[5]).mean()
    ecart_production_2018_2019 = (moyenne_2019 - moyenne_2018) / moyenne_2019
    prod_vege_2018.iloc[5,2:] = prod_vege_2018.iloc[5,2:].replace([prod_vege_2018.iloc[5,2:].values], [np.array(prod_vege_2019.iloc[5,2:] - (moyenne_2019 *ecart_production_2018_2019))])
    
    
    # In[10]:
    
    
    
    # In[20]:
    
    
    moyenne_2018 = prod_vege_2018.iloc[:, prod_vege_2018.columns.get_level_values(1)=='Production(1000 t)'].mean()
    moyenne_2019 = prod_vege_2019.iloc[:, prod_vege_2019.columns.get_level_values(1)=='Production(1000 t)'].mean()
    
    ecart_production_2018_2019 = pd.DataFrame((moyenne_2019 - moyenne_2018) / moyenne_2019, columns = ['ecart_production_2018_2019'])
    
    
    # In[21]:
    
    
    moyenne_2020 = prod_vege_2020.iloc[:, prod_vege_2020.columns.get_level_values(1)=='Production(1000 t)'].mean()
    ecart_production_2019_2020 = pd.DataFrame((moyenne_2020 - moyenne_2019) / moyenne_2020, columns = ['ecart_production_2019_2020'])
    
    
    # In[22]:
    
    
    moyenne_2021 = prod_vege_2021.iloc[:, prod_vege_2021.columns.get_level_values(1)=='Production(1000 t)'].mean()
    ecart_production_2020_2021 = pd.DataFrame((moyenne_2021 - moyenne_2020) / moyenne_2021, columns = ['ecart_production_2020_2021'])
    
    
    # In[23]:
    
    
    prod_2018_2019 = pd.DataFrame(ecart_production_2018_2019.values.reshape(14,1), columns = ['ecart production 2018-2019'], index = prod_vege_2018.columns[2:].get_level_values(0).unique())
    prod_2019_2020 = pd.DataFrame(ecart_production_2019_2020.values.reshape(14,1), columns = ['ecart production 2019-2020'], index = prod_vege_2018.columns[2:].get_level_values(0).unique())
    prod_2020_2021 = pd.DataFrame(ecart_production_2020_2021.values.reshape(14,1), columns = ['ecart production 2020-2021'], index = prod_vege_2018.columns[2:].get_level_values(0).unique())
    
    
    # In[24]:
    
    
    variations_prod_2018_2021 = pd.concat([prod_2018_2019, prod_2019_2020, prod_2020_2021], axis = 1)
    
    
    # In[25]:
    
    
    variations_prod_2018_2021 = (variations_prod_2018_2021 * 100).round(2).astype(str) + '%'
    
    
    # In[26]:
    
    
    moyenne_2018 = prod_vege_2018.iloc[:, prod_vege_2018.columns.get_level_values(1)=='Rendement(q/ha)'].mean()
    moyenne_2019 = prod_vege_2019.iloc[:, prod_vege_2019.columns.get_level_values(1)=='Rendement(q/ha)'].mean()
    ecart_rendement_2018_2019 = (moyenne_2019 - moyenne_2018) / moyenne_2019
    
    moyenne_2020 = prod_vege_2020.iloc[:, prod_vege_2020.columns.get_level_values(1)=='Rendement(q/ha)'].mean()
    ecart_rendement_2019_2020 = (moyenne_2020 - moyenne_2019) / moyenne_2020
    
    moyenne_2021 = prod_vege_2021.iloc[:, prod_vege_2021.columns.get_level_values(1)=='Rendement(q/ha)'].mean()
    ecart_rendement_2020_2021 = (moyenne_2021 - moyenne_2020) / moyenne_2021
    
    rend_2018_2019 = pd.DataFrame(ecart_rendement_2018_2019.values.reshape(14,1), columns = ['ecart rendement 2018-2019'], index = prod_vege_2018.columns[2:].get_level_values(0).unique())
    rend_2019_2020 = pd.DataFrame(ecart_rendement_2019_2020.values.reshape(14,1), columns = ['ecart rendement 2019-2020'], index = prod_vege_2018.columns[2:].get_level_values(0).unique())
    rend_2020_2021 = pd.DataFrame(ecart_rendement_2020_2021.values.reshape(14,1), columns = ['ecart rendement 2020-2021'], index = prod_vege_2018.columns[2:].get_level_values(0).unique())
    
    variations_rend_2018_2021 = pd.concat([rend_2018_2019, rend_2019_2020, rend_2020_2021], axis = 1)
    
    variations_rend_2018_2021 = (variations_rend_2018_2021 * 100).round(2).astype(str) + '%'
    
    
    # In[27]:
    
    
    moyenne_2018 = prod_vege_2018.iloc[:, prod_vege_2018.columns.get_level_values(1)=='Superficie(1000 ha)'].mean()
    moyenne_2019 = prod_vege_2019.iloc[:, prod_vege_2019.columns.get_level_values(1)=='Superficie(1000 ha)'].mean()
    ecart_surface_2018_2019 = (moyenne_2019 - moyenne_2018) / moyenne_2019
    
    moyenne_2020 = prod_vege_2020.iloc[:, prod_vege_2020.columns.get_level_values(1)=='Superficie(1000 ha)'].mean()
    ecart_surface_2019_2020 = (moyenne_2020 - moyenne_2019) / moyenne_2020
    
    moyenne_2021 = prod_vege_2021.iloc[:, prod_vege_2021.columns.get_level_values(1)=='Superficie(1000 ha)'].mean()
    ecart_surface_2020_2021 = (moyenne_2021 - moyenne_2020) / moyenne_2021
    
    surf_2018_2019 = pd.DataFrame(ecart_surface_2018_2019.values.reshape(14,1), columns = ['ecart surface 2018-2019'], index = prod_vege_2018.columns[2:].get_level_values(0).unique())
    surf_2019_2020 = pd.DataFrame(ecart_surface_2019_2020.values.reshape(14,1), columns = ['ecart surface 2019-2020'], index = prod_vege_2018.columns[2:].get_level_values(0).unique())
    surf_2020_2021 = pd.DataFrame(ecart_surface_2020_2021.values.reshape(14,1), columns = ['ecart surface 2020-2021'], index = prod_vege_2018.columns[2:].get_level_values(0).unique())
    
    variations_surf_2018_2021 = pd.concat([surf_2018_2019, surf_2019_2020, surf_2020_2021], axis = 1)
    
    variations_surf_2018_2021 = (variations_surf_2018_2021 * 100).round(2).astype(str) + '%'
    
    
 
    
    
    
    # In[23]:
    if not Path("Resources/phenologie blé 2018 2021(3).csv").is_file():
        with zipfile.ZipFile("Resources/phenologie blé 2018 2021(3).zip", 'r') as zip_ref:
            zip_ref.extractall("Resources")
     
    
    pheno_ble = pd.read_csv("Resources/phenologie blé 2018 2021(3).csv", error_bad_lines = False, sep = ';', encoding="ISO-8859-1")
    
    
    

    
    # In[425]:
    
    
    pheno_ble.drop(['kingdom', 'data_source', 'scale', 'genus', 'binomial_name'], axis=1, inplace=True)
    
    
    # In[426]:
    
    
    
    
    # In[427]:
    
    
    pheno_ble.drop_duplicates(inplace=True)
    
    
    # In[428]:
    
    
    pheno_ble.reset_index(drop=True, inplace=True)
    
    
  
    
    # In[430]:
    
    
    pheno_ble['date'] = pd.to_datetime(pheno_ble['date'],format='%d/%m/%Y', utc = True)
    
    

    
    
    # In[432]:
    
    
    pheno_ble.sort_values(by=['site_id','date'], inplace=True)
    
    
    # In[433]:
    
    
    pheno_ble.reset_index(drop=True, inplace=True)
    
    
    # In[434]:
    
    
    new_names = {'Centre':'Centre-Val de Loire','Languedoc-Roussillon':'Occitanie', 'Nord-Pas-de-Calais': 'Hauts-de-France', 'Limousin':'Nouvelle-Aquitaine','Poitou-Charentes':'Nouvelle-Aquitaine','Franche-Comté':'Bourgogne-Franche-Comté', 'Bourgogne':'Bourgogne-Franche-Comté','Auvergne':'Auvergne-Rhône-Alpes', 'Rhône-Alpes':'Auvergne-Rhône-Alpes','Champagne-Ardenne':'Grand Est','Alsace':'Grand Est','Midi-Pyrénées':'Occitanie', 'Picardie':'Hauts-de-France','Lorraine':'Grand Est', 'Aquitaine': 'Nouvelle-Aquitaine'}
    pheno_ble = pheno_ble.replace(new_names)
    
    
    # In[435]:
    
    
    pheno_ble = pheno_ble.rename({'species':'taxon'}, axis=1)
    
    

    
    # In[437]:
    
    
    stage_description = pheno_ble[pheno_ble['phenological_main_event_code'].isin(pheno_ble['phenological_main_event_code'].unique())][['phenological_main_event_code', 'phenological_main_event_description','stage_code', 'stage_description' ]].drop_duplicates()
    
    
    # In[438]:
    
    
    stage_description = stage_description.sort_values(by=['phenological_main_event_code', 'stage_code']).set_index('phenological_main_event_code')
    
    
 
    # In[447]:
    
    
    percent_category_2018 = []
    for i in pheno_ble[pheno_ble['year']== 2018]['phenological_main_event_code'].value_counts():
        percent_category_2018.append((i/len(pheno_ble[pheno_ble['year']== 2018]['phenological_main_event_code']))*100)
    percent_category_2018 = pd.DataFrame(np.array(percent_category_2018), columns = ['phenological_main_event_code 2018'], index = pheno_ble[pheno_ble['year']== 2018]['phenological_main_event_code'].value_counts().index)
    percent_category_2018 = percent_category_2018.round(2).astype(str) + '%'
    
    
    
    
    # In[449]:
    
    
    rend2018 = pd.DataFrame(prod_vege_2018.iloc[6:12, prod_vege_2018.columns.get_level_values(1)=='Rendement(q/ha)'].mean(), columns = ['2018'])
    
    

    
    
    # In[451]:
    
    
    percent_category_2019 = []
    for i in pheno_ble[pheno_ble['year']== 2019]['phenological_main_event_code'].value_counts():
        percent_category_2019.append((i/len(pheno_ble[pheno_ble['year']== 2019]['phenological_main_event_code']))*100)
    percent_category_2019 = pd.DataFrame(np.array(percent_category_2019), columns = ['phenological_main_event_code 2019'], index = pheno_ble[pheno_ble['year']== 2019]['phenological_main_event_code'].value_counts().index)
    percent_category_2019 = percent_category_2019.round(2).astype(str) + '%'
    
    
    # In[452]:
    
    
   
    
    
    # In[453]:
    
    
    rend2019 = pd.DataFrame(prod_vege_2019.iloc[6:12, prod_vege_2019.columns.get_level_values(1)=='Rendement(q/ha)'].mean(), columns = ['2019'])
    
    
  
    
    
    # In[455]:
    
    
    percent_category_2020 = []
    for i in pheno_ble[pheno_ble['year']== 2020]['phenological_main_event_code'].value_counts():
        percent_category_2020.append((i/len(pheno_ble[pheno_ble['year']== 2020]['phenological_main_event_code']))*100)
    percent_category_2020 = pd.DataFrame(np.array(percent_category_2020), columns = ['phenological_main_event_code 2020'], index = pheno_ble[pheno_ble['year']== 2020]['phenological_main_event_code'].value_counts().index)
    percent_category_2020 = percent_category_2020.round(2).astype(str) + '%'
    
    
   
    
    
    # In[457]:
    
    
    rend2020 = pd.DataFrame(prod_vege_2020.iloc[6:12, prod_vege_2020.columns.get_level_values(1)=='Rendement(q/ha)'].mean(), columns = ['2020'])
    
    
    
    
    # In[459]:
    
    # In[8]:
    #st.header('Analyse des variables météorologiques de 2018 à 2021')
    if not Path("Resources/meteo 2018 2021 (2).csv").is_file():
        with zipfile.ZipFile("Resources/meteo 2018 2021 (2).zip", 'r') as zip_ref:
            zip_ref.extractall("Resources")
    meteo_2018_2021 = pd.read_csv("Resources/meteo 2018 2021 (2).csv", sep=';', error_bad_lines = False)
    
    
    
    
    # In[11]:
    
    
    meteo_2018_2021['Date'] = pd.to_datetime(meteo_2018_2021['Date'], utc = True)
    
    
    # In[12]:
    
    
    
    
    # In[13]:
    
    
    meteo_2018_2021.drop(meteo_2018_2021[meteo_2018_2021['region (name)'] == 'Guyane'].index, inplace=True)
    meteo_2018_2021.drop(meteo_2018_2021[meteo_2018_2021['region (name)'] == 'Terres australes et antarctiques françaises'].index, inplace=True)
    meteo_2018_2021.drop(meteo_2018_2021[meteo_2018_2021['region (name)'] == 'Guadeloupe'].index, inplace=True)
    meteo_2018_2021.drop(meteo_2018_2021[meteo_2018_2021['region (name)'] == 'Saint-Pierre-et-Miquelon'].index, inplace=True)
    meteo_2018_2021.drop(meteo_2018_2021[meteo_2018_2021['region (name)'] == 'Mayotte'].index, inplace=True)
    meteo_2018_2021.drop(meteo_2018_2021[meteo_2018_2021['region (name)'] == 'La Réunion'].index, inplace=True)
    meteo_2018_2021.drop(meteo_2018_2021[meteo_2018_2021['region (name)'] == 'Martinique'].index, inplace=True)
    
    
    # In[14]:
    
    
    meteo_2018_2021 = meteo_2018_2021.sort_values(by=['Date','region (name)'])
    meteo_2018_2021.reset_index(drop =True, inplace = True)
    
    
 
    
    
    # In[15]:
    
    
    meteo_2018_2021.rename({'Visibilité horizontale': 'Visibilité horizontale (en mètre)', 'region (name)' : 'nom'}, axis=1, inplace=True)
    
    
    
    
    
    # In[17]:
    
    
    columns_to_drop = meteo_2018_2021.columns[(meteo_2018_2021.notna().sum() < 81000) == True]
    meteo_2018_2021.drop(columns_to_drop, axis=1, inplace = True)
    
    
    
    
    
    # In[19]:
    
    
    meteo_2018_2021.drop(['Type de tendance barométrique.1','region (code)','communes (code)', 'mois_de_l_annee', 'EPCI (name)', 'EPCI (code)', 'Temps présent', 'Nom', 'communes (name)','ID OMM station' ], axis=1, inplace = True)
    
    
  
    
    
    # In[21]:
    
    
    meteo_2018_2021 = meteo_2018_2021.fillna(method="ffill")
    
    
 
    
    # In[23]:
    
    
    'Deux outliers : -49.352333 et -66.663167'
    
    
    # In[24]:
    
    
    meteo_2018_2021 = meteo_2018_2021.query("Latitude != -49.352333")
    
    
    # In[25]:
    
    
    meteo_2018_2021 = meteo_2018_2021.query("Latitude != -66.663167")
    
    
    
    
    
    meteo_2018_2021['rolling_avg_temp'] = meteo_2018_2021['Température (°C)'].rolling(window=5, min_periods=1).mean()
    
    
  
    
    # In[460]:
    st.header("Prédictions pour L'année manquante 2021")
    
    train_data_pheno = pheno_ble.query("year != 2021")
    train_data_pheno = pheno_ble[['stage_code', 'date','grid_label','site_latitude','site_longitude','phenological_main_event_code']]
    
    
    # In[461]:
    
    
    train_data_meteo = meteo_2018_2021.drop(['department (name)','department (code)', 'Coordonnees','Altitude'], axis=1)
    
    
    # In[462]:
    
    
    
    
   
    
    
    # In[464]:
    
    
    train_data_meteo = train_data_meteo.loc[train_data_meteo['Température minimale sur 12 heures (°C)'].notna(), :]
    
    
    # In[465]:
    
    
    train_data_pheno.rename({'grid_label':'nom', 'date':'Date'}, axis=1, inplace = True)
    
    
    # In[466]:
    
    
    train_data = pd.merge(train_data_meteo,train_data_pheno, on=['nom', 'Date'])
    
    
    # In[467]:
    
    
    train_data.drop(['site_latitude','site_longitude', 'Latitude','Longitude'], axis= 1, inplace = True)
    
    
    # In[468]:
    
    
    
    
    # In[469]:
    
    
    train_data.drop_duplicates(inplace=True)
    
    
    # In[470]:
    
    st.markdown("Merging de météo et phénologie sans l'année 2021 ")
    st.write(train_data.head())
    
    
    # In[471]:
    if st.button('Table de corrélation'):
    
        st.write(train_data.corr())
    
    
    st.markdown('**Selon le tableau de corrélation, la variable météorologique la plus corrélée au stade de développement du blé est la température**')
    # In[474]:
    st.markdown('Test ANOVA pour déterminer la corrélation entre une variable catégorielle et une variable numérique continue')
    variable = st.selectbox('Variable Numérique continue',['Température (°C)','rolling_avg_temp','Précipitations dans les 24 dernières heures','Humidité'])
    if variable == 'Température (°C)':
        st.image('Resources/ANOVA temp.png')
    # In[475]:
    
    if variable == 'rolling_avg_temp' : 
        st.image('Resources/ANOVA rolling_avg_temp.png')

    
    # In[476]:
    
    if variable == 'Précipitations dans les 24 dernières heures' :
        st.image('Resources/ANOVA Precipitations.png')
          
                
    # In[477]:
    
    
    if variable == 'Humidité':
        st.image('Resources/ANOVA Humidite.png')
       
    
    train_data = pd.concat([pd.get_dummies(train_data.nom), train_data], axis =1)
    
    
    # In[479]:
    
    st.markdown("Les variables météorologiques les plus corrélées sont la température et l'humidité")
    train_data.drop(['nom','Précipitations dans la dernière heure',
       'Précipitations dans les 3 dernières heures',
       'Précipitations dans les 6 dernières heures',
       'Précipitations dans les 12 dernières heures',
       'Précipitations dans les 24 dernières heures','Pression au niveau mer','Variation de pression en 3 heures','Type de tendance barométrique','Direction du vent moyen 10 mn','Vitesse du vent moyen 10 mn', 'Point de rosée','Visibilité horizontale (en mètre)',"Nebulosité totale","Nébulosité  des nuages de l' étage inférieur","Hauteur de la base des nuages de l'étage inférieur",'Pression station','Variation de pression en 24 heures', 'Rafale sur les 10 dernières minutes','Rafales sur une période','Periode de mesure de la rafale','Etat du sol','Hauteur totale de la couche de neige, glace, autre au sol', 'Nébulosité couche nuageuse 1','Hauteur de base 1','Nébulosité couche nuageuse 2','Hauteur de base 2', 'Température','Température minimale sur 12 heures','Température maximale sur 12 heures','Température minimale du sol sur 12 heures'], axis=1, inplace = True)
    
    
    # In[480]:
    
    
    train_data['year'] = train_data.Date.dt.year
    train_data['month'] = train_data.Date.dt.month
    train_data['day'] = train_data.Date.dt.day
    
    
    # In[481]:
    
    
    train_data.drop('Date', axis=1, inplace=True)
    
    
    # In[482]:
    
    
    
    
    # In[483]:
    
    
    data = train_data.drop(['stage_code','phenological_main_event_code'], axis=1)
    target = train_data['phenological_main_event_code']
    
    
    # In[484]:
    
    
    
    
    # In[485]:
    
    
    test_2021 = meteo_2018_2021[meteo_2018_2021['Date'].dt.year == 2021].drop(['Pression au niveau mer','Précipitations dans la dernière heure',
       'Précipitations dans les 3 dernières heures',
       'Précipitations dans les 6 dernières heures',
       'Précipitations dans les 12 dernières heures',
       'Précipitations dans les 24 dernières heures','Variation de pression en 3 heures','Type de tendance barométrique','Direction du vent moyen 10 mn','Vitesse du vent moyen 10 mn', 'Point de rosée','Visibilité horizontale (en mètre)',"Nebulosité totale","Nébulosité  des nuages de l' étage inférieur","Hauteur de la base des nuages de l'étage inférieur",'Pression station','Variation de pression en 24 heures', 'Rafale sur les 10 dernières minutes','Rafales sur une période','Periode de mesure de la rafale','Etat du sol','Hauteur totale de la couche de neige, glace, autre au sol', 'Nébulosité couche nuageuse 1','Hauteur de base 1','Nébulosité couche nuageuse 2','Hauteur de base 2', 'Température','Température minimale sur 12 heures','Température maximale sur 12 heures','Température minimale du sol sur 12 heures', 'Coordonnees','department (name)','department (code)','Altitude', 'Latitude','Longitude'], axis=1)
    test_2021 = test_2021.loc[train_data_meteo['Température minimale sur 12 heures (°C)'].notna(), :]
    
    
    pheno_ble2 = pheno_ble[pheno_ble['year']==2018].sort_values(by='date').rename({'date':'Date'}, axis = 1).reset_index(drop=True)    
    
    # In[489]:
    test_2021 = test_2021.sort_values(by=['Date','nom'])
    test_2021 = test_2021.iloc[::2]
    test_2021 = test_2021.iloc[::2]
    test_2021 = test_2021.iloc[::2]
    
    test_2021 = test_2021.sample(n=9393, random_state=42)
    
    test_2021 = test_2021.sort_values(by='Date').reset_index(drop=True)
    
    # In[490]:
    
    
    for i in range(len(test_2021)):
        test_2021['Date'][i] = pd.to_datetime('2021-' + pheno_ble2['Date'].iloc[i].strftime('%m-%d'))
    test_2021['Date'] = pd.to_datetime(test_2021['Date'])
    
    # In[491]:
    
    test_2021 = pd.concat([test_2021, pd.get_dummies(test_2021['nom'])], axis=1)

    test_2021.drop('nom', axis=1, inplace=True)
    
    
    # In[492]:
    
    
    test_2021['year'] = test_2021.Date.dt.year
    test_2021['month'] = test_2021.Date.dt.month
    test_2021['day'] = test_2021.Date.dt.day
    test_2021.drop('Date', axis=1, inplace=True)
    
    
    # In[493]:
    
    
    test_2021.drop('Corse', axis=1, inplace=True)
    
    
    # In[494]:
    
    
    
    
    # In[495]:
    
    
    
    
    # In[496]:
    
    
    test_2021.drop_duplicates(inplace=True)
    st.subheader("Recherche de l'algorithme le plus efficient pour prédire les stades de croissance du blé de 2021")
    
    # In[497]:
    
    
    from sklearn.model_selection import GridSearchCV
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import precision_score
    from sklearn.model_selection import train_test_split
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.ensemble import GradientBoostingClassifier

    
    # In[498]:
   
    
    X_train, X_test, y_train, y_test = train_test_split(data, target, test_size = 0.2, random_state = 123)
    
    X_train.sort_index(axis=1, inplace=True)
    test_2021.sort_index(axis=1, inplace=True)
    X_test.sort_index(axis=1, inplace=True)
    # In[499]:
    
    
    from sklearn import preprocessing
    scaler = preprocessing.StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    test_2021_scaled = scaler.transform(test_2021)

    
    
    # In[501]:
    
    alg = st.selectbox('Algorithme de Classification', ['Decision Tree','Random Forest','Gradient Boosting','KNN'])
    if alg == 'Decision Tree':
    
        
        
        # In[524]:
        
        clf_entr = DecisionTreeClassifier(criterion = 'entropy', max_depth = 9,min_samples_split = 7)
        clf_entr.fit(X_train_scaled, y_train)
        joblib.dump(clf_entr,'decision_tree_model.joblib')

        loaded_clf_entr = joblib.load('decision_tree_model.joblib')

        y_pred = loaded_clf_entr.predict(X_test_scaled)
        st.write(pd.crosstab(y_pred, y_test))
        
        
        # In[525]:
        
        
        st.write(f'accuracy score DT :  {loaded_clf_entr.score(X_test_scaled, y_test).round(3)}')
   
        st.write(f'precision score DT : {precision_score(y_pred, y_test, average = "weighted").round(3)}')
        
        
        # In[528]:
        
        
        y_pred_2021 = loaded_clf_entr.predict(test_2021_scaled)
        
        
        # In[529]:
        
        
        st.write(f'prédictions 2021 DT : {np.unique(y_pred_2021)}')
    if alg == 'Random Forest':
        rf = RandomForestClassifier(max_depth =  10, min_samples_split = 10, n_estimators = 50)
        
        
        # In[502]:
        
        
        rf.fit(X_train_scaled, y_train)

        joblib.dump(rf, 'random_forest_model.joblib')

        loaded_rf = joblib.load('random_forest_model.joblib')

        y_pred_rf = loaded_rf.predict(X_test_scaled)
        st.write(pd.crosstab(y_pred_rf, y_test))
        st.write(f'score RF : {loaded_rf.score(X_test_scaled, y_test).round(3)}')
        
        
        # In[503]:
  
        
        st.write(f'precision score RF : {precision_score(y_pred_rf, y_test, average = "weighted").round(3)}')
        
        
        # In[506]:
        
        
        
        
        # In[507]:
        
        
        y_pred_2021_rf = loaded_rf.predict(test_2021_scaled)
        st.write(f'prédictions 2021 RF : {np.unique(y_pred_2021_rf)}')
        

    # In[508]:
    if alg == 'Gradient Boosting':
    
        
        gb = GradientBoostingClassifier(n_estimators = 100, max_depth = 7, learning_rate = 0.01, subsample = 1)
        
        
        # In[509]:
        
        
        gb.fit(X_train_scaled, y_train)
        joblib.dump(gb,'gradient_bossting_model.joblib')

        loaded_gb = joblib.load('gradient_bossting_model.joblib')

        y_pred_gb = loaded_gb.predict(X_test_scaled)
        st.write(pd.crosstab(y_pred_gb, y_test))
        st.write(f'score GB : {loaded_gb.score(X_test_scaled, y_test).round(3)}')
        
        
        # In[510]:
        
      
        
        # In[511]:
        
        
        st.write(f'precision score GB: {precision_score(y_pred_gb, y_test, average = "weighted").round(3)}')
        
        
        # In[512]:
        
        
        y_pred_2021_gb = loaded_gb.predict(test_2021_scaled)
        st.write(f'prédictions 2021 GB : {np.unique(y_pred_2021_gb)}')
        
        
    # In[513]:
    
    
    
    # In[520]:
    if alg == 'KNN':
    
        
        knn = KNeighborsClassifier(n_neighbors=5)
        
        knn.fit(X_train_scaled, y_train)
        
        joblib.dump(knn,'knn_model.joblib')

        loaded_knn = joblib.load('knn_model.joblib')

        y_pred_knn = loaded_knn.predict(X_test_scaled)
        
        
        st.write(pd.crosstab(y_pred_knn, y_test))

        # In[521]:
        st.write(f'accuracy score KNN :  {loaded_knn.score(X_test_scaled, y_test).round(3)}')

        
        st.write(f'precision score KNN: {precision_score(y_pred_knn, y_test, average = "weighted").round(3)}')
        
        
        # In[522]:
        
        
        y_pred_knn_2021 = loaded_knn.predict(test_2021_scaled)
        st.write(f'prédictions 2021 KNN : {np.unique(y_pred_knn_2021)}')
    
    
    # In[523]:
    
    
    st.markdown('Modèle le plus performant : Decision Tree')
    
    
    # In[530]:
    clf_entr = DecisionTreeClassifier(criterion = 'entropy', max_depth = 9,min_samples_split = 7)
    clf_entr.fit(X_train_scaled, y_train)
    joblib.dump(clf_entr,'dt_model.joblib')

    loaded_dt = joblib.load('dt_model.joblib')
            
    y_pred_2021 = loaded_dt.predict(test_2021_scaled)

    test_2021['phenological_main_event_code'] = y_pred_2021
    
    
    # In[531]:
    
    
    
    
    # In[532]:
    
    
    pheno_meteo = pd.concat([train_data, test_2021])
    pheno_meteo['régions'] = pheno_meteo[['Auvergne-Rhône-Alpes','Bourgogne-Franche-Comté','Bretagne','Centre-Val de Loire','Grand Est','Hauts-de-France','Normandie','Nouvelle-Aquitaine','Occitanie','Pays de la Loire',"Provence-Alpes-Côte d'Azur",'Île-de-France']].idxmax(axis=1)
    
    
    # In[533]:
    
    
    pheno_meteo.drop(['Auvergne-Rhône-Alpes','Bourgogne-Franche-Comté','Bretagne','Centre-Val de Loire','Grand Est','Hauts-de-France','Normandie','Nouvelle-Aquitaine','Occitanie','Pays de la Loire',"Provence-Alpes-Côte d'Azur",'Île-de-France'], axis=1, inplace=True)
    
    
    # In[534]:
    
    
    pheno_meteo['date'] = pd.to_datetime(pheno_meteo[['year', 'month', 'day']])
    
    
    # In[535]:
    
    
    
    
  
    
    # In[301]:
    
    
    # In[302]:
    
    
    percent_category_2021 = []
    for i in pheno_meteo[pheno_meteo['year']== 2021]['phenological_main_event_code'].value_counts():
        percent_category_2021.append((i/len(pheno_meteo[pheno_meteo['year']== 2021]['phenological_main_event_code']))*100)
    percent_category_2021 = pd.DataFrame(np.array(percent_category_2021), columns = ['phenological_main_event_code 2021'], index = pheno_meteo[pheno_meteo['year']== 2021]['phenological_main_event_code'].value_counts().index)
    percent_category_2021 = percent_category_2021.round(2).astype(str) + '%'
    
    
    # In[303]:
    
    
    rend2021 = pd.DataFrame(prod_vege_2021.iloc[6:12, prod_vege_2021.columns.get_level_values(1)=='Rendement(q/ha)'].mean(), columns = ['2021'])
    
    
    # In[304]:
    button = st.button('Comparaison de la distribution des différents stades de croissance et du rendement pour 2021')
    if button :     
        st.write(percent_category_2021)
        st.write(rend2021.iloc[0,:])
        
    
    # In[308]:
    
    
    st.markdown("**Le stade 3 représente en moyenne environ 30% de la durée totale du cycle de croissance du végétal et son rendement est de 60 q/h. Des chiffres à peu près similaires à ce qu'on a pu observé pour les autres années.**")
    
    # In[73]:
    st.header('Prédictions pour 2100')
    
    page = urlopen('https://www.linfodurable.fr/environnement/38-degres-en-2100-rechauffement-climatique-pire-que-prevu-en-france-34833')
    soup = bs(page, 'html.parser')
    
    
    # In[74]:
    
    
    
    # In[76]:
    
    st.subheader("Prédictions des stades phénologiques du blé en 2100 à partir des prédictions sur les températures du rapport du GIEC pour l'année 2100")
    texte1 = soup.find('h2',{'class':'font-medium fs-20 node-20'}).text.strip()
    
    
    # In[77]:
    
    
    tokenizer = PunktSentenceTokenizer()
    texte = tokenizer.tokenize(texte1)
    
    
    # In[78]:
    
    
    texte2 = tokenizer.tokenize(soup.find('div', {'class':'clearfix text-formatted field field--name-field-article-body field--type-text-with-summary field--label-hidden field__item'}).text.strip())
    
    
    # In[84]:
    
    
    
    
    # In[80]:
    
    
    pred_giec_meteo = texte,TreebankWordDetokenizer().detokenize(texte2[10:18])
    
    pred_giec_meteo = str(pred_giec_meteo)
    
    
    import re
    pred_giec_meteo = re.sub(r"\\", "", pred_giec_meteo)
    button = st.button('**Rapport GIEC météo**')
    if button :
        st.write(pred_giec_meteo)
    
    
    # In[235]:
    
    
    st.markdown("Nous allons maintenant utiliser les informations du rapport du GIEC concernant les prédictions de hausses de températures. En 2100 les températures augmenteront en moyenne de 3.8°C, mais en hiver de 3.2°C et en été de 5.1°C. Nous allons donc augmenter en conséquence les températures de notre dataset météo et prédire les stades de croissance du blé.")
    
    
    # In[236]:
    
    
    
    
    # In[237]:
    
    
    st.markdown("Pour réaliser les prédictions, prenons comme référence l'année 2018. C'est celle pour laquelle nous avons le plus de données (du dataframe pheno_ble).")
    
    
    # In[309]:
    
    
    pheno_meteo_pred_train = pheno_meteo[pheno_meteo['year'] == 2018].drop(['date','stage_code','phenological_main_event_code'], axis=1)
    
    
    # In[310]:
    
    
    pheno_meteo_pred_train['year'] = pheno_meteo_pred_train['year'].replace(2018, 2100)
    
    
    # In[311]:
    
    
    pheno_meteo_pred_train = pd.concat([pd.get_dummies(pheno_meteo_pred_train['régions']), pheno_meteo_pred_train], axis =1).drop('régions', axis=1)
    
    
    # In[312]:
    
    
    
    
    # In[313]:
    
    
    pheno_meteo_pred_train.loc[(pheno_meteo_pred_train['month'] <= 4) | (pheno_meteo_pred_train['month'] >= 9),'Température (°C)'] += 3.2
    pheno_meteo_pred_train.loc[(pheno_meteo_pred_train['month'] > 4) & (pheno_meteo_pred_train['month'] < 9),'Température (°C)'] += 5.1
    pheno_meteo_pred_train.loc[(pheno_meteo_pred_train['month'] <= 4) | (pheno_meteo_pred_train['month'] >= 9),'Température minimale sur 12 heures (°C)'] += 3.2
    pheno_meteo_pred_train.loc[(pheno_meteo_pred_train['month'] > 4) & (pheno_meteo_pred_train['month'] < 9),'Température minimale sur 12 heures (°C)'] += 5.1
    pheno_meteo_pred_train.loc[(pheno_meteo_pred_train['month'] <= 4) | (pheno_meteo_pred_train['month'] >= 9),'Température maximale sur 12 heures (°C)'] += 3.2
    pheno_meteo_pred_train.loc[(pheno_meteo_pred_train['month'] > 4) & (pheno_meteo_pred_train['month'] < 9),'Température maximale sur 12 heures (°C)'] += 5.1
    pheno_meteo_pred_train.loc[(pheno_meteo_pred_train['month'] <= 4) | (pheno_meteo_pred_train['month'] >= 9),'Température minimale du sol sur 12 heures (en °C)'] += 3.2
    pheno_meteo_pred_train.loc[(pheno_meteo_pred_train['month'] > 4) & (pheno_meteo_pred_train['month'] < 9),'Température minimale du sol sur 12 heures (en °C)'] += 5.1
    pheno_meteo_pred_train.loc[(pheno_meteo_pred_train['month'] <= 4) | (pheno_meteo_pred_train['month'] >= 9),'rolling_avg_temp'] += 3.2
    pheno_meteo_pred_train.loc[(pheno_meteo_pred_train['month'] > 4) & (pheno_meteo_pred_train['month'] < 9),'rolling_avg_temp'] += 5.1
    
    
    # In[314]:
    
    
    
    pheno_meteo_pred_train.sort_index(axis=1, inplace=True)
    # In[315]:
    
    
    pheno_meteo_pred_train_scaled = scaler.transform(pheno_meteo_pred_train)
    
    
    # In[316]:
    st.markdown("**Algorithme Decision Tree (utilisé précedemment) pour prédire les stades de l'année 2100**")

    clf_entr = DecisionTreeClassifier(criterion = 'entropy', max_depth = 9,min_samples_split = 7)
    clf_entr.fit(X_train_scaled, y_train)
    joblib.dump(clf_entr, 'decision_tree_model.joblib')
    loaded_clf_entr = joblib.load('decision_tree_model.joblib')

    y_pred_2100 = loaded_clf_entr.predict(pheno_meteo_pred_train_scaled)
    
    
    # In[317]:
    
    
    st.write(f'**Stades prédits : {np.unique(y_pred_2100)}**')
    
    
    # In[318]:
    
    
    pheno_meteo_pred_train['phenological_main_event_code'] = y_pred_2100
    
    
    # In[319]:
    
    
    
    
    # In[320]:
    
    
    pheno_meteo_pred_train['régions'] = pheno_meteo_pred_train[['Auvergne-Rhône-Alpes','Bourgogne-Franche-Comté','Bretagne','Centre-Val de Loire','Grand Est','Hauts-de-France','Normandie','Nouvelle-Aquitaine','Occitanie','Pays de la Loire',"Provence-Alpes-Côte d'Azur",'Île-de-France']].idxmax(axis=1)
    pheno_meteo_pred_train.drop(['Auvergne-Rhône-Alpes','Bourgogne-Franche-Comté','Bretagne','Centre-Val de Loire','Grand Est','Hauts-de-France','Normandie','Nouvelle-Aquitaine','Occitanie','Pays de la Loire',"Provence-Alpes-Côte d'Azur",'Île-de-France'], axis=1, inplace=True)
    pheno_meteo_pred_train['date'] = pd.to_datetime(pheno_meteo_pred_train[['year', 'month', 'day']])
    
    
    
    # In[321]:
    
    
    percent_category_2100 = []
    for i in pheno_meteo_pred_train['phenological_main_event_code'].value_counts():
        percent_category_2100.append((i/len(pheno_meteo_pred_train['phenological_main_event_code']))*100)
    percent_category_2100 = pd.DataFrame(np.array(percent_category_2100), columns = ['phenological_main_event_code 2100'], index = pheno_meteo_pred_train['phenological_main_event_code'].value_counts().index)
    percent_category_2100 = percent_category_2100.round(2).astype(str) + '%'
    
    
    # In[322]:
    st.markdown('Comparaison des distributions des années 2018 et 2100 des stades de croissance du blé.')
    dist = st.selectbox('Année',['2018','2100'])
    if dist == '2018':
        st.write(percent_category_2018)
    
    
    # In[323]:
    
    if dist == '2100':
        st.write(percent_category_2100)
    
    
    # In[251]:
    
    
    st.markdown("Comme démontré précedemment, le stade déterminant pour une bonne récolte est le stade de montaison à 1cm d'épi qui correspond au stade 3. On en compte moins en 2100 qu'en 2018. On peut donc supposer que selon ces prédictions, le stade sera plus court, le rendement aura donc tendance à être plus faible en 2100.")
    
    