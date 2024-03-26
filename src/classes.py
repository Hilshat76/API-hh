import requests
import json
from abc import ABC, abstractmethod


class APIVacanciesHH(ABC):
    """
    Абстрактный класс для работы с API сервиса вакансий.
    """

    @abstractmethod
    def getting_vacancies(self, keyword):
        pass


class HeadHunterRuAPI(APIVacanciesHH):
    """
    Подключается к API и получает вакансии по ключевому слову
    """

    def getting_vacancies(self, keyword):
        """
        Получает вакансии по ключевому слову из API сервиса поиска вакансий
        :param keyword: Ключевое слово для поиска вакансий
        :return: JSON-данные с информацией о вакансиях
        """
        url = 'https://api.hh.ru/vacancies'
        params = {'text': keyword}
        response = requests.get(url, params=params)
        data = response.json()
        return data

    @staticmethod
    def saving_json(data, filename):
        """
           Сохраняет данные в формате JSON в файл.

           :param data: Данные в формате JSON, которые нужно сохранить.
           :param filename: Имя файла, в который нужно сохранить данные.
           """
        with open(filename, 'w') as file:
            json.dump(data, file)


class VacanciesHH:
    """
    Класс для представления вакансий
    """

    def __init__(self, name, city, salary_from, salary_to, currency, requirements, link):
        self.name = name
        self.city = city
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.requirements = requirements
        self.link = link

        self.validate_data()

    def validate_data(self):
        """
        Валидация данный о вакансии
        :return: Если зарплата не указана, устанавливает значение 0 для salary_from.
        """
        if not self.salary_from and not self.salary_to:
            self.salary_from = 0

    def __lt__(self, other):
        """
        Метод для сравнения вакансий по ЗП
        :param other:
        :return: True, если зарплата текущей вакансии (self) меньше зарплаты второй вакансии (other)
        """
        return self.salary_from < other.salary_from

    def __eq__(self, other):
        """
        Проверка равенства вакансий
        :param other:
        :return: True, если атрибуты двух вакансий (self и other) равны
        """
        return (self.name == other.name and self.city == other.city and self.salary_from == other.salary_from
                and self.salary_to == other.salary_to
                and self.requirements == other.requirements and self.link == other.link)

    def __repr__(self):
        """
        Строковое представление объекта класса VacanciesHH
        :return:
        """
        return (f"""
                Название вакансии: {self.name}
                Город: {self.city}
                Заработная плата: {self.salary_from} - {self.salary_to} {self.currency}
                Требования: {self.requirements}
                Ссылка на вакансию: {self.link}
                """)

