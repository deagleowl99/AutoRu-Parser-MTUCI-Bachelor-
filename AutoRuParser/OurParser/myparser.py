# -*- coding: utf-8 -*-
import requests # библиотека для взаимодействия с протоколом HTTP
from bs4 import BeautifulSoup # библиотека для создания парсеров
import csv # библиотека для работы с csv файлами
import os # библиотека для работы с файлами

FILE = 'D:\\cars2.csv' # путь файла
HEADERS = {'user-agent': 'Google Chrome (Windows NT 10.0; Win64; x64'} # заголовки для формирования запроса

def get_html(url, params=None): # процедура получения кода ответа HTTP
    r = requests.get(url, headers=HEADERS, params=params)
    return r
	
def parse(html): # процедура для сбора данных
    soup = BeautifulSoup(html, 'html.parser') # экземпляр класса для парсера
    titles = soup.find_all('a', class_='Link ListingItemTitle-module__link') # поиск названий моделей
    data = soup.find_all('div', class_='ListingItemTechSummaryDesktop ListingItem-module__techSummary') # поиск параметров моделей
    prices = soup.find_all('div', class_='ListingItemPrice-module__content') # поиск значений стоимости
    years = soup.find_all('div', class_='ListingItem-module__year') # поиск значений года производства
    probegs = soup.find_all('div', class_='ListingItem-module__kmAge') # поиск значений пробега
    titles2 = []
    links2 = []
    
    for link in soup.findAll('a', {'class': 'Link ListingItemTitle-module__link'}):
        try:
            links2.append(link['href'])
        except KeyError:
            pass
    i = 0
    for tag in titles: # раскодировка из UTF-8
        tagtext = tag.text
        tagtext = tagtext.replace('Ð ÐµÑÑÐ°Ð¹Ð»Ð¸Ð½Ð³', 'Рестайлинг')
        tagtext = tagtext.replace('Ð£ÐÐ', 'УАЗ')
        tagtext = tagtext.replace('Ð', 'Б')
        tagtext = tagtext.replace('ÐÐ¿ÑÑÐ½ÑÐ¹ Ð¾Ð±ÑÐ°Ð·ÐµÑ', 'Опытный образец')
        tagtext = tagtext.replace('ÐÐ¾Ð½Ð¾ÑÐ½ÑÐ¹ Ð°Ð²ÑÐ¾Ð¼Ð¾Ð±Ð¸Ð»Ñ Ð¤Ð¾ÑÐ¼ÑÐ»Ð°', 'Гоночный автомобиль Формула')
        tagtext = tagtext.replace('ÐÐ¾ÑÐºÐ²Ð¸Ñ', 'Москвич')
        tagtext = tagtext.replace('Ð¡Ð²ÑÑÐ¾Ð³Ð¾Ñ', 'Святогор') 
        tagtext = tagtext.replace('Ð®ÑÐ¸Ð¹ ÐÐ¾Ð»Ð³Ð¾ÑÑÐºÐ¸Ð¹', 'Юрий Долгорукий')
        tagtext = tagtext.replace('ÐÐ½ÑÐ·Ñ ÐÐ»Ð°Ð´Ð¸Ð¼Ð¸Ñ', 'Князь Владимир')
        tagtext = tagtext.replace('ÐÐ­', 'ИЭ')
        tagtext = tagtext.replace('ÐÐÐ', 'ВАЗ')
        tagtext = tagtext.replace('ÐÐºÐ°', 'Ока')
        tagtext = tagtext.replace('Ð¡ÐµÐÐ', 'СеАЗ')
        tagtext = tagtext.replace('ÐÐ°Ð¼ÐÐ', 'КамАЗ')
        tagtext = tagtext.replace('БÐ¾Ð³Ð´Ð°Ð½', 'Богдан')
        tagtext = tagtext.replace('ÐÐ°Ð´ÐµÐ¶Ð´Ð°', 'Надежда')
        tagtext = tagtext.replace('Ð ÑÑÑ', 'Рысь')
        tagtext = tagtext.replace('ÐÐÐ', 'ГАЗ')
        link = soup.find('a', class_='Link ListingItemTitle-module__link').get('href')
        tagtext = tagtext + ' '
        titles2.append(tagtext)

    data2 = []
    for tag in data: # раскодировка из UTF-8
        tagtext = tag.text
        tagtext = tagtext.replace(u'\xa0', '')
        tagtext = tagtext.replace(u'\x80', '')
        tagtext = tagtext.replace(u'\x81', '')
        tagtext = tagtext.replace(u'\x82', '')
        tagtext = tagtext.replace(u'\x83', '')
        tagtext = tagtext.replace(u'\x84', '')
        tagtext = tagtext.replace(u'\x85', '')
        tagtext = tagtext.replace(u'\x87', '')
        tagtext = tagtext.replace(u'\x89', '')
        tagtext = tagtext.replace(u'\x91', '')
        tagtext = tagtext.replace(u'\x93', '')
        tagtext = tagtext.replace(u'\x94', '')
        tagtext = tagtext.replace(u'\â/â', '')
        tagtext = tagtext.replace(u'Ð»â', 'л')
        tagtext = tagtext.replace(u'/â', ' / ')
        tagtext = tagtext.replace(u'ÂÐ».Ñ.â', ' л.с.')
        tagtext = tagtext.replace('ÐÐµÐ½Ð·Ð¸Ð½', 'Бензин')
        tagtext = tagtext.replace('Ð¼Ð¸Ð½Ð¸Ð²Ñ\x8dÐ½', 'Минивэн')
        tagtext = tagtext.replace('Ð¿ÐµÑÐµÐ´Ð½Ð¸Ð¹', 'Передний')
        tagtext = tagtext.replace('ÐÐ¸Ð·ÐµÐ»Ñ\x8c', 'Дизель')
        tagtext = tagtext.replace('Ð°Ð²ÑÐ¾Ð¼Ð°Ñ', 'Автомат')
        tagtext = tagtext.replace('Ð²Ð½ÐµÐ´Ð¾ÑÐ¾Ð¶Ð½Ð¸Ðº 5 Ð´Ð².', 'Внедорожник 5 дв.')
        tagtext = tagtext.replace('Ð¿Ð¾Ð»Ð½Ñ\x8bÐ¹', 'Полный')
        tagtext = tagtext.replace('ÑÑ\x8dÑÑÐ±ÐµÐº 3 Ð´Ð².', 'Хэтчбек 3 дв.')
        tagtext = tagtext.replace('Ð¼ÐµÑÐ°Ð½Ð¸ÐºÐ°', 'Механика')
        tagtext = tagtext.replace('ÑÐ¾Ð±Ð¾Ñ', 'Робот')
        tagtext = tagtext.replace('ÑÐµÐ´Ð°Ð½', 'Седан')
        tagtext = tagtext.replace('ÑÑ\x8dÑÑÐ±ÐµÐº 5 Ð´Ð².', 'Хэтчбек 5 дв.')
        tagtext = tagtext.replace('ÑÐ½Ð¸Ð²ÐµÑÑÐ°Ð» 5 Ð´Ð².', 'Универсал 5 дв.')
        tagtext = tagtext.replace('ÐºÐ¾Ð¼Ð¿Ð°ÐºÑÐ²Ñ\x8dÐ½', 'Компактвэн')
        tagtext = tagtext.replace('Ð»Ð¸ÑÑÐ±ÐµÐº', 'Лифтбек')
        tagtext = tagtext.replace('ÑÐµÑÑ\x8bÐ¹', 'Белый')
        tagtext = tagtext.replace('Ð±ÐµÐ¶ÐµÐ²Ñ\x8bÐ¹', 'Бежевый')
        tagtext = tagtext.replace('ÑÐ¸Ð½Ð¸Ð¹', 'Синий')
        tagtext = tagtext.replace('Ð·Ð°Ð´Ð½Ð¸Ð¹', 'Задний')
        tagtext = tagtext.replace('ÐºÐ°Ð±ÑÐ¸Ð¾Ð»ÐµÑ', 'Кабриолет')
        tagtext = tagtext.replace('â\Ð\xadÐ»ÐµÐºÑÑÐ¾', 'Электро')
        tagtext = tagtext.replace('â\ÐÐ¸Ð±ÑÐ¸Ð´', 'Гибрид')
        tagtext = tagtext.replace('Ð²Ð°ÑÐ¸Ð°ÑÐ¾Ñ', 'Вариатор')
        tagtext = tagtext.replace('Ð¿Ð¸ÐºÐ°Ð¿', 'Пикап')
        tagtext = tagtext.replace('ÐºÐ°Ð±Ð¸Ð½Ð°', 'кабина')
        tagtext = tagtext.replace('Ð´Ð²Ð¾Ð¹Ð½Ð°Ñ\x8f', 'двойная')
        tagtext = tagtext.replace('ÐºÑÐ¿Ðµ', 'Купе')
        tagtext = tagtext.replace('ÑÑÑÐ³Ð¾Ð½', 'Фургон')
        tagtext = tagtext.replace('Ð¿Ð¾Ð»ÑÑÐ¾ÑÐ½Ð°Ñ\x8f', 'полуторная')  
        data2.append(tagtext)
            
    prices2 = []
    for tag in prices: # раскодировка из UTF-8
        tagtext = tag.text
        tagtext = tagtext.replace('Â', '')
        tagtext = tagtext.replace(u'\xa0', '')
        tagtext = tagtext.replace(u'\x82', '')
        tagtext = tagtext.replace('Ð´', '')
        tagtext = tagtext.replace('Ð¾Ñ', '')
        tagtext = tagtext.replace('Ð¾', '')
        tagtext = tagtext.replace('â', '')
        tagtext = tagtext.replace('½', '')
        tagtext = tagtext.lstrip(' ')
        prices2.append(tagtext)

    years2 = []
    for tag in years: # раскодировка из UTF-8
        tagtext = tag.text
        years2.append(tagtext)
            
    probegs2 = []
    for tag in probegs: # раскодировка из UTF-8
        tagtext = tag.text
        tagtext = tagtext.replace('Â', '')
        tagtext = tagtext.replace(u'\xa0', '')
        tagtext = tagtext.replace('Ðº', '')
        tagtext = tagtext.replace('Ð¼', '')
        tagtext = tagtext.replace('Ð\x9dÐ¾Ð²Ñ\x8bÐ¹', 'Новый')
        probegs2.append(tagtext)

    oilvolumes = []
    for i in range(0, len(data2)):
        oilvolumes.append(data2[i][0:data2[i].rfind('/')].rstrip(' '))
            
    for i in range(0, len(data2) - 1):
        data2[i] = titles2[i] + ' ' + data2[i] + ' ' + ' ' + years2[i] + ' ' + probegs2[i] + ' ' + links2[i]

    bodytypes = []
    for i in range(0, len(data2)):
        if data2[i].find('Минивэн') != -1:
            bodytypes.append('Минивэн')
        elif data2[i].find('Внедорожник 5 дв.') != -1:
            bodytypes.append('Внедорожник 5 дв.')
        elif data2[i].find('Хэтчбек 3 дв.') != -1:
            bodytypes.append('Хэтчбек 3 дв.')
        elif data2[i].find('Хэтчбек 5 дв.') != -1:
            bodytypes.append('Хэтчбек 5 дв.')
        elif data2[i].find('Универсал 5 дв.') != -1:
            bodytypes.append('Универсал 5 дв.')
        elif data2[i].find('Компактвэн') != -1:
            bodytypes.append('Компактвэн')
        elif data2[i].find('Лифтбэк') != -1:
            bodytypes.append('Лифтбэк')
        elif data2[i].find('Кабриолет') != -1:
            bodytypes.append('Кабриолет')
        elif data2[i].find('Фургон') != -1:
            bodytypes.append('Фургон')
        elif data2[i].find('Купе') != -1:
            bodytypes.append('Купе')
        elif data2[i].find('Пикап полуторная кабина') != -1:
            bodytypes.append('Пикап полуторная кабина')
        elif data2[i].find('Пикап двойная кабина') != -1:
            bodytypes.append('Пикап двойная кабина')
        elif data2[i].find('Innovation') != -1:
            bodytypes.append('Innovation')
        else:            
            bodytypes.append('Уточняйте')        
    enginetypes = []
    for i in range(0, len(data2)):
        if data2[i].find('Бензин') != -1:
            enginetypes.append('Бензин')
        elif data2[i].find('Дизель') != -1:
            enginetypes.append('Дизель')
        elif data2[i].find('Гибрид') != -1:
            enginetypes.append('Гибрид')
        elif data2[i].find('Электро') != -1:
            enginetypes.append('Электро')
        else:
            enginetypes.append('Уточняйте')

            
    drivetypes = []
    for i in range(0, len(data2)):
        if data2[i].find('Передний') != -1:
            drivetypes.append('Передний')
        elif data2[i].find('Задний') != -1:
            drivetypes.append('Задний')
        elif data2[i].find('Полный') != -1:
            drivetypes.append('Полный')
        else:
            drivetypes.append('Уточняйте')

    transmissiontypes = []
    for i in range(0, len(data2)):
        if data2[i].find('Автомат') != -1:
            transmissiontypes.append('Автомат')
        elif data2[i].find('Робот') != -1:
            transmissiontypes.append('Робот')
        elif data2[i].find('Вариатор') != -1:
            transmissiontypes.append('Вариатор')
        elif data2[i].find('Механика') != -1:
            transmissiontypes.append('Механика')
        else:
            transmissiontypes.append('Уточняйте')

    data3 = []
    for i in range(0, len(data2)):
        data3.append({'title': titles2[i], 'oilvolume': oilvolumes[i], 'bodytype': bodytypes[i], 'enginetype': enginetypes[i], 'drivetype': drivetypes[i],
                        'transmissiontype': transmissiontypes[i], 'year': years2[i], 'probeg': probegs2[i], 'link': links2[i]})
    return data3
    
    
