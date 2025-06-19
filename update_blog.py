import feedparser
import os
import html

USERNAME = "yumin991209"
RSS_URL = f"https://velog.io/rss/{USERNAME}"
OUTPUT_DIR = "posts"

def sanitize_filename(s):
    # 파일명에 사용할 수 없는 문자 제거 및 공백은 언더바로 변경
    return "".join(c if c.isalnum() or c in " _-" else "" for c in s).replace(" ", "_")

def main():
    feed = feedparser.parse(RSS_URL)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for entry in feed.entries:
        title = entry.title.strip()
        published = entry.published
        link = entry.link
        content = entry.content[0].value

        filename = sanitize_filename(title) + ".md"
        filepath = os.path.join(OUTPUT_DIR, filename)

        # 이미 파일이 있으면 스킵 (중복 방지)
        if os.path.exists(filepath):
            continue

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n")
            f.write(f"> 📅 {published}\n\n")
            f.write(f"🔗 [원문 링크]({link})\n\n")
            f.write("---\n\n")
            f.write(html.unescape(content))

if __name__ == "__main__":
    main()
