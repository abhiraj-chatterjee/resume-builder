from flask import Flask, render_template, url_for, request, jsonify, redirect
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
import requests
import datetime

# Use a service account
cred = credentials.Certificate('resume-builder-9141e-firebase-adminsdk-ca5df-b75f5f90e0.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

app = Flask(__name__)

# ======== Backend ========

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    user = 'abhiraj-chatterjee'
    doc_ref = db.collection('resumes').document(user).get()
    # return doc_ref.to_dict()
    return render_template("dashboard.html",user=user,resCount=doc_ref.to_dict()['resume_count'])

@app.route('/dashboard/resumes/all')
def allResumes():
    user = 'abhiraj-chatterjee'
    doc_ref = db.collection('resumes').document(user).collections()
    resumes = []
    for collection in doc_ref:
        resumes.append(str(collection.id))
    doc_ref = db.collection('resumes').document(user).get()
    return render_template('all_resumes.html',user=user,resumes=resumes,resCount=doc_ref.to_dict()['resume_count'])

@app.route('/dashboard/resumes/<template>')
def resumes(template):
    user = 'abhiraj-chatterjee'
    doc_ref = db.collection('resumes').document(user).collections()
    resume_hash = {}
    for collection in doc_ref:
        for each in collection.stream():
            resume_hash[each.id] = each.to_dict()
    doc_ref = db.collection('resumes').document(user).get()
    return render_template('resume.html',user=user,resume_hash=resume_hash,resCount=doc_ref.to_dict()['resume_count'])

@app.route('/new/resume')
def newResume():
    user = 'abhiraj-chatterjee'
    return render_template("new_resume.html",user=user)

@app.route('/new/resume/<template>',methods=['POST','GET'])
def newTemplate(template):
    user = 'abhiraj-chatterjee'
    if request.method == 'POST':
        
        doc_ref = db.collection('resumes').document(user).collection(template)
        time = str(datetime.datetime.now())

        db.collection('resumes').document(user).update({'resume_count': firestore.Increment(1)})

        # Metadata
        doc_ref.document('meta').set({
            'template': template
        })

        # Basic Information
        doc_ref.document('basic').set({
            'name': [
                { time: request.form['name'] }
            ],
            'email': [
                { time: request.form['email'] }
            ],
            'phone': [
                { time: request.form['phone'] }
            ],
            'address': [
                { time: request.form['address'] }
            ]
        })

        # Programming Languages
        arr = request.form.getlist('lang')
        langs = {}
        for each in arr:
            langs[each] = time
        doc_ref.document('lang').set(langs)

        # Open Source Work
        doc_ref.document('open').set({
            'account': [
                { time : request.form['gitAccount'] }
            ],
            'repos': [
                { time : request.form['gitRepos'] }
            ],
            'gists': [
                { time : request.form['gitGists'] }
            ],
            'followers': [
                { time : request.form['gitFollowers'] }
            ]
        })

        # Education
        doc_ref.document('edu').set({
            'college': [
                { time : request.form['college'] }
            ],
            'gradDate': [
                { time : request.form['grad'] }
            ],
            'majors': [
                { time : request.form['major'] }
            ],
            'minors': [
                { time : request.form['minor'] }
            ]
        })

        # Experience
        doc_ref.document('exp').set({
            'employer': [
                { time : request.form['employer'] }
            ],
            'position': [
                { time : request.form['position'] }
            ],
            'startDate': [
                { time : request.form['start'] }
            ],
            'endDate': [
                { time : request.form['end'] }
            ],
            'description': [
                { time : request.form['descrip'] }
            ]
        })

        return redirect(url_for('dashboard'))
    else:
        # List of all programming languages
        with open("data_file.json", "r") as read_file:
            data = json.load(read_file)
        lang = data["languages"]
        lang.sort()
        # List of universities
        unis = data["universities"]
        # GitHub Profile
        data = requests.get('https://api.github.com/users/'+user)
        # return jsonify(unis)
        return render_template(template+"_template.html",user=user,lang=lang,github=data.json(),unis=unis)

# ======== API ========

@app.route('/api/<template>/update/<doc>/<field>',methods=['POST','GET'])
def updateField(doc,field,template):
    user = 'abhiraj-chatterjee'
    time = str(datetime.datetime.now())
    if doc == 'lang':
        db.collection('resumes').document(user).collection(template).document(doc).update({
            request.form['lang'] : time
        })
    else:
        db.collection('resumes').document(user).collection(template).document(doc).update({
            field: firestore.ArrayUnion([{ time : request.form[field] }])
        })
    return redirect(url_for('resumes', template='technical'))

# ======== Config ========

# @app.route('/test')
# def test():
#     doc_ref = db.collection(u'users').document(u'alovelace')
#     doc_ref.set({
#         u'first': u'Ada',
#         u'last': u'Lovelace',
#         u'born': 1815
#     })
#     return 'Success!'

# Fix css sync errors
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

if __name__ == "__main__":
    app.run(debug=True)
