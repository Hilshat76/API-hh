from typing import List
import requests
from abc import ABC, abstractmethod


class APIVacanciesHH(ABC):
    """
    Абстрактный класс для работы с API сервиса вакансий.
    """

    @abstractmethod
    def getting_vacancies(self, keyword: str) -> List[dict]:
        pass


class HeadHunterRuAPI(APIVacanciesHH):
    """
    Подключается к API и получает вакансии по ключевому слову
    """

    def __init__(self, per_page: int = 20):
        self._url = 'https://api.hh.ru/vacancies'
        self._per_page = per_page

    def getting_vacancies(self, keyword: str) -> List[dict]:
        """
        Получает вакансии по ключевому слову из API сервиса поиска вакансий
        :param keyword: Ключевое слово для поиска вакансий
        :return: JSON-данные с информацией о вакансиях
        """
        params = {'text': keyword, 'per_page': self._per_page}
        response = requests.get(self._url, params=params)
        data = response.json()
        return data
