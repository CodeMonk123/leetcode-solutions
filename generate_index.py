import subprocess
import os
import json


def get_questions():
    url = "https://leetcode.com/api/problems/all/"

    raw = subprocess.check_output(['curl', url])

    question_list = json.loads(raw)["stat_status_pairs"]

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

contents = '# LeetCode\n'
for d in dirs:
    contents += '## {}\n'.format(d)
    subdirs = sorted(os.listdir(os.path.join('.', d)))
    for sd in subdirs:
        contents += '### {}\n'.format(sd.replace('_', ' ').capitalize())
        contents += '| Questoin ID | LeetCode Address | Solution |\n'
        contents += '| ---- | ---- | ---- |\n'
        files = os.listdir(os.path.join(d, sd))
        for f in files:
            if f.endswith('.py'):
                solution_id = f.split('.')[0]
                important = False
                if solution_id.endswith('*'):
                    important = True
                    solution_id = solution_id[:-1]
                solution_id = int(solution_id)

                for (question_id, question_slug, question_title) in questions:
                    if question_id == solution_id:
                        if not important:
                            contents += '| Question {} |  [{}]({}) | [{}]({}) \n'.format(
                                question_id, question_title,
                                'https://leetcode-cn.com/problems/{}'.format(
                                    question_slug), os.path.join(d, sd, f),
                                os.path.join(d, sd, f))
                        else:
                            contents += '| **Question {}** |  [{}]({}) | [{}]({}) \n'.format(
                                question_id, question_title,
                                'https://leetcode-cn.com/problems/{}'.format(
                                    question_slug), os.path.join(d, sd, f),
                                os.path.join(d, sd, f))

with open('README.md', mode='w') as f:
    f.write(contents)
