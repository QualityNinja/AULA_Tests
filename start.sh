#!/bin/bash
# Получение параметров с файла .env
export $(cat ./.env | grep -v ^# | xargs) >/dev/null
# сборка докера aula-test
docker build -t aula-test .
# запуск контейнера с параметрами
docker run -e LOGIN="${login}" -e PASSWORD="${password}" --rm --volume $PWD:/usr/workspace --workdir /usr/workspace aula-test