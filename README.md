# fullstack_vue_js_and_python_hh_test


### Установка зависимостей
```
pip install -r requirements.txt
```

### Миграции
```python
python manage.py makemigrations
```
```python
python manage.py migrate
```
Дополнительно будет создана одна модель `Product` для наполнения данными с wb

### Запуск парсера
```python
manage.py run_parser [category_url]
```
`category_url` - Полный адрес категории на wb, напр. `https://www.wildberries.ru/catalog/muzhchinam/odezhda/kombinezony` Команда 

### Frontend
Vue и vuetify напрямую подключены в `templates/index.html` для экономии времени  