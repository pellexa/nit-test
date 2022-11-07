# How to

```bash
git clone https://github.com/pellexa/nit-test.git sp_testwork
cd sp_testwork
```

Open three terminal tabs.

(first tab) Only the database is running.

```bash
docker-compose up
```

(second tab) Start Django.

```bash
cd app/backend/
python3 -m venv sp_env
source sp_env/bin/activate
pip install -r requirements.txt
cp .env.example .env
python3 manage.py migrate
python3 manage.py runserver
```

http://127.0.0.1:8000 Must return "Page not found (404)"

(third tab) Start Vue.

```bash
cd app/frontend/app/
cp .env.example .env
npm install
npm run dev
```

http://localhost:5173/
