from src.class_api import HeadHunterRuAPI
from src.class_connector import SaveJson
from src.class_vacancies_hh import VacanciesHH


def get_value(dictionary, *keys):
    """
    Возвращает значение из словаря по заданному пути ключей.
    :param dictionary: словарь, из которого мы получаем значение
    :param keys: переменное количество ключей в виде строки, определяющих путь к значению.
    :return: Значение из словаря, связанное с заданным путем ключей.
     Если хотя бы один ключ не существует или путь прерывается значениями None, будет возвращено None.
    """
    for key in keys:
        if dictionary is None:
            return None
        dictionary = dictionary.get(key)
    return dictionary


def user_interaction():
    """
    Функция для работы с запросами пользователя
    """
    print('Привет! С помощью этого приложения поиск вакансий на Hh.ru станет намного проще.')
    try:
        name_vacancy = input('Введите название вакансии: ')
        top_n = int(input('Введите количество вакансий для отображения по убыванию зарплаты: '))

        vacancy_hh = HeadHunterRuAPI()
        all_vacancy = vacancy_hh.getting_vacancies(name_vacancy)

        # Фильтрация вакансий по валюте RUR
        all_vacancy = [vacancy for vacancy in all_vacancy.get('items') if get_value(vacancy, 'salary', 'currency') == 'RUR']

        good_vacancy = []

        print(f"Всего количество вакансий по запросу '{name_vacancy}': {len(all_vacancy)}")
        print(f"Топ {min(top_n, len(all_vacancy))} вакансий по зарплате:")

        # использование {} для создания пустого словаря вместе с методом get() обеспечивает
        # безопасный доступ к значениям словаря и предотвращает возможные ошибки
        # при отсутствии ключей или пустых значений в словаре.
        for vacancy in all_vacancy:
            name = get_value(vacancy, 'name')
            area = get_value(vacancy, 'area', 'name')
            salary_from = get_value(vacancy, 'salary', 'from')
            salary_to = get_value(vacancy, 'salary', 'to')
            salary_currency = get_value(vacancy, 'salary', 'currency')
            requirement = get_value(vacancy, 'snippet', 'requirement')
            alternate_url = get_value(vacancy, 'alternate_url')

            good_vacancy.append(
                VacanciesHH(name, area, salary_from, salary_to, salary_currency, requirement, alternate_url))

        top_vacancy = sorted(good_vacancy, key=lambda x: x.salary_to if x.salary_to is not None else 0, reverse=True)

        for vacancy in top_vacancy[:min(top_n, len(top_vacancy))]:
            print(vacancy)

    except TypeError as e:
        print(f"{e}")


if __name__ == "__main__":
    user_interaction()
