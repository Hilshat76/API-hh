from src.class_api import HeadHunterRuAPI
from src.class_connector import SaveJson
from src.class_vacancies_hh import VacanciesHH


def user_intetraction():
    """
    Функция для работы с запросами пользователя
    """
    print('Привет! С помощью этого приложения поиск вакансий на Hh.ru станет намного проще.')
    name_vacancy = input('Введите название вакансии: ')
    salary_vacancy = input('Введите количество вакансий для отображения по убыванию зарплаты: ')
    # keyword_vacancy = input('Введите ключевые слова для фильтрации вакансий: ')

    vacancy_hh = HeadHunterRuAPI()

    all_vacancy = vacancy_hh.getting_vacancies(name_vacancy)
    good_vacancy = []
    for vacancy in all_vacancy['items']:
        print(vacancy)
        good_vacancy.append(
            VacanciesHH(vacancy['name'], vacancy['area']['name'], vacancy['salary']['from'], vacancy['salary']['to'],
                        vacancy['salary']['currency'], vacancy['snippet']['requirement'], vacancy['alternate_url']))
    print(good_vacancy)


if __name__ == "__main__":
    user_intetraction()
