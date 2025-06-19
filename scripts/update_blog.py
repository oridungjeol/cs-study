import feedparser
import os
import re

rss_url = 'https://api.velog.io/rss/@yumin991209'
repo_path = '.'
posts_dir = os.path.join(repo_path, 'velog-posts')

if not os.path.exists(posts_dir):
    os.makedirs(posts_dir)

feed = feedparser.parse(rss_url)

def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', '-', name)

for entry in feed.entries:
    file_name = sanitize_filename(entry.title) + '.md'
    file_path = os.path.join(posts_dir, file_name)

    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(entry.description)
