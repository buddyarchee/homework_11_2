import json
from pprint import pprint


def load_candidates():
    with open("candidates.json",  "r", encoding="utf-8") as file:
        data = json.load(file)
        candidates = {}
        for i in data:
            candidates[i['id']] = i
        return candidates

def get_candidate_by_id(id):
    candidate = load_candidates()[id]
    return candidate

def get_candidate_by_name(name):
    candidate = load_candidates()
    candidate_search = []
    for candidate in candidate.values():
        if name in candidate['name']:
            candidate_search.append(candidate)
    return candidate_search

def get_candidate_by_skill(skill):
    candidate = load_candidates()
    candidate_search = []
    for candidate in candidate.values():
        skill_list = candidate['skills'].split(", ")
        skill_list = [x.lower() for x in skill_list]
        if skill.lower() in skill_list:
            candidate_search.append(candidate)
    return candidate_search

load_candidates()

pprint(get_candidate_by_name("Adela Hendricks"))