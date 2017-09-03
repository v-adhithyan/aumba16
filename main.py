from flask import Flask, render_template
import csv
import mba

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/profile/<string:rollno>/")
def profile(rollno):
    data = mba.profile(rollno)

    if data['no_error']:
        name = data['name']
        elective_1 = data['elective_1']
        elective_2 = data['elective_2']
        about_me = data['about_me']
        degree = data['degree']
        college = data['college']
        summer_int = data['summer_int']
        int_stream = data['int_stream']
        prev_org = data['prev_org']
        exp = data['exp']
        designation = data['designation']
        email = data['email']
        linkedin_profile = data['linkedin_profile']
        linkedin_image = data['linkedin_image']

        return render_template('profile.html', **locals())

    else:
        return "404: Not found: No such profile. Not in database."

app.run(host='0.0.0.0', port=80)
