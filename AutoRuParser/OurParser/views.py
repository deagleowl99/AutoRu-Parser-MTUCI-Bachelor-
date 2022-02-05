# -*- coding: utf-8 -*-
from .models import UserU
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.urls import reverse
from django.conf import settings
from django.core.signing import Signer
from django.core import signing
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from OurParser import myparser
from OurParser import filternames
from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup
import csv
import os
import pandas as pd
		
def registration(request): # представление для регистрации пользователей
    if request.method == "POST": # Если пользователь нажимает на кнопку "Регистрация"
        form = { # Данные, которые заполняются в форме
			'surname': request.POST["surname"], # Фамилия
			'name': request.POST["name"],       # Имя
			'fathername': request.POST["fathername"], # Отечество
            'login': request.POST["login"], # Логин
            'mail': request.POST["mail"],   # Почта
            'password': request.POST["password"], # Пароль	
        }
        if form["surname"] and form["name"] and form["fathername"] and form["login"] and form["mail"] and form["password"]: # Проверка на отсутствие пустых полей
            try: # Если логин пользователя не уникален
                UserU.objects.get(username = form["login"]) 
                form['errors'] = u"Не уникальное имя пользователя!" # Вывод ошибки
                return render(request, 'registration.html', {'form': form}) # Возврат на страницу регистрации
            except UserU.DoesNotExist:
                try: # Если почта пользователя не уникальна
                    UserU.objects.get(email = form["mail"])
                    form['errors'] = u"Не уникальная почта!" # Вывод ошибки
                    return render(request, 'registration.html', {'form': form}) # Возврат на страницу регистрации
                except UserU.DoesNotExist:
                    if  not "@" in form["mail"] or not "." in form["mail"] or form["mail"].find("@") > form["mail"].rfind("."): # Если почта введена в не правильном формате
                        form['errors'] = u"Почта введена не правильно!" # Вывод ошибки
                        return render(request, 'registration.html', {'form': form}) # Возврат на страницу регистрации
                    else: # Если почта правильно введена
                        signer = Signer() # Экземпляр встроенного класса для шифратора строки
                        newusername=signing.dumps(list(form["login"])) # Шифрование логина					
                        user=UserU.objects.create_user(newusername, form["mail"], form["password"]) # Создание экземпляра пользователя
                        user.Surname=form["surname"] 
                        user.Name=form["name"] 
                        user.Fathername=form["fathername"]           
                        user.save() # Сохранение новых данных в БД
                        return redirect('autoruparser') # Возврат на страницу парсера
        else: # Если остались пустые поля
            form['errors'] = u"У вас имеются пустые поля!" # Вывод ошибки
            return render(request, 'registration.html', {"form": form}) # Возврат на страницу регистрации
    else:
        return render(request, 'registration.html', {}) # Переход на страницу регистрации с посторонней страницы приложения
	
def login_user(request): # представление для авторизации пользователей
    if request.method == "POST": # Если пользователь нажимает на кнопку "Вход"
        form = { # Данные, которые заполняются в форме
            'login': request.POST["login"], # Логин
            'password': request.POST["password"], # Почта
			'email': request.POST["email"] # Пароль
        }
        if form["login"] and form["password"] and form["email"]: # Проверка на отсутствие пустых полей
            user2=UserU.objects.get(email=form["email"])
            if form["login"] != ''.join(list(signing.loads(user2.username))): # Если отсутствует соответствие введеных данных
                form['errors'] = u"Неверный логин или пароль" # Вывод ошибки
                return render(request, 'login.html', {'form': form}) # Возврат на страницу авторизации
            else: # Если Данные были правильно введены			
                login(request, user2) # Выполнение аутентификации
                return redirect('autoruparser') # Возврат на страницу парсера
        else: # Если остались пустые поля
            user2=UserU.objects.get(email=form["email"])
            form['errors'] = u"У вас имеются пустые поля!" # Вывод ошибки
            return render(request, 'login.html', {'form': form}) # Возврат на страницу авторизации
    else:
        return render(request, 'login.html', {}) # Переход на страницу регистрации с посторонней страницы приложения
		
