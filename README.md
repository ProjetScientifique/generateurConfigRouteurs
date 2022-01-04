# generateurConfigRouteurs

## Explications

Ce script Python utilise le moteur de template Jinja pour générer des configurations de routeurs afin de faciliter le déploiement d'un nouveau SDIS. Une fois lancé, le script demande le numéro du SDIS à générer. 
Il crée deux fichiers texte correspondants à la configuration des deux routeurs :  
- Un routeur SDIS qui est le point de sortie du réseau du SDIS
- Un routeur BBN qui permet de connecter le SDIS au backbone    

Tous les routeurs BBN sont connectés à trois autres routeurs : R5, R6 (pour assurer de la redondance) et au SDIS généré.  
### Exemple pour le déploiement du SDIS-3
![image](https://user-images.githubusercontent.com/71138452/148044142-8fbc6384-a565-4f42-a54c-e25801f9182b.png)
