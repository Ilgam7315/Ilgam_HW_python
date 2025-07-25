# Проект автоматизированного тестирования (Lesson 10)

## Содержание
1. [О проекте](#-о-проекте)
2. [Предварительные требования](#-предварительные-требования)
3. [Установка](#-установка)
4. [Запуск тестов](#-запуск-тестов)
5. [Просмотр отчетов](#-просмотр-отчетов)


## 🧩 О проекте

Проект содержит автоматизированные тесты с использованием:
- Selenium WebDriver
- Pytest
- Allure Framework

Тестируемые приложения:
1. [Медленный калькулятор](https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html)
2. [Интернет-магазин Saucedemo](https://www.saucedemo.com/)

## 📋 Предварительные требования

Перед началом работы убедитесь, что у вас установлено:
- Python 3.7 или новее
- Браузеры Chrome и Firefox
- Allure Commandline ([инструкция по установке](https://docs.qameta.io/allure/#_installing_a_commandline))

## ⚙️ Установка

1. Клонируйте репозиторий:
bash
git clone https://github.com/ваш-username/ваш-репозиторий.git
cd ваш-репозиторий

   
## Запуск тестов 
python -m pytest --alluredir allure-result  

## Просмотр отчетов
allure serve allure-result
