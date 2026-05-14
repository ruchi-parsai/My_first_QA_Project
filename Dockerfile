FROM mcr.microsoft.com/playwright/python:v1.59.0-jammy

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN pip install pytest-playwright allure-pytest Faker

CMD ["pytest", "tests/", "--alluredir=allure-results"]