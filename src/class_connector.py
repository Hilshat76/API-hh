from abc import ABC, abstractmethod
import json
from typing import Any, Dict, List  # Any указывает на любой возможный тип данных.
from src.class_vacancies_hh import VacanciesHH


class WorkingWithAFile(ABC):

    @abstractmethod
    def add_vacancy(self, vacancy_data: Dict[str, Any]) -> None:
        pass

    @abstractmethod
    def get_vacancies(self) -> List[str]:
        pass

    @abstractmethod
    def del_vacancies(self) -> None:
        pass


class SaveJson(WorkingWithAFile):
    """
    Класс для сохранения и получения вакансий в JSON-файл
    """

    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def add_vacancy(self, vacancy_data: Dict[str, Any]) -> None:
        with open(self.file_name, 'a') as file:
            json.dump(vacancy_data, file, default=VacanciesHH.convert_to_dict)
            file.write('\n')

    def get_vacancies(self) -> List[str]:
        with open(self.file_name, 'r') as file:
            vacancies = json.load(file)
            return vacancies

    def del_vacancies(self) -> None:
        pass


class SaveTxt(WorkingWithAFile):
    """
    Класс для сохранения, получения и удаления вакансий из .txt-файла
    """

    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def add_vacancy(self, vacancy_data: Dict[str, Any]) -> None:
        with open(self.file_name, 'a') as file:
            file.write(str(vacancy_data) + '\n')

    def get_vacancies(self) -> List[str]:
        with open(self.file_name, 'r') as file:
            return file.readlines()

    def del_vacancies(self) -> None:
        pass
