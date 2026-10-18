# DevOps laboratory by Assylbek Tajibayev

Name: Assylbek · Surname: Tajibayev · Group: IT2-2310 · Student ID: 38288

Персональное приложение и полный путь Linux → Git → GitHub → Jenkins → Docker.
Приложение использует стандартную библиотеку Python, не требует pip-пакетов и показывает
данные студента через HTML и JSON. Настройки можно переопределить переменными окружения.

## Запуск

```bash
git clone https://github.com/asylbektajibayev-max/tajibayev-assylbek-devops.git
cd tajibayev-assylbek-devops
docker compose up -d --build --wait
curl http://localhost:8086/api/student
docker compose ps
docker compose down
```

Адрес приложения: http://localhost:8086. Jenkins использует отдельный порт 8096,
а контейнер, запущенный Pipeline, — порт 8087. Порты привязаны к localhost.

## Структура

```text
app/main.py                    HTTP приложение
tests/test_app.py              5 поведенческих тестов
scripts/                       Linux демонстрация и системный отчёт
config/app.conf                учебная конфигурация проекта
logs/                          генерируемый журнал, исключён из Git
backup/                        временные копии, исключены из Git
Tajibayev_Assylbek_info.txt     данные студента
Dockerfile                     образ приложения
docker-compose.yml             запуск приложения
Jenkinsfile                    CI/CD Pipeline
infra/                         локальное окружение Jenkins
docs/                          объяснения и сценарий видео
```

Пустые каталоги Git не хранит. `scripts/linux_demo.sh` создаёт logs и backup.
`config/app.conf` служит примером файла конфигурации в Linux; приложение читает
переменные окружения непосредственно, этот файл не является их загрузчиком.

## Linux

Для буквального соответствия пути из задания на Linux:

```bash
mkdir -p ~/devops
git clone https://github.com/asylbektajibayev-max/tajibayev-assylbek-devops.git ~/devops/tajibayev_assylbek
cd ~/devops/tajibayev_assylbek
bash scripts/linux_demo.sh
./scripts/Tajibayev_Assylbek_system.sh
```

На Windows лабораторные Linux-команды выполняются в отдельном Linux-контейнере.
Команды `uname`, `free`, `ps` в нём описывают контейнер и ядро Docker Desktop,
а не нативную Windows. Не следует называть этот контейнер Ubuntu или полноценной VM.

## Проверки

```bash
python3 -m compileall -q app tests
python3 -m unittest discover -s tests -v
git status
git log --oneline --graph --all
git check-ignore -v logs/application.log backup/example.txt .env
git ls-files '*.log' backup .env
```

Последняя команда должна вернуть пустой вывод. `.gitignore` не снимает с учёта
файлы, которые были добавлены раньше; для них требуется `git rm --cached`.

## Docker вручную

```bash
docker build -t tajibayev-assylbek-devops .
docker images tajibayev-assylbek-devops
docker run -d --name tajibayev-assylbek-manual -p 127.0.0.1:8088:8000 \
  -e STUDENT_NAME=Assylbek -e STUDENT_SURNAME=Tajibayev \
  -e STUDENT_GROUP=IT2-2310 -e STUDENT_ID=38288 tajibayev-assylbek-devops
docker ps
docker ps -a
docker logs tajibayev-assylbek-manual
docker exec tajibayev-assylbek-manual id
docker stop tajibayev-assylbek-manual
docker start tajibayev-assylbek-manual
docker stop tajibayev-assylbek-manual
docker rm tajibayev-assylbek-manual
```

`tajibayev-assylbek-container` — обязательное имя основного Compose контейнера.
Для ручной демонстрации выбран суффикс manual, чтобы не конфликтовать с ним.

## Jenkins

Job: `Tajibayev_Assylbek_DevOps`. Тип: Pipeline from SCM, SCM: Git,
URL: https://github.com/asylbektajibayev-max/tajibayev-assylbek-devops.git,
Branch: `*/main`, Script Path: `Jenkinsfile`.

Локальный стенд:

```bash
# Создайте infra/.env со строкой JENKINS_ADMIN_PASSWORD=<свой случайный пароль>
docker compose -f infra/compose.yml up -d --build
```

Откройте http://localhost:8096, пользователь `assylbek`, пароль из `infra/.env`.
Этот файл исключён из Git. Стенд автоматически создаёт Job с нужным GitHub URL.
Кнопка Build Now запускает Checkout → Build → Test → Docker Build → Docker Run.
Pipeline печатает студента и Git SHA, проверяет здоровье и все четыре поля JSON
у реально запущенного контейнера. Ошибка команды с ненулевым кодом завершает
стадию ошибкой; следующие обычные стадии пропускаются, выполняется блок post.

Учебный Jenkins получает Docker socket и работает от root, поэтому имеет контроль
над локальным Docker Engine. Используйте только доверенные Jenkinsfile; не открывайте
этот стенд в интернет. Приложение в своём образе работает от непривилегированного student.
В постоянном окружении нужны отдельные агенты и ограниченные полномочия.

Остановка стенда без удаления истории:

```bash
docker compose -f infra/compose.yml down
```

## Сдача

Нужны GitHub URL, PDF с реальными результатами и один непрерывный ролик 10–20 минут
с вашим экраном и собственным голосом. Сценарий: `docs/VIDEO_RU.md`.
Теория и вопросы защиты: `docs/DEFENSE_RU.md`.

## Официальные источники

- https://docs.docker.com/reference/dockerfile/
- https://docs.docker.com/compose/how-tos/environment-variables/set-environment-variables/
- https://www.jenkins.io/doc/book/pipeline/
- https://www.jenkins.io/doc/book/installing/docker/
- https://git-scm.com/docs
