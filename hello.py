#!/usr/bin/python3
# -*- coding: utf-8 -*

import cgi 

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

html = """<!DOCTYPE html>
<head>
    <title>Bonjour</title>
</head>
<body>
	<!DOCTYPE html>
<body>
<style>
h1
{
color:red;
}
</style>
	<h1>Bienvenue sur mon site</h1>
<form method="POST" action="/formulaire.py">
<legend>Inscription</legend>
<input type="text" name="nom" placeholder="Nom"  />
<br />
<input type="text" name="prenom" placeholder="Prenom"  />
<br />
<input type="text" password="mot de passe" placeholder="Mot de passe" />
<br />
<input type="submit" class="btn btn-primary" value="Valider" />
<background-image>
<img src="/image/callout.jpg" />
</background-image>
</form>
</body>
</html>
</body>
</html>
"""

print(html)