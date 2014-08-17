from flask import Flask, render_template, jsonify, request, json, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

from ideas import insert_idea, get_session, Idea

@app.route('/api/add_idea', methods=['GET', 'POST'])
def api_add_idea():
    if request.method == 'POST':
        name = insert_idea(request.form['description'], request.form['creator'])
        return jsonify({"name": name,
                        "description": request.form['description'],
                        "creator": request.form['creator']})
    else:
        return render_template("index.html")

@app.route('/api/ideas')
def api_ideas():
    session = get_session()
    ideas = []
    for idea in session.query(Idea).all():
        ideas.append({'name': idea.name,
                      'description': idea.description,
                      'creator': idea.creator})
    return jsonify({'ideas': ideas})
    
