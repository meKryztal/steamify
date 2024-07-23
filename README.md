# Автофарм Steamify
![photo_2024-07-23_22-02-01](https://github.com/user-attachments/assets/b854b0bf-2d7d-4c0a-ad9a-35d0a3da349d)



-  Клеймит каждые 6 часов поинты
-  Забирает дейли ревард
-  Можно загрузить сотни акков
-  Работа по ключу, без авторизации
-  Забирает бусты
-  Выполняет задания 
-  Забирает награду с рефки


# Установка:
1. Установить python (Протестировано на 3.11)

2. Зайти в cmd(терминал) и вписывать
   ```
   git clone https://github.com/meKryztal/steamify.git
   ```
   
   ```
   cd steamify
   ```
3. Установить модули
   
   ```
   pip install -r requirements.txt
   ```
 
   или
   
   ```
   pip3 install -r requirements.txt
   ```



4. Запуск
   ```
   python tabi.py
   ```

   или

   ```
   python3 tabi.py
   ```
   
# Или через Pycharm ГАЙД на любых системах и решения ошибок внизу гайда
https://telegra.ph/Avtoklikker-dlya-BLUM-GAJD-05-29
   



## Вставить в файл init_data ключи такого вида, каждый новый ключ с новой строки:
   ```
   query_id=xxxxxxxxxx&user=xxxxxxfirst_namexxxxxlast_namexxxxxxxusernamexxxxxxxlanguage_codexxxxxxxallows_write_to_pmxxxxxxx&auth_date=xxxxxx&hash=xxxxxxx
   query_id=xxxxxxxxxx&user=xxxxxxfirst_namexxxxxlast_namexxxxxxxusernamexxxxxxxlanguage_codexxxxxxxallows_write_to_pmxxxxxxx&auth_date=xxxxxx&hash=xxxxxxx
   query_id=xxxxxxxxxx&user=xxxxxxfirst_namexxxxxlast_namexxxxxxxusernamexxxxxxxlanguage_codexxxxxxxallows_write_to_pmxxxxxxx&auth_date=xxxxxx&hash=xxxxxxx
   query_id=xxxxxxxxxx&user=xxxxxxfirst_namexxxxxlast_namexxxxxxxusernamexxxxxxxlanguage_codexxxxxxxallows_write_to_pmxxxxxxx&auth_date=xxxxxx&hash=xxxxxxx
   ```
Вместо query_id= может быть user=, разницы нету
# Как получить query_id:
Заходите в telegram web, открываете бота, жмете F12 или в десктопной версии открывайте окно, правой кнопкой жмете и выбираете самое нижнее "проверить" и переходите в Network, жмете старт в веб версии или перезагружаете страницу в десктопной, ищете запрос с именем info, в правой колонке находите Rawdata: query_id=бла бла бла или user=

![photo_2024-07-24_01-33-06](https://github.com/user-attachments/assets/0fd130cd-e8e9-4e71-bf57-9f7a9b4e9d56)

