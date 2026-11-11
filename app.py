from flask import Flask, render_template, request, redirect
from supabase import create_client, Client

app = Flask(__name__)

# మీ Supabase వివరాలు ఇక్కడ ఇవ్వండి (Supabase Settings -> API నుండి తీసుకోవచ్చు)
SUPABASE_URL = "https://ipfwgpwfypatvkqmhgeu.supabase.co"
SUPABASE_KEY = "sb_publishable_vUghVlLa1vTw19MDI4tXFQ_tIO2OKZH"

# Supabase క్లయింట్‌ను ఇనిషియలైజ్ చేయడం
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/')
def home():
    # డేటాబేస్ నుండి మెంబర్స్ డేటాను తెచ్చుకోవడం
    response = supabase.table('community_members').select("*").execute()
    members_list = response.data if response.data else []
    
    return render_template('index.html', members=members_list)

@app.route('/submit', methods=['POST'])
def submit():
    # ఫారమ్ నుండి వచ్చిన డేటాను తీసుకోవడం
    name = request.form.get('name')
    message = request.form.get('message')
    
    # Supabase డేటాబేస్‌లోకి డేటాను ఇన్సర్ట్ (సేవ్) చేయడం
    supabase.table('community_members').insert({
        "name": name, 
        "message": message
    }).execute()
    
    # సక్సెస్ అయిన తర్వాత హోమ్ పేజీకి రీడైరెక్ట్ చేయడం
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
