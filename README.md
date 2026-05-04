# sverk.tech_autotests
## Автотесты для sverk.tech

Проект написан на Python + Selenium + pytest и отображает базовую автоматизацию 

### Запуск тестов
git clone https://github.com/unreso1veed/sverk.tech_autotests

cd sverk.tech_autotests

python3 -m venv .venv

source .venv/bin/acivate #MAC or

.venv\Scripts\activate #Windows

pip3 install -r requirements.txt

pytests tests

-------------
Запуск с отчетом:

pytest tests/ --html=report.html --self-contained-html

-------------
Есть наработки под автоматизацию для мобилок с помощью эмуляции через Selenium. В device_driver.py можно изменить тип устройства. 

