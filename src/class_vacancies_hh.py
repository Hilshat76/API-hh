from typing import Optional  # позволяет указать, что переменная может
# иметь указанный тип или быть None.


class VacanciesHH:
    """
    Класс для представления вакансий
    """

    def __init__(self, name: str, city: str, salary_from: Optional[int], salary_to: Optional[int], currency: str, requirements: str, link: str):
        self.name = name
        self.city = city
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.requirements = requirements
        self.link = link

        self.validate_data()

    def validate_data(self) -> None:
        """
        Валидация данный о вакансии
        """
        if not self.salary_from and not self.salary_to:
            self.salary_from = 0

    def __lt__(self, other: 'VacanciesHH') -> bool:
        """
        Метод для сравнения вакансий по ЗП
        """
        return self.salary_from < other.salary_from

    def __eq__(self, other: 'VacanciesHH') -> bool:
        """
        Проверка равенства вакансий
        """
        return (self.name == other.name and self.city == other.city and self.salary_from == other.salary_from
                and self.salary_to == other.salary_to
                and self.requirements == other.requirements and self.link == other.link)

    def __repr__(self) -> str:
        """
        Строковое представление объекта класса VacanciesHH
        """
        return (f"""
                Название вакансии: {self.name}
                Город: {self.city}
                Заработная плата: {self.salary_from} - {self.salary_to} {self.currency}
                Требования: {self.requirements}
                Ссылка на вакансию: {self.link}
                """)

    @staticmethod
    def convert_to_dict(obj: 'VacanciesHH'):
        """
        Сериализирует объект класса VacanciesHH в формат JSON.
        """
        if isinstance(obj, VacanciesHH):
            return obj.__dict__
        return obj
