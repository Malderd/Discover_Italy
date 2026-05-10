import json
import os

# файлы с информацией
BASE_DIR = os.path.dirname(__file__)
ARTICLES_FILE = os.path.join(BASE_DIR, 'articles.json')
ARTICLES_FILE = os.path.join(BASE_DIR, 'files_articles/articles.json')

# загрузка статей
def load_articles():
    if not os.path.exists(ARTICLES_FILE):
        return []
    with open(ARTICLES_FILE, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except:
            return []
        

# сохранение статей
def save_articles(articles):
    with open(ARTICLES_FILE, 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=4)
