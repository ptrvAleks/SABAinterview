import os

# Базовый URL сайта
site_url = "https://ptrvaleks.github.io/SABAinterview/"

# Папка с исходными Markdown-файлами
docs_dir = "docs"

# Путь к итоговому sitemap.txt в папке site/
txt_sitemap_path = "site/sitemap.txt"

urls = []

# Проходим по всем папкам и файлам
for root, _, files in os.walk(docs_dir):
    for f in files:
        if f.endswith(".md"):
            # Получаем путь относительно docs/
            rel_path = os.path.relpath(os.path.join(root, f), docs_dir)
            # Убираем расширение, заменяем обратные слэши на прямые, делаем строчные буквы
            url_path = os.path.splitext(rel_path)[0].replace("\\", "/").lower()
            # Пропускаем index.md в корне, он уже соответствует /
            if url_path == "index":
                urls.append(site_url)
            else:
                urls.append(site_url + url_path + "/")

# Сортируем URL по алфавиту
urls = sorted(urls)

# Создаём sitemap.txt
os.makedirs(os.path.dirname(txt_sitemap_path), exist_ok=True)
with open(txt_sitemap_path, "w", encoding="utf-8") as f:
    for url in urls:
        f.write(url + "\n")

print(f"sitemap.txt создан в {txt_sitemap_path} с {len(urls)} URL")