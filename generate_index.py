import requests, json

session = requests.Session()
user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'


def get_questions():
    url = "https://leetcode.com/api/problems/all/"

    headers = {'User-Agent': user_agent, 'Connection': 'keep-alive'}
    resp = session.get(url, headers=headers, timeout=10)

    question_list = json.loads(
        resp.content.decode('utf-8'))["stat_status_pairs"]

    def extract(question):
        return question['stat']['frontend_question_id'], question['stat'][
            'question__title_slug'], question['stat']['question__title']

    question_list = list(map(extract, question_list))
    return question_list


questions = get_questions()

import os
dirs = os.listdir('.')
dirs.remove('.vscode')
dirs.remove('.git')
dirs = list(filter(os.path.isdir, dirs))
dirs = sorted(dirs)
print(dirs)

contents = '# LeetCode\n'
for d in dirs:
    contents += '## {}\n'.format(d)
    subdirs = sorted(os.listdir(os.path.join('.', d)))
    for sd in subdirs:
        contents += '--- \n'
        contents += '### {}\n'.format(sd.replace('_', ' ').capitalize())
        contents += '| Questoin ID | LeetCode Address | Solution |\n'
        contents += '| ---- | ---- | ---- |\n'
        files = os.listdir(os.path.join(d, sd))
        for f in files:
            if f.endswith('.py'):
                solution_id = int(f.split('.')[0])
                for (question_id, question_slug, question_title) in questions:
                    if question_id == solution_id:
                        contents += '| Question {} |  [{}]({}) | [{}]({}) \n'.format(
                            question_id, question_title,
                            'https://leetcode-cn.com/problems/{}'.format(
                                question_slug), os.path.join(d, sd, f),
                            os.path.join(d, sd, f))

with open('README.md', mode='w') as f:
    f.write(contents)
