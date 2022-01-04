# generateurConfigRouteurs

## Explications

Ce script Python utilise le moteur de template Jinja pour générer des configurations de routeurs afin de faciliter le déploiement d'un nouveau SDIS. Une fois lancé, le script demande le numéro du SDIS à générer. 
Il crée deux fichiers texte correspondants à la configuration des deux routeurs :  
- Un routeur SDIS qui est le point de sortie du réseau du SDIS
- Un routeur BBN qui permet de connecter le SDIS au backbone    

Tous les routeurs BBN sont connectés à trois autres routeurs : R5, R6 (pour assurer de la redondance) et au SDIS généré.  

## Procédure pour créer un nouveau SDIS
- Ajouter et renommer deux routeurs c7200 sur la topologie GNS3 (un dans le backbone et un pour le SDIS)
- Ajouter sur le routeur BBN-Rx deux interfaces Ethernet (Configure -> Slots -> slot 3: PA-2FE-TX)  
 Si besoin ajouter aussi ces interfaces sur les routeurs R5 et R6
- Connecter le routeur BBN-Rx à BBN-R5 (interface f0/0 de BBN-Rx) et BBN-R6 (interface f0/1 de BBN-Rx)
- Configurer les adresses IP sur les interfaces utilisées de BBN-R5 et BBN-R6 et les activer en respectant la stratégie d'adressage
- Connecter le routeur BBN-Rx (f3/0) au routeur du SDIS (f0/0)
- Ajouter un switch et le connecter au nouveau routeur du SDIS (f0/1)
- Ajouter un ordinateur (VPCS) et le connecter au switch
- Exécuter le script **routerConfigGen.py** puis rentrer le numéro du SDIS à générer
- Injecter le contenu des deux fichiers textes générés dans les routeurs correspondants au nom
- Essayer d'exécuter la commande **ip dhcp** sur le VPCS pour vérifier que la connexion est fonctionnelle

### Exemple pour le déploiement du SDIS-3
![image](https://user-images.githubusercontent.com/71138452/148044142-8fbc6384-a565-4f42-a54c-e25801f9182b.png)
