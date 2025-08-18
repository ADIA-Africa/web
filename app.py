from flask import Flask, render_template, url_for
import os
import json

app = Flask(__name__)

def load_json(filename):
    with open(os.path.join('data', filename), 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/team')
def team():
    team_members = load_json('team.json')
    return render_template('team.html', team=team_members)

@app.route('/organs')
def organs():
    organs_list = load_json('organs.json')
    return render_template('organs.html', organs=organs_list)


@app.route('/chamber/skill-development')
def skill_development():
    return render_template('chamber_skill_development.html')

@app.route('/technical-management')
def technical_management():
    return render_template('technical_management.html')

@app.route('/device-access-and-development')
def device_access_and_development():
    return render_template('device_access.html')

@app.route('/chamber-marginalized-groups')
def chamber_marginalized_groups():
    return render_template('chamber_marginalized_groups.html')

@app.route('/policy-studies')
def policy_studies():
    return render_template('policy_studies.html')

@app.route('/digital-impact')
def digital_impact():
    return render_template('digital_impact.html')

@app.route('/industry-development')
def industry_development():
    return render_template('industry_development.html')

# organs routes

@app.route('/organs/general-assembly')
def general_assembly():
    return render_template('organs/general_assembly.html')


@app.route('/organs/diaspora-network')
def diaspora_network():
    return render_template('organs/diaspora_network.html')


@app.route('/organs/operational')
def operational():
    return render_template('organs/operational.html')

@app.route('/organs/digital_councils')
def digital_councils():
    return render_template('organs/digital_councils.html')

@app.route('/organs/inclusion_councils')
def inclusion_councils():
    return render_template('organs/inclusion_councils.html')

@app.route('/organs/operational_council')
def operational_council():
    return render_template('organs/operational_council.html')

@app.route('/organs/center_excellence')
def center_excellence():
    return render_template('organs/center-excellence.html')


@app.route('/events')
def events():
    events_list = load_json('events.json')
    return render_template('events.html', events=events_list)

if __name__ == '__main__':
    app.run(debug=True)