# cic-IDS


Système de détection d'intrusion (IDS) basé sur l'apprentissage automatique

## ▶ Résumé du projet 

Le projet implique les étapes suivantes :

- Surveillance du flux de trafic : Le système sera configuré pour capturer le flux de trafic entrant et sortant sur un réseau.

- Extraction des données pertinentes : Les données pertinentes telles que les adresses IP source et destination, les ports, les protocoles, la durée des connexions, etc., seront extraites à partir du flux de trafic capturé.

- Enregistrement dans un fichier CSV : Les données extraites seront directement enregistrées dans un fichier CSV. Chaque ligne du fichier CSV représentera une observation unique du flux de trafic, avec ses attributs correspondants.

- Analyse des corrélations : Un fichier CSV distinct, généré à l'aide de CICFlowMeter ou d'un outil similaire, sera utilisé pour analyser les corrélations des données. Cela peut inclure des informations sur les schémas de trafic, les caractéristiques des paquets, etc.

- Normalisation des données : Avant d'appliquer l'apprentissage automatique, les données seront normalisées pour mettre à l'échelle les valeurs des attributs et les rendre comparables.

- Détection des attaques et du trafic régulier : En utilisant des techniques d'apprentissage automatique telles que les algorithmes de classification, le système sera formé pour distinguer entre les attaques et le trafic réseau régulier. Cela nécessitera l'utilisation d'un jeu de données étiqueté pour l'entraînement.

En résumé, le projet vise à automatiser la surveillance et la détection d'attaques dans le trafic réseau en utilisant des techniques d'analyse de données et d'apprentissage automatique, avec un accent particulier sur l'enregistrement direct des données dans un format CSV pour une analyse ultérieure.

## ⚛ CIC-FLOWMETER 

 CICFlowMeter is a network traffic flow generator available from here . It can be used to generate bidirectional flows, where the first packet determines the forward (source to destination) and backward (destination to source) directions, hence the statistical time-related features can be calculated separately in the forward and backward directions. Additional functionalities include, selecting features from the list of existing features, adding new features, and controlling the duration of flow timeout. 
