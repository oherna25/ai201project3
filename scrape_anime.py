import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

def scrape_anime_posts(max_posts=100):
    print("start")
    posts = []
    url = "https://old.reddit.com/r/anime/new/"   # Change to /hot/, /top/, /rising/ etc.
    fetched = 0

    print(f"Starting scrape → target: {max_posts} posts from r/anime")

    while fetched < max_posts:
        try:
            resp = requests.get(url, headers=headers, timeout=15)
            if resp.status_code != 200:
                print(f"Status code: {resp.status_code} - Reddit may be blocking")
                break

            soup = BeautifulSoup(resp.text, 'html.parser')

            for post in soup.find_all('div', class_='thing'):
                # Title
                title_tag = post.find('a', class_='title')
                title = title_tag.get_text(strip=True) if title_tag else ""

                # Flair
                flair = ""
                flair_tag = post.find('span', class_='linkflairlabel')
                if flair_tag:
                    flair = flair_tag.get_text(strip=True)
                else:
                    # Alternative locations
                    flair_tag = post.find('div', class_=lambda x: x and 'flair' in x.lower())
                    if flair_tag:
                        flair = flair_tag.get_text(strip=True)

                # Content (selftext)
                content = ""
                selftext_div = post.find('div', class_='usertext-body')
                if selftext_div:
                    content = selftext_div.get_text(strip=True)

                permalink = "https://old.reddit.com" + post.get('data-permalink', '')

                posts.append({
                    'title': title,
                    'flair': flair,
                    'content': content,
                    'permalink': permalink
                })

                fetched += 1
                if fetched % 50 == 0:
                    print(f"Fetched {fetched}/{max_posts} posts...")

                if fetched >= max_posts:
                    break

            # Next page
            next_button = soup.find('a', class_='next-button')
            if not next_button or not next_button.get('href'):
                print("No more pages available.")
                break

            url = next_button['href']
            time.sleep(1.5)  # Respectful delay

        except Exception as e:
            print(f"Error: {e}")
            break

    # Save to CSV
    df = pd.DataFrame(posts)
    filename = f"r_anime_title_flair_content_{len(df)}_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
    df.to_csv(filename, index=False, encoding='utf-8')
    print("end")
    print(f"\n✅ Finished! Saved {len(df)} posts to {filename}")
    