import json

with open('source_file_2.json', 'r') as source_file:
    source_text = source_file.read()

source_data = json.loads(source_text)
ordered_priority_data = sorted(source_data, key=lambda k: k['priority'])
managers_projects = {}
watchers_projects = {}

for project in ordered_priority_data:
    for manager in project['managers']:
        if manager in managers_projects:
            managers_projects[manager].append(project['name'])
        else:
            managers_projects[manager] = [project['name']]

    for watcher in project['watchers']:
        if watcher in watchers_projects:
            watchers_projects[watcher].append(project['name'])
        else:
            watchers_projects[watcher] = [project['name']]

with open('watchers.json', 'w') as output_file_1:
    output_file_1.write(json.dumps(managers_projects, indent=4, sort_keys=True))

with open('managers.json', 'w') as output_file_2:
    output_file_2.write(json.dumps(watchers_projects, indent=4, sort_keys=True))

source_file.close()
output_file_1.close()
output_file_2.close()
