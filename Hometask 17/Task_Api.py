import requests

# 2. Используя requests вывести информацию об каком-то одном instance.

respons = requests.get('https://v2.jokeapi.dev/joke/Any?safe-mode')

print(respons.json())

# 3. Получить данные из API, отсортировав их по какому-либо признаку.
# Например, если вы используете API для получения новостей
# покажите только новости определенной категории или из определенного источника.

respons = requests.get('https://v2.jokeapi.dev/joke/Dark')

print(respons.json())

# 4. Проанализируйте ваше API. Например:
# извлеките определенные данные из ответа
# (получите заголовки новостей из JSON-ответа и вывести их на экран).

respons = requests.get('https://v2.jokeapi.dev/joke/category')

print(respons.json())
