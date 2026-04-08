from flask import Flask, render_template, request

app = Flask(__name__)

# Modern brands use emotional descriptions
perfumes = [
    {
        "id": 1,
        "name": "Vampire Blood",
        "price": "250",
        "size": "15ml",
        "description": "Top Notes: Bergamot, Sweet Strawberry, Blood-Red BerriesMiddle Notes: Midnight Blooming Jasmine, Red BerriesBase Notes: Dark Plum, Black Musk, Green Leaves",
        "image": "vampire_blood.webp" # Make sure this is in your static folder!
    },
    {
        "id": 2,
        "name": "Hawas Ice",
        "price": "250",
        "size": "15ml",
        "description": "Top Notes: Frozen Apple, Italian Bergamot, Italian Lemon, Star AniseMiddle Notes: Orange Blossom, Plum, CardamomBase Notes: Moss, Driftwood, Amber, Musk",
        "image": "hawas_ice.webp"
    },
    {
        "id": 3,
        "name": "Dior Sauvage",
        "price": "250",
        "size": "15ml",
        "description": "Top Notes: Calabrian BergamotMiddle Notes: Sichuan Pepper, Lavender, Star Anise, NutmegBase Notes: Ambroxan, Papua New Guinean Vanilla ",
        "image": "dior_sauvage.jfif"
    }
]

@app.route('/')
def home():
    return render_template('index.html', products=perfumes)
@app.route('/search')
def search():
    # This gets the word someone typed into the search bar
    query = request.args.get('query', '').lower()
    
    # This filters your perfume list by name
    filtered_products = [p for p in perfumes if query in p['name'].lower()]
    
    # This reloads the page showing only the matching perfumes
    return render_template('index.html', products=filtered_products)
import os

if __name__ == '__main__':
    # This line lets Render tell the app which port to use
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