def autoruparser(request):
    unknowncity = ''
    unknownmark = ''
    unknownbodytype = ''
    unknowntransmissiontype = ''
    unknownenginetype = ''
    unknowngeartype = ''
    unknowncolor = ''
    unknownyearfrom = ''
    unknownyearto = ''
    unknownkmagefrom = ''
    unknownkmageto = ''
    unknownaccelerationfrom = ''
    unknownaccelerationto = ''
    unknowndisplacementfrom = ''
    unknowndisplacementto = ''
    unknownpricefrom = ''
    unknownpriceto = ''
    unknownpowerfrom = ''
    unknownpowerto = ''
    unknownfuelrateto = ''
    unknownclearancefrom = ''
    if request.method == "POST":
        if not request.POST.get("city") or not request.POST.get("pagenumber"):
            if not request.POST.get("city"):
                form = {}
                form['errors'] = "Вы не указали город!"
                return render(request, 'autoruparser.html', {'form': form, "cities2": filternames.cities2, "marks2": filternames.marks2, "bodytypes2": filternames.bodytypes2, "transmissiontypes": filternames.transmissiontypes2, "enginetypes": filternames.enginetypes2, "geartypes": filternames.geartypes2, "colors": filternames.colors2})
            if not request.POST.get("pagenumber"):
                form = {}
                form['errors'] = "Вы не указали количество страниц для сбора данных!"
                return render(request, 'autoruparser.html', {'form': form, "cities2": filternames.cities2, "marks2": filternames.marks2, "bodytypes2": filternames.bodytypes2, "transmissiontypes": filternames.transmissiontypes2, "enginetypes": filternames.enginetypes2, "geartypes": filternames.geartypes2, "colors": filternames.colors2})	
        else:
            if request.POST.get("city") and request.POST.get("pagenumber"):
                form = {
                    'city': request.POST["city"],
                    'pagenumber': request.POST["pagenumber"]
                }
                choosecity=request.POST.get("city")
                choosecity2=filternames.cities.get(choosecity)
                if not form["pagenumber"].isdigit():
                    form['errors'] = u"Текстовые поля содержат только цифры!"
                    return render(request, 'autoruparser.html', {'form': form, "cities2": filternames.cities2, "marks2": filternames.marks2, "bodytypes2": filternames.bodytypes2, "transmissiontypes": filternames.transmissiontypes2, "enginetypes": filternames.enginetypes2, "geartypes": filternames.geartypes2, "colors": filternames.colors2})
                else:
                    if int(form["pagenumber"]) == 0:
                        form['errors'] = u"Число страниц всегда больше единицы!"
                        return render(request, 'autoruparser.html', {'form': form, "cities2": filternames.cities2, "marks2": filternames.marks2, "bodytypes2": filternames.bodytypes2, "transmissiontypes": filternames.transmissiontypes2, "enginetypes": filternames.enginetypes2, "geartypes": filternames.geartypes2, "colors": filternames.colors2})
                    else:
                        pagenumber=int(request.POST.get("pagenumber"))
                if request.POST.get("mark"):
                    form = {
					     'mark': request.POST.get("mark")
                    }
                    choosemark=request.POST.get("mark")
                    choosemark2=filternames.marks.get(choosemark)
                    unknownmark=choosemark2
                if request.POST.get("bodytype"):
                    form = {
                         'bodytype': request.POST["bodytype"]
                    }
                    choosebodytype=request.POST.get("bodytype")
                    choosebodytype2=filternames.bodytypes.get(choosebodytype)
                    unknownbodytype=choosebodytype2
                if request.POST.get("transmissiontype"):
                    form = {
                         'transmissiontype': request.POST["transmissiontype"]
                    }
                    choosetransmissiontype=request.POST.get("transmissiontype")
                    choosetransmissiontype2=filternames.transmissiontypes.get(choosetransmissiontype)
                    unknowntransmissiontype=choosetransmissiontype2
                if request.POST.get("enginetype"):
                    form = {
                         'enginetype': request.POST["enginetype"]
                    }
                    chooseenginetype=request.POST.get("enginetype")
                    chooseenginetype2=filternames.enginetypes.get(chooseenginetype)
                    unknownenginetype=chooseenginetype2
                if request.POST.get("geartype"):
                    form = {
                         'geartype': request.POST["geartype"]
                    }
                    choosegeartype=request.POST.get("geartype")
                    choosegeartype2=filternames.geartypes.get(choosegeartype)
                    unknowngeartype=choosegeartype2
                if request.POST.get("color"):
                    form = {
                         'color': request.POST["color"]
                    }
                    choosecolor=request.POST.get("color")
                    choosecolor2=filternames.colors.get(choosecolor)
                    unknowncolor=choosecolor2
                if request.POST.get("yearfrom"):
                    form = {
                         'yearfrom': request.POST["yearfrom"]
                    }
                    if not form["yearfrom"].isdigit():
                        form['errors'] = u"Текстовые поля содержат только цифры!"
                        return render(request, 'autoruparser.html', {'form': form, "cities2": filternames.cities2, "marks2": filternames.marks2, "bodytypes2": filternames.bodytypes2, "transmissiontypes": filternames.transmissiontypes2, "enginetypes": filternames.enginetypes2, "geartypes": filternames.geartypes2, "colors": filternames.colors2})
                    else:
                        unknownyearfrom=request.POST.get("yearfrom")
                if request.POST.get("yearto"):
                    form = {
                         'yearto': request.POST["yearto"]
                    }
                    if not form["yearto"].isdigit():
                        form['errors'] = u"Текстовые поля содержат только цифры!"
                        return render(request, 'autoruparser.html', {'form': form, "cities2": filternames.cities2, "marks2": filternames.marks2, "bodytypes2": filternames.bodytypes2, "transmissiontypes": filternames.transmissiontypes2, "enginetypes": filternames.enginetypes2, "geartypes": filternames.geartypes2, "colors": filternames.colors2})
                    else:
                        unknownyearto=request.POST.get("yearto")
                if request.POST.get("powerfrom"):
                    form = {
                         'powerfrom': request.POST["powerfrom"]
                    }
                    if not form["powerfrom"].isdigit():
                        form['errors'] = u"Текстовые поля содержат только цифры!"
                        return render(request, 'autoruparser.html', {'form': form, "cities2": filternames.cities2, "marks2": filternames.marks2, "bodytypes2": filternames.bodytypes2, "transmissiontypes": filternames.transmissiontypes2, "enginetypes": filternames.enginetypes2, "geartypes": filternames.geartypes2, "colors": filternames.colors2})
                    else:
                        unknownpowerfrom=request.POST.get("powerfrom")
                if request.POST.get("powerto"):
                    form = {
                         'powerto': request.POST["powerto"]
                    }
                    if not form["powerto"].isdigit():
                        form['errors'] = u"Текстовые поля содержат только цифры!"
                        return render(request, 'autoruparser.html', {'form': form, "cities2": filternames.cities2, "marks2": filternames.marks2, "bodytypes2": filternames.bodytypes2, "transmissiontypes": filternames.transmissiontypes2, "enginetypes": filternames.enginetypes2, "geartypes": filternames.geartypes2, "colors": filternames.colors2})
                    else:
                        unknownpowerto=request.POST.get("powerto")
                if request.POST.get("kmagefrom"):
                    form = {
                         'kmagefrom': request.POST["kmagefrom"]
                    }
                    if not form["kmagefrom"].isdigit():
                        form['errors'] = u"Текстовые поля содержат только цифры!"
                        return render(request, 'autoruparser.html', {'form': form, "cities2": filternames.cities2, "marks2": filternames.marks2, "bodytypes2": filternames.bodytypes2, "transmissiontypes": filternames.transmissiontypes2, "enginetypes": filternames.enginetypes2, "geartypes": filternames.geartypes2, "colors": filternames.colors2})
                    else:
                        unknownkmagefrom=request.POST.get("kmagefrom")
                if request.POST.get("kmageto"):
                    form = {
                         'kmageto': request.POST["kmageto"]
                    }
                    if not form["kmageto"].isdigit():
                        form['errors'] = u"Текстовые поля содержат только цифры!"
                        return render(request, 'autoruparser.html', {'form': form, "cities2": filternames.cities2, "marks2": filternames.marks2, "bodytypes2": filternames.bodytypes2, "transmissiontypes": filternames.transmissiontypes2, "enginetypes": filternames.enginetypes2, "geartypes": filternames.geartypes2, "colors": filternames.colors2})
                    else:
                        unknownkmageto=request.POST.get("kmageto")
                if request.POST.get("accelerationfrom"):
                    form = {
                         'accelerationfrom': request.POST["accelerationfrom"]
                    }
                    if not form["accelerationfrom"].isdigit():
                        form['errors'] = u"Текстовые поля содержат только цифры!"
                        return render(request, 'autoruparser.html', {'form': form, "cities2": filternames.cities2, "marks2": filternames.marks2, "bodytypes2": filternames.bodytypes2, "transmissiontypes": filternames.transmissiontypes2, "enginetypes": filternames.enginetypes2, "geartypes": filternames.geartypes2, "colors": filternames.colors2})
                    else:
                        unknownaccelerationfrom=request.POST.get("accelerationfrom")
                if request.POST.get("accelerationto"):
                    form = {
                         'accelerationto': request.POST["accelerationto"]
                    }
                    if not form["accelerationto"].isdigit():
                        form['errors'] = u"Текстовые поля содержат только цифры!"
                        return render(request, 'autoruparser.html', {'form': form, "cities2": filternames.cities2, "marks2": filternames.marks2, "bodytypes2": filternames.bodytypes2, "transmissiontypes": filternames.transmissiontypes2, "enginetypes": filternames.enginetypes2, "geartypes": filternames.geartypes2, "colors": filternames.colors2})
                    else:
                        unknownaccelerationto=request.POST.get("accelerationto")
                if request.POST.get("displacementfrom"):
                    form = {
                         'displacementfrom': request.POST["displacementfrom"]
                    }
                    if not form["displacementfrom"].isdigit():
                        form['errors'] = u"Текстовые поля содержат только цифры!"
                        return render(request, 'autoruparser.html', {'form': form, "cities2": filternames.cities2, "marks2": filternames.marks2, "bodytypes2": filternames.bodytypes2, "transmissiontypes": filternames.transmissiontypes2, "enginetypes": filternames.enginetypes2, "geartypes": filternames.geartypes2, "colors": filternames.colors2})
                    else:
                        unknowndisplacementfrom=request.POST.get("displacementfrom")
                if request.POST.get("displacementto"):
                    form = {
                         'displacementto': request.POST["displacementto"]
                    }
                    if not form["displacementto"].isdigit():
                        form['errors'] = u"Текстовые поля содержат только цифры!"
                        return render(request, 'autoruparser.html', {'form': form, "cities2": filternames.cities2, "marks2": filternames.marks2, "bodytypes2": filternames.bodytypes2, "transmissiontypes": filternames.transmissiontypes2, "enginetypes": filternames.enginetypes2, "geartypes": filternames.geartypes2, "colors": filternames.colors2})
                    else:
                        unknowndisplacementto=request.POST.get("displacementto")
                if request.POST.get("pricefrom"):
                    form = {
                         'pricefrom': request.POST["pricefrom"]
                    }
                    if not form["pricefrom"].isdigit():
                        form['errors'] = u"Текстовые поля содержат только цифры!"
                        return render(request, 'autoruparser.html', {'form': form, "cities2": filternames.cities2, "marks2": filternames.marks2, "bodytypes2": filternames.bodytypes2, "transmissiontypes": filternames.transmissiontypes2, "enginetypes": filternames.enginetypes2, "geartypes": filternames.geartypes2, "colors": filternames.colors2})
                    else:
                        unknownpricefrom=request.POST.get("pricefrom")
                if request.POST.get("priceto"):
                    form = {
                         'priceto': request.POST["priceto"]
                    }
                    if not form["priceto"].isdigit():
                        form['errors'] = u"Текстовые поля содержат только цифры!"
                        return render(request, 'autoruparser.html', {'form': form, "cities2": filternames.cities2, "marks2": filternames.marks2, "bodytypes2": filternames.bodytypes2, "transmissiontypes": filternames.transmissiontypes2, "enginetypes": filternames.enginetypes2, "geartypes": filternames.geartypes2, "colors": filternames.colors2})
                    else:
                        unknownpriceto=request.POST.get("priceto")
                if request.POST.get("fuelrateto"):
                    form = {
                         'fuelrateto': request.POST["fuelrateto"]
                    }
                    if not form["fuelrateto"].isdigit():
                        form['errors'] = u"Текстовые поля содержат только цифры!"
                        return render(request, 'autoruparser.html', {'form': form, "cities2": filternames.cities2, "marks2": filternames.marks2, "bodytypes2": filternames.bodytypes2, "transmissiontypes": filternames.transmissiontypes2, "enginetypes": filternames.enginetypes2, "geartypes": filternames.geartypes2, "colors": filternames.colors2})
                    else:
                        unknownfuelrateto=request.POST.get("fuelrateto")
                if request.POST.get("clearancefrom"):
                    form = {
                         'clearancefrom': request.POST["clearancefrom"]
                    }
                    if not form["clearancefrom"].isdigit():
                        form['errors'] = u"Текстовые поля содержат только цифры!"
                        return render(request, 'autoruparser.html', {'form': form, "cities2": filternames.cities2, "marks2": filternames.marks2, "bodytypes2": filternames.bodytypes2, "transmissiontypes": filternames.transmissiontypes2, "enginetypes": filternames.enginetypes2, "geartypes": filternames.geartypes2, "colors": filternames.colors2})
                    else:
                        unknownclearancefrom=request.POST.get("clearancefrom")						
                form['errors'] = "https://auto.ru/" + str(choosecity2) +  "/cars/all/?catalog_filter=mark%3D" + unknownmark.upper() + "&body_type_group=" + str(unknownbodytype) + "&transmission=" + str(unknowntransmissiontype) + "&engine_group=" + str(unknownenginetype) + "&gear_type=" + str(unknowngeartype) + "&color=" + str(unknowncolor) + "&year_from=" + unknownyearfrom + "&year_to=" + unknownyearto + "&km_age_from=" + unknownkmagefrom + "&km_age_to=" + unknownkmageto + "&acceleration_from=" + unknownaccelerationfrom + "&acceleration_to=" + unknownaccelerationto + "&displacement_from=" + unknowndisplacementfrom + "&displacement_to=" + unknowndisplacementto + "&price_from=" + unknownpricefrom + "&price_to=" + unknownpriceto + "&fuel_rate_to=" + unknownfuelrateto + "&clearance_from=" + unknownclearancefrom
                URL =  "https://auto.ru/" + str(choosecity2) +  "/cars/all/?catalog_filter=mark%3D" + unknownmark.upper() + "&body_type_group=" + str(unknownbodytype) + "&transmission=" + str(unknowntransmissiontype) + "&engine_group=" + str(unknownenginetype) + "&gear_type=" + str(unknowngeartype) + "&color=" + str(unknowncolor) + "&year_from=" + unknownyearfrom + "&year_to=" + unknownyearto + "&power_from=" + unknownpowerfrom + "&power_to=" + unknownpowerto + "&km_age_from=" + unknownkmagefrom + "&km_age_to=" + unknownkmageto + "&acceleration_from=" + unknownaccelerationfrom + "&acceleration_to=" + unknownaccelerationto + "&displacement_from=" + unknowndisplacementfrom + "&displacement_to=" + unknowndisplacementto + "&price_from=" + unknownpricefrom + "&price_to=" + unknownpriceto + "&fuel_rate_to=" + unknownfuelrateto + "&clearance_from=" + unknownclearancefrom
                html = myparser.get_html(URL)
                if html.status_code == 200:
                    data3 = []
                    for page in range(1, pagenumber + 1):
                        html = myparser.get_html(URL, params={'page': page})
                        data3.extend(myparser.parse(html.text))
                    with open('D:\\cars2.csv', 'w', newline='') as file:
                        writer = csv.writer(file, delimiter=';')
                        writer.writerow(['Объем / Мощность', 'Кузов', 'Двигатель', 'Привод', 'Коробка', 'Год производства', 'Пробег (км)', 'Ссылка'])
                        for data in data3:
                            writer.writerow([data['oilvolume'], data['bodytype'], data['enginetype'], data['drivetype'],
                                             data['transmissiontype'], data['year'], data['probeg'], data['link']])
                else:
                    pass					
                return render(request, 'autoruparser.html', {'form': form, "cities2": filternames.cities2, "marks2": filternames.marks2, "bodytypes2": filternames.bodytypes2, "transmissiontypes": filternames.transmissiontypes2, "enginetypes": filternames.enginetypes2, "geartypes": filternames.geartypes2, "colors": filternames.colors2, "data3": data3})
    else:
        return render(request, 'autoruparser.html', {"cities2": filternames.cities2, "marks2": filternames.marks2, "bodytypes2": filternames.bodytypes2, "transmissiontypes": filternames.transmissiontypes2, "enginetypes": filternames.enginetypes2, "geartypes": filternames.geartypes2, "colors": filternames.colors2})
    return render(request, 'autoruparser.html', {"cities2": filternames.cities2, "marks2": filternames.marks2, "bodytypes2": filternames.bodytypes2, "transmissiontypes": filternames.transmissiontypes2, "enginetypes": filternames.enginetypes2, "geartypes": filternames.geartypes2, "colors": filternames.colors2})
# Create your views here.
