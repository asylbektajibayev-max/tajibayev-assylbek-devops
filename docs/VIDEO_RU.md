# Сценарий непрерывной видеодемонстрации

Запишите экран и собственный голос одним дублем, примерно 15–18 минут.
Перед записью откройте приложение, GitHub и Jenkins. Не показывайте infra/.env,
пароли, токены, окна менеджера паролей. Говорите своими словами и объясняйте команды.

## Минуты 0–1 Представление

«Меня зовут Assylbek Tajibayev, группа IT2-2310, Student ID 38288.
Я показываю свой проект DevOps: Linux, Git, GitHub, Docker и Jenkins».
Откройте информационный файл и структуру проекта.

## Минуты 1–5 Linux

Откройте Linux-терминал лабораторного контейнера, перейдите в
`/root/devops/tajibayev_assylbek`. Выполните `pwd`, `ls -la` и
`bash scripts/linux_demo.sh`. Объясните mkdir, touch, cp, mv, rm,
cat, head и tail по реальному выводу. Покажите find, grep ERROR,
grep WARNING и grep -c: в журнале 10 строк, ERROR=2, WARNING=2.
Покажите права 600 и 644, объясните owner/group/others и r/w/x.
Запустите системный скрипт, покажите проверку наличия файла.
Покажите ps aux и top: назовите конкретный PID, владельца, CPU и MEM.

## Минуты 5–8 Git и GitHub

Покажите `git status`, локальную identity, `git log --oneline --graph --all`,
ветки main/development и merge commit. Откройте .gitignore и выполните
`git check-ignore -v logs/application.log backup/example.txt .env`.
`git ls-files '*.log' backup .env` возвращает пустой результат.
Покажите `git remote -v` и настоящий репозиторий в браузере: файлы и коммиты.
Объясните branch, commit, push, pull; покажите, что секреты не опубликованы.

## Минуты 8–12 Docker

Откройте Dockerfile, объясните FROM, WORKDIR, COPY, RUN, EXPOSE, CMD и USER.
Покажите docker images, docker ps, docker ps -a и приложение localhost:8086.
Покажите Docker logs и exec; выполните stop/start.
Для удаления используйте отдельный manual контейнер из README.
Измените STUDENT_GROUP в отдельном запуске и покажите изменение JSON.
Верните IT2-2310. Покажите docker compose down, затем up -d --wait и compose ps.

## Минуты 12–16 Jenkins

Откройте localhost:8096 и Job Tajibayev_Assylbek_DevOps.
Покажите SCM GitHub URL и Jenkinsfile, затем Build Now.
Дождитесь завершения: покажите пять стадий, данные студента, Git SHA,
тесты, Docker build/run и последнюю строку Finished: SUCCESS в Console Output.
Откройте localhost:8087, покажите запущенный Pipeline контейнер в docker ps.

## Минуты 16–18 Объяснение цепочки

Расскажите, как Linux даёт среду, Git хранит версии, GitHub публикует код,
Jenkins получает определённый коммит, выполняет сборку и тесты, создаёт образ,
запускает и проверяет контейнер. Объясните остановку Pipeline при ошибке.
Покажите PDF-отчёт и три элемента сдачи: URL, PDF, собственное видео.
