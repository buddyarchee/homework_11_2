from flask import Flask

import utils

app = Flask(__name__)

candidates = utils.load_candidates()

@app.route('/')
def page_index():
    str_candidates = '<pre>\n'
    for candidate in candidates.values():
        str_candidates += f"\n{candidate['name']} \n {candidate['position']} \n {candidate['skills']}\n"
    str_candidates += '</pre>\n'
    return str_candidates


@app.route('/candidate/<int:id>')
def page_profile(id):
    candidate = candidates[id]
    str_candidate = f"<pre>\n <img src={candidate['picture']}> \n{candidate['name']} \n {candidate['position']} \n {candidate['skills']}\n</pre>"
    return str_candidate

@app.route('/skills/<skill>')
def page_skills(skill):
    str_candidates_skill = '<pre>\n'
    for candidate in candidates.values():
        skill_list = candidate['skills'].split(", ")
        skill_list = [x.lower() for x in skill_list]
        if skill.lower() in skill_list:
            str_candidates_skill += f"\n{candidate['name']} \n {candidate['position']} \n {candidate['skills']}\n"
    str_candidates_skill += '</pre>\n'
    return str_candidates_skill


app.run()