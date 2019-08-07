import json
from django.utils.text import slugify

def concat_name(prefix, last, first, middle, suffix):

    id_name = last
    if prefix:
        id_name = prefix + " " + id_name
    id_name = id_name + ", " + first
    if middle:
        id_name = id_name + " " + middle
    if suffix:
        id_name = id_name + " " + suffix

    return id_name

def check_people(people, contributors):
    person_count = 0
    person_found_count = 0

    for person in people:
        person_count = person_count + 1
        person_exists = False
        person_id = person['pk']
        for contributor in contributors:
            contributor_id = contributor['pk']
            if person_id == contributor_id:
                person_found_count = person_found_count + 1
                person_exists = True
        if not person_exists:
            name_prefix = person['fields']['name_prefix']
            name_first = person['fields']['name_first']
            name_middle = person['fields']['name_middle']
            name_last = person['fields']['name_last']
            name_suffix = person['fields']['name_suffix']
            name = concat_name(name_prefix, name_last, name_first, name_middle, name_suffix)
            name_id = slugify(name)
            contributor_json = ',{"model": "api.contributor","pk": "'+person_id+'","fields": {"id": "'+name_id+'","name": "'+name+'","created": "2019-08-01T19:50:34.995Z","modified": "2019-08-01T19:50:34.995Z","description": ""}}'
            print('\t'+str(contributor_json))

    print()
    print('Total People: ' + str(person_count))
    print('People Found: ' + str(person_found_count))
    print()

def check_orgs(orgs, contributors):
    org_count = 0
    org_found_count = 0

    for org in orgs:
        org_count = org_count + 1
        org_exists = False
        org_id = org['pk']
        for contributor in contributors:
            contributor_id = contributor['pk']
            if org_id == contributor_id:
                org_found_count = org_found_count + 1
                org_exists = True
        if not org_exists:
            contributor_json = ',{"model": "api.contributor","pk": "'+org_id+'","fields": {"id": "org_'+str(org_count)+'","name": "Org '+str(org_count)+'","created": "2019-08-01T19:50:34.995Z","modified": "2019-08-01T19:50:34.995Z","description": ""}}'
            print('\t'+str(contributor_json))

    print()
    print('Total Orgs: ' + str(org_count))
    print('Orgs Found: ' + str(org_found_count))


with open('./fixtures/person.json') as json_data:
   people = json.load(json_data)

with open('./fixtures/organization.json') as json_data:
   orgs = json.load(json_data)

with open('./fixtures/contributor.json') as json_data:
   contributors = json.load(json_data)

with open('./fixtures/book.json') as json_data:
    books = json.load(json_data)

for org in orgs:
    org_id = org['pk']

    for book in books:
        testers = book['fields']['play_tester']
        if len(testers) > 0:
            for tester in testers:
                print(tester)




