import feedparser
import pandas as pd
import time
from datetime import datetime

def scrape_anime_rss(max_posts=500):
    posts = []
    url = "https://old.reddit.com/r/anime/new/.rss"   # Change to /hot/.rss or /top/.rss if wanted
    
    print(f"Fetching via RSS → target up to {max_posts} posts")

    # Reddit RSS is paginated poorly, so we fetch multiple times with delay
    for attempt in range(10):  # Try up to 10 pages
        feed = feedparser.parse(url)
        
        if not feed.entries:
            print("No entries returned (possibly temporary block)")
            break

        new_on_page = 0
        for entry in feed.entries:
            title = entry.title
            content = entry.get('summary', '') or entry.get('description', '')
            
            # Clean HTML from summary if needed
            if '<' in content:
                import re
                content = re.sub('<.*?>', '', content)
            
            link = entry.link
            
            if title and title not in [p['title'] for p in posts]:
                posts.append({
                    'title': title,
                    'content': content,
                    'permalink': link
                })
                new_on_page += 1

            if len(posts) >= max_posts:
                break

        print(f"Attempt {attempt+1}: +{new_on_page} posts | Total: {len(posts)}")

        if len(posts) >= max_posts or not feed.entries:
            break

        time.sleep(2.5)

    df = pd.DataFrame(posts)
    filename = f"r_anime_title_content_{len(df)}_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
    df.to_csv(filename, index=False, encoding='utf-8')

    print(f"\n✅ Saved {len(df)} posts to {filename}")
    print("\nPreview:")
    print(df.head(10))
    return df


# ===================== RUN =====================
if __name__ == "__main__":
    scrape_anime_rss(max_posts=400)