#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 14:01:28 2018

@author: lydia
"""


import requests
def download_file(url, output_file):

    headers = {}
    r = requests.get(url, headers=headers, stream=True)

    with open(output_file, 'wb') as f: 
        for chunk in r.iter_content(chunk_size=4096): 
            if chunk: 
                f.write(chunk)
        f.flush()

    return output_file


folder_path = "./downloads/"

population = 'https://data.cityofnewyork.us/api/views/xywu-7bv9/rows.csv?accessType=DOWNLOAD'
felony = 'https://data.cityofnewyork.us/api/views/2fra-mtpn/rows.csv?accessType=DOWNLOAD'
library = 'https://data.cityofnewyork.us/api/views/feuq-due4/rows.csv?accessType=DOWNLOAD'
rodent = 'https://data.cityofnewyork.us/api/views/p937-wjvj/rows.csv?accessType=DOWNLOAD'
tree = 'https://data.cityofnewyork.us/api/views/uvpi-gqnh/rows.csv?accessType=DOWNLOAD'


print("Téléchargement des données (peut prendre quelques minutes)")
print("----")
print("----")
print("Téléchargement de Population.csv")
download_file(population, folder_path+"Population.csv")
print("Téléchargement de Population.csv terminé")
print("--")
print("Téléchargement de Felonies.csv")
download_file(felony,folder_path+"Felonies.csv")
print("Téléchargement de Felonies.csv terminé")
print("--")
print("Téléchargement de Libraries.csv")
download_file(library,folder_path+"Libraries.csv")
print("Téléchargement de Libraries.csv terminé")
print("--")
print("Téléchargement de Rodents.csv")
download_file(rodent,folder_path+"Rodents.csv")
print("Téléchargement de Rodents.csv terminé")
print("--")
print("Téléchargement de Trees.csv")
download_file(tree,folder_path+"Trees.csv")
print("Téléchargement de Trees.csv terminé")
print("----")
print("----")
print("Téléchargement terminé") 