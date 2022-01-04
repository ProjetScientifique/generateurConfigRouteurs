# generateurConfigRouteurs

Ce script Python utilise le moteur de template Jinja pour générer des configurations de routeurs afin de faciliter le déploiement d'un nouveau SDIS.
Une fois lancé, le script demande le numéro du SDIS à générer. Il crée deux fichiers correspondants aux deux routeurs.
Un routeur SDIS qui est le point de sortie du réseau du SDIS et un routeur BBN qui permet de connecter le SDIS au backbone.
Tous les routeurs BBN sont connectés à trois autres routeurs : R5, R6 (pour assurer de la redondance) et au SDIS généré.
