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
