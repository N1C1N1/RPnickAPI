import requests
from bs4 import BeautifulSoup
import random

class NationType(): # Нации
    RUSSIAN = 'russian'
    JAPANESE = 'japanese'
    ITALIAN = 'italian'
    LATINOS = 'latinos'
    FRENCH = 'french'
    SWEDISH = 'swedish'
    GERMAN = 'german'
    DANISH = 'danish'
    ROMANIAN = 'romanian'
    AMERICAN = 'american'

    def random(): # Выбор рандомной нации
        return random.choice(['russian', 'japanese', 'italian', 'latinos', 'french', 'swedish', 'german', 'danish', 'romanian', 'american'])
class GenderType(): # Гендеры
    MALE = 'male'
    FEMALE = 'female'

    def random(): # Выбор рандомного гендера
        return random.choice(['male', 'famale'])
def GenerateNick(gender = '' or GenderType or str, nation = '' or NationType or str, name = '' or str, surname = '' or str, ExitOnError = True or bool):
    page = requests.get(f'http://rp-nicks.aa-roleplay.ru/index.php?gender={gender}&nation={nation}&name={name}&surname={surname}')
    if 'Для создания ника выберите пол, национальность и нажмите на кнопку.' in BeautifulSoup(page.text, 'lxml').find_all('p'):
        soup = BeautifulSoup(page.text, 'lxml')
        nick = soup.find('textarea')
        return nick.text
    else:
        print(f'Ошибочка: гендер или нация не правельны!\nГендер: {gender}, Нация: {nation}')
        if ExitOnError == True:
            exit()
