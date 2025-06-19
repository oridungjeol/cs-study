import feedparser
import git
import os
import re

rss_url = 'https://api.velog.io/rss/@yumin991209'
repo_path = '.'
posts_dir = os.path.join(repo_path, 'velog-posts')

if not os.path.exists(posts_dir):
    os.makedirs(posts_dir)

repo = git.Repo(repo_path)
feed = feedparser.parse(rss_url)

def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', '-', name)

for entry in feed.entries:
    file_name = sanitize_filename(entry.title) + '.md'
    file_path = os.path.join(posts_dir, file_name)

    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(entry.description)

        repo.git.add(file_path)
        commit_msg = f'Add post: {entry.title}'
        repo.git.commit('-m', commit_msg)

try:
    repo.git.push()
except Exception as e:
    print(f'Error pushing to remote: {e}')
