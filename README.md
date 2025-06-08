Как запустить проект...

```bash
python3 -m venv venv (если не хотите использовать глобальный интерпретатор)

pip3 install -r requirements.txt

python3 manage.py migrate --run-syncdb

python3 manage.py runserver
```
