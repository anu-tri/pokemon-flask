from flask import Flask, render_template, request

import requests


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html.j2')


@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
    if request.method == 'POST':
        name = request.form.get('pokemon_name').lower()
        url = f'https://pokeapi.co/api/v2/pokemon/{name}'
        response = requests.get(url)
        pokemon_details = []
        
        if response.ok:
                #request worked
                if not response.json():
                    return "Error loading pokemon details."
                pokemon = response.json()
                
                pokemon_data={
                    'id': pokemon['id'],
                    'name': pokemon['name'],
                    'order': pokemon['order'],
                    'hp': pokemon['stats'][0]['base_stat'],
                    'defense': pokemon['stats'][2]['base_stat'],
                    'attack': pokemon['stats'][1]['base_stat'],
                    'url': pokemon['sprites']['front_shiny']
                }
                pokemon_details.append(pokemon_data)
        else:
            # The request fail
            return "<h3>We have a problem. Please search for another pokemon.<h3>"
                
        return render_template('pokemon.html.j2', pokemon=pokemon_details)   
    return render_template('pokemon.html.j2')  


if __name__ == '__main__':
    app.debug = True
    app.run()
