FROM python:3.12.0a4-alpine3.17

# установка зависимостей
RUN echo "https://dl-4.alpinelinux.org/alpine/v3.10/main" >> /etc/apk/repositories && \
    echo "https://dl-4.alpinelinux.org/alpine/v3.10/community" >> /etc/apk/repositories && \
    apk update && \
    apk add --no-cache chromium chromium-chromedriver tzdata && \
    wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-2.30-r0.apk && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-bin-2.30-r0.apk && \
    apk update && \
    apk add --no-cache openjdk11-jre curl tar && \
    curl -o allure-2.13.8.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.tgz && \
    tar -zxvf allure-2.13.8.tgz -C /opt/ && \
    ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure && \
    rm allure-2.13.8.tgz && \ 
    rm /var/cache/apk/*

# установка рабочей директорий
WORKDIR /usr/workspace

# копирование зависимостей в рабочую директорию
COPY ./requirements.txt /usr/workspace

# установка зависимостей питона
RUN pip3 install -r requirements.txt

# запуск тестов
CMD ["pytest","-sv","--alluredir=allure-results"]