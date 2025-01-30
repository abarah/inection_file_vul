from flask import Flask, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

# Répertoire de téléchargement des fichiers
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Acceptation de tous les types de fichiers (vulnérabilité)
ALLOWED_EXTENSIONS = {'*'}  # Aucun contrôle des extensions des fichiers téléchargés

def allowed_file(filename):
    # La fonction n'effectue aucune vérification sur le fichier, ce qui est une mauvaise pratique.
    return True

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Postuler à un stage</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background-color: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                width: 400px;
                text-align: center;
            }
            h1 {
                font-size: 24px;
                color: #333;
            }
            form {
                margin-top: 20px;
            }
            input[type="file"],
            input[type="text"],
            input[type="email"] {
                padding: 10px;
                font-size: 16px;
                margin-bottom: 15px;
                border: 1px solid #ccc;
                border-radius: 4px;
                width: 100%;
                box-sizing: border-box;
            }
            input[type="submit"] {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 16px;
                width: 100%;
            }
            input[type="submit"]:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Postuler à un stage</h1>
            <form method="POST" action="/upload" enctype="multipart/form-data">
                <input type="text" name="name" placeholder="Votre nom" required>
                <input type="email" name="email" placeholder="Votre email" required>
                <input type="file" name="file" required>
                <input type="submit" value="Envoyer la candidature">
            </form>
        </div>
    </body>
    </html>
    '''

@app.route('/upload', methods=['POST'])
def upload_file():
    # Récupérer les informations du formulaire
    name = request.form['name']
    email = request.form['email']
    
    # Vérifie s'il y a un fichier dans la requête
    if 'file' not in request.files:
        return 'Aucun fichier sélectionné'

    file = request.files['file']
    
    # Si le nom du fichier est vide
    if file.filename == '':
        return 'Aucun fichier sélectionné'

    # Si le fichier est valide (aucun contrôle de type)
    if file and allowed_file(file.filename):
        # Le fichier sera sauvegardé sans aucun contrôle de sécurité
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        # Retourner un message avec les détails de la candidature
        return f'Candidature envoyée avec succès ! Nom: {name}, Email: {email}, Fichier: {filename}'

    return 'Le fichier téléchargé n\'est pas valide'

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    # Permet d'afficher un fichier téléchargé (attention à la sécurité)
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    # Crée le dossier de téléchargement s'il n'existe pas
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    app.run(debug=True, host='0.0.0.0')
