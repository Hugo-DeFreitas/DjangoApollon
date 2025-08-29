# DjangoApollon
Python project built with Django 3.
It’s a playlist creation and music listening website (Spotify clone), that showcases Django/Pythion best practices and capabilities

# Features 
- Search among millions of songs, thanks to integrations with the Apple Music and Genius APIs.
- Discover detailed information about lyrics, artists, and albums.
- Create playlists. Share them with friends, or keep them private.
- Secure authentication.
- Email account confirmation using token generation.
-	Secure password reset flow (chained steps with token generation).
-	Follow other users, and discover their playlists.

# Database
A sample database is available for testing and demo purposes.
To use it, run the following command at the root of the project:

```bash
cp -f ./example/sample.sqlite3 apollon.sqlite3
```
The superuser credentials are:
- username: apollon-admin
- password: apollondjango
