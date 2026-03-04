import requests
from bs4 import BeautifulSoup
import json
import time
from urllib.parse import urljoin
from tqdm import tqdm
from pathlib import Path


def scrape_isw(start_date, end_date, save_result=False, file_name="isw_data.json", max_pages=3):
    base_url = "https://understandingwar.org"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    all_articles_links = []

    url = f"{base_url}/research/?_date_from={start_date}%2C{end_date}&_teams=russia-ukraine"

    for page in tqdm(range(1, max_pages + 1), desc="Scraping pages:"):
        if page != 1:
            url += f"&_paged={page}"

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        page_links = []
        for a in soup.select('h3.research-card-title a'):
            href = a.get('href')
            if href:
                full_url = urljoin(base_url, href)
                if full_url not in page_links:
                    page_links.append(full_url)

        if not page_links:
            print(f"no news in {page}")
            break

        all_articles_links.extend(page_links)

        time.sleep(1)


    if not all_articles_links:
        print("no news")
        return

    news_data = []

    for link in tqdm(all_articles_links, desc="Scraping links:"):
        try:
            page_resp = requests.get(link, headers=headers)
            page_soup = BeautifulSoup(page_resp.text, 'html.parser')

            title_tag = page_soup.select_one('h1.gb-headline, h1#page-title, h1')
            title = title_tag.text.strip() if title_tag else "no title"

            date = "no data"
            date_tag = page_soup.select_one('h6.gb-text')
            if date_tag and "202" in date_tag.text:
                date = date_tag.text.strip()
            else:
                meta_date = page_soup.find('meta', property='article:published_time')
                if meta_date:
                    date = meta_date.get('content', '').split('T')[0]

            takeaways = []

            kt_container = page_soup.find(attrs={"data-id": "key-takeaways"})
            if kt_container:
                list_elem = kt_container.find(['ul', 'ol'])
                if list_elem:
                    for li in list_elem.find_all('li'):
                        takeaways.append(li.text.strip())

            if not takeaways:
                headers_tags = page_soup.find_all(['h2', 'h3', 'strong'])
                for header in headers_tags:
                    if "Key Takeaways" in header.text or "Toplines" in header.text:
                        parent = header.parent if header.name == 'strong' else header
                        curr = parent.find_next_sibling()
                        while curr:
                            if curr.name in ['ul', 'ol']:
                                for li in curr.find_all('li'):
                                    takeaways.append(li.text.strip())
                                break

                            nested_list = curr.find(['ul', 'ol'])
                            if nested_list:
                                for li in nested_list.find_all('li'):
                                    takeaways.append(li.text.strip())
                                break

                            if curr.name in ['h2', 'h3']:
                                break
                            curr = curr.find_next_sibling()
                        if takeaways:
                            break

            if not takeaways:
                takeaways.append("no key takeways")

            news_data.append({
                "date": date,
                "title": title,
                "url": link,
                "key_takeaways": takeaways
            })

            time.sleep(0.5)

        except Exception as e:
            print(f"error {link}: {e}")

    if save_result:
        data_dir = Path("data/isw/")

        if not data_dir.exists():
            data_dir.mkdir(parents=True)

        file_path = data_dir / file_name

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(news_data, f, ensure_ascii=False, indent=4)

        
    return news_data


if __name__ == "__main__":
    data = scrape_isw(start_date="2022-02-24", end_date="2026-03-04", save_result=True, max_pages=100)
    print(data)