# Exemple en Python avec Flask
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/dm/user_updates.json', methods=['GET'])
def get_user_updates():
    # Récupérer les données de la conversation
    conversation_id = request.args.get('conversation_id')
    cursor = request.args.get('cursor')
    
    # Récupérer les messages de la conversation depuis la base de données ou ailleurs
    
    # Générer la réponse JSON
    response_data = {
        'conversation_id': conversation_id,
        'messages': ['Message 1', 'Message 2', 'Message 3']  # Exemple de données
    }
    
    # Créer la réponse HTTP
    response = jsonify(response_data)
    
    # Mauvaise configuration : Ne pas spécifier d'en-tête Cache-Control
    return response

if __name__ == '__main__':
    app.run(debug=True)
