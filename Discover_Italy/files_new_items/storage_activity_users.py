import os, json

# файлы с информацией
base_dir = os.path.dirname(file)
user_file = os.path.join(base_dir, 'users.json')

def load_users():
    if not os.path.exists(user_file):
        return []
    with open(user_file, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except:
            return []


def save_users(users):
    with open(user_file, 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False, indent=4)
