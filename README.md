# DjangoApollon
Projet Python réalisé en Django 3.
Il s'agit d'un site de création de playlist, d'écoute de titres

# Fonctionnalités 
- Rechercher parmi des millions de titres, avec le câblage avec les API d'Apple Music et de Genius. Découvrez des détails sur les paroles, l'artiste, ou l'album.
- Créez des playlists. Partagez-les avec vos amis ou gardez-les privées.
- Authentification sécurisée 
  - Confirmation de compte par mail (génération de token)
  - Procédure d'oubli de mot de passe sécurisée (chaînée, génération de token)
- Suivez d'autres utilisateurs, découvrez leurs playlists.

# Base de données 
Une base de données d'exemple a été créée à des fins de tests et d'exemples.
Pour l'utiliser, il vous suffit d'exécuter à la racine du projet :
```bash
cp -f ./example/sample.sqlite3 apollon.sqlite3
```
Le superutilisateur est alors accessible :
- username : apollon-admin
- password : apollondjango