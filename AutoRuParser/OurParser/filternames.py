cities = {'Московская область': 'moskovskaya_oblast', 'Москва': 'moskva', 
              'Санкт-Петербург': 'sankt-peterburg', 'Владимир': 'vladimir',
              'Волгоград': 'volgograd', 'Воронеж': 'voronezh', 'Екатеринбург': 'ekaterinburg', 
		      'Иваново': 'ivanovo', 'Казань':'kazan', 'Калуга': 'kaluga', 'Кострома': 'kostroma', 
		      'Краснодар': 'krasnodar', 'Красноярск': 'krasnoyarsk',
              'Нижний Новгород': 'nizhniy_novgorod', 'Новосибирск':'novosibirsk', 'Омск': 'omsk', 
		      'Пермь': 'perm', 'Ростов-на-Дону': 'rostov-na-donu', 'Самара': 'samara', 
		      'Саратов': 'saratov', 'Тверь': 'tver', 'Тула': 'tula',
              'Уфа': 'ufa', 'Челябинск': 'chelyabinsk', 'Ярославль': 'yaroslavl'} # домены для городов
			  
marks = {'Любая': '', 'AC': 'ac', 'AMC': 'amc', 'Acura': 'acura', 'Alfa Romeo': 'alfa_romeo', 
			'Alphina': 'alpina', 'Ariel': 'ariel', 'Aro': 'aro', 'Asia': 'asia', 
			'Aston Martin': 'aston_martin', 'Audi': 'audi', 'Austin Healey': 'austin_healey', 
			'BMW': 'bmw', 'BYD': 'byd', 'Bentley': 'bentley', 'Borgward': 'borgward', 
			'Brilliance': 'brlliance', 'Bugatti': 'bugatti', 'Buick': 'buick',
            'CHERYEXEED': 'cherryexeed', 'Cadillac': 'cadillac', 'Changan': 'changan', 
			'Chery': 'chery', 'Chevrolet': 'chevrolet', 'Chrysler': 'chrysler', 
			'Citroen': 'citroen', 'DKW': 'dkw', 'DS': 'ds', 'DW Hower': 'dw_hower', 
			'Dacia': 'dacia', 'Daewoo': 'daewoo', 'Daihatsu': 'daihatsu', 'Daimler': 'daimler', 
			'Datsun': 'datsun', 'Delage': 'delage', 'Derways': 'derways', 'Dodge': 'dodge', 
			'DongFong': 'dongfong', 'Doninvest': 'doninvest', 'Eagle': 'eagle', 
			'Excalibur': 'excalibur', 'FAW': 'faw', 'Ferrari': 'ferrari', 'Fiat': 'fiat', 
			'Fisker': 'fisker', 'Ford': 'ford', 'GAC': 'gac', 'GMC': 'gmc', 'Geely': 'geely', 
			'Genesis': 'genesis', 'Great Wall': 'great_wall', 'Hafei': 'hafei', 'Haima': 'haima', 
			'Haval': 'haval', 'Hawtai':  'hawtai', 'Heinkel':  'heinkel', 'Honda': 'honda',
            'Hummer': 'hummer', 'Hyundai': 'hyundai', 'Infiniti': 'infiniti',
			'Iran Khodro': 'iran_khodro', 'Isuzu': 'isuzu', 'JAC': 'jac', 'Jaguar':  'jaguar',
            'Jeep': 'jeep', 'Kia': 'kia', 'LADA': 'vaz', 'Lamborghini': 'lamborghini', 
			'Lancia': 'lancia', 'Land Rover': 'land_rover', 'Lexus': 'lexus', 'Lifan': 'lifan',
            'Lincoln': 'lincoln', 'Luxgen': 'luxgen', 'MG': 'mg', 'MINI': 'mini', 
			'Maserati': 'maserati', 'Maybach': 'maybach', 'Mazda': 'mazda', 'McLaren': 'mclaren',
            'Mercedes-Benz': 'mercedes', 'Mercury': 'mercury', 'Metrocab': 'metrocab', 
			'Mitsubishi': 'mitsubishi', 'Mitsuoka': 'mitsuoka', 'Nissan': 'nissan', 
			'Oldsmobile': 'oldsmobile', 'Opel': 'opel', 'Puch': 'puch', 'Packard': 'packard', 
			'Peugeot': 'peugeot', 'Plymouth': 'plymouth', 'Pontiac': 'pontiac', 
			'Porsche': 'porsche', 'RAM': 'ram', 'Ravon': 'ravon', 'Renault': 'renault', 
			'Rolls-Royce': 'rolls_royce', 'Rover': 'rover', 'SEAT': 'seat', 'Saab': 'saab', 
			'Saturn': 'saturn', 'Scion': 'scion', 'Shanghai Maple': 'shanghai_maple', 
			'Skoda': 'skoda', 'Smart': 'smart', 'SsangYong': 'ssangyong', 'Subaru': 'subaru', 
			'Suzuki': 'suzuki', 'Tatra': 'tatra', 'Tesla': 'tesla', 'Toyota': 'toyota', 
			'Triumph': 'triumph', 'Volkswagen': 'volkswagen', 'Volvo': 'volvo', 'Vortex': 'vortex', 
			'Willys': 'willys', 'Xinkai': 'xinkai', 'ZX': 'zx', 'Zotye': 'zotye', 'ГАЗ': 'gaz', 
			'Гоночный автомобиль': 'promo_auto', 'ЗАЗ': 'zaz', 'ЗИЛ': 'zil', 'ЗиС': 'zis', 'ИЖ': 
			'ig', 'ЛуАЗ': 'luaz', 'Москвич': 'moscvich', 'СМЗ': 'smz', 'ТагАЗ': 'tagaz', 'УАЗ': 'uaz'} # домены для марок
			
bodytypes = {'Любой': '', 'Седан': 'SEDAN', 'Хэтчбек 3 дв.': 'HATCHBACK_3_DOORS', 
	             'Хэтчбек 5 дв.': 'HATCHBACK_5_DOORS', 'Лифтбек': 'LIFTBACK', 
				 'Внедорожник 3 дв.': 'ALLROAD_3_DOORS', 'Внедорожник 5 дв.': 'ALLROAD_5_DOORS',
				 'Универсал': 'WAGON', 'Купе': 'COUPE', 'Минивэн': 'MINIVAN', 'Пикап': 'PICKUP', 
				 'Лимузин': 'LIMOUSINE', 'Фургон': 'VAN', 'Кабриолет': 'CABRIO'} # домены для кузовов
				 
transmissiontypes = {'Любая': '', 'Автоматическая': 'AUTOMATIC', 'Робот': 'ROBOT', 'Вариатор': 'VARIATOR', 
	                     'Механическая': 'MECHANICAL'} # домены для коробок
						 
enginetypes = {'Любой': '', 'Бензин': 'GASOLINE', 'Дизель': 'DIESEL', 'Гибрид': 'HYBRID', 
	               'Электро': 'ELECTRO', 'Турбированный': 'TURBO', 'Атмосферный': 'ATMO',
	                     'Газобалонное оборудование': 'LPG'} # домены для двигателей
						 
geartypes = {'Любой': '', 'Передний': 'FORWARD_CONTROL', 'Задний': 'REAR_DRIVE', 'Полный': 'ALL_WHEEL_DRIVE'} # домены для приводов

colors = {'Любой': '', 'Черный': '040001', 'Серебристый': 'CACECB', 'Белый': 'FAFBFB', 'Серый': '97948F', 'Синий': '0000CC', 
                  'Красный': 'EE1D19', 'Зеленый': '007F00', 'Коричневый': '200204', 'Бежевый': 'C49648', 
				  'Голубой': '22A0F8', 'Золотистый': 'DEA522', 'Пурпурный': '660099',
			      'Фиолетовый': '4A2197', 'Желтый': 'FFD600', 'Оранжевый': 'FF8649', 'Розовый': 'FFC0CB'} # домены для цветов

cities2 = cities.keys() # Список названий городов
marks2 = marks.keys() # Список названий марок
bodytypes2 = bodytypes.keys() # Список названий кузовов
transmissiontypes2 = transmissiontypes.keys() # Список названий коробок
enginetypes2 = enginetypes.keys() # Список названий двигателей
geartypes2 = geartypes.keys() # Список названий приводов
colors2 = colors.keys() # Список названий цветов

