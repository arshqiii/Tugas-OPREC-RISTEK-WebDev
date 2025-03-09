# Installation Guide ⚙️

### 1. Clone Repository
```shell
git clone https://github.com/arshqiii/Tugas-OPREC-RISTEK-WebDev.git
```
### 2. Create Virtual Environment
```shell
python -m venv env
source env/bin/activate  # MacOS/Linux
env\Scripts\activate     # Windows
```
### 3. Install Requirements
```shell
pip install -r requirements.txt
```
### 4. Migrate Database
```shell
python manage.py migrate
```
### 5. Runserver
```shell
python manage.py runserver
```
Access Website Locally at : http://127.0.0.1:8000