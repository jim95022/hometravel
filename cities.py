cities = [(0, 'Москва'), (1, 'Санкт-Петербург'), (2, 'Новосибирск'), (3, 'Екатеринбург'), (4, 'Нижний Новгород'), (5, 'Казань'), (6, 'Челябинск'), (7, 'Омск'), (8, 'Самара'), (9, 'Ростов-на-Дону'), (10, 'Уфа'), (11, 'Красноярск'), (12, 'Пермь'), (13, 'Воронеж'), (14, 'Волгоград'), (15, 'Краснодар'), (16, 'Саратов'), (17, 'Тюмень'), (18, 'Тольятти'), (19, 'Ижевск'), (20, 'Барнаул'), (21, 'Иркутск'), (22, 'Ульяновск'), (23, 'Хабаровск'), (24, 'Владивосток'), (25, 'Ярославль'), (26, 'Махачкала'), (27, 'Томск'), (28, 'Оренбург'), (29, 'Кемерово'), (30, 'Новокузнецк'), (31, 'Рязань'), (32, 'Астрахань'), (33, 'Набережные Челны'), (34, 'Пенза'), (35, 'Липецк'), (36, 'Киров'), (37, 'Тула'), (38, 'Чебоксары'), (39, 'Калининград'), (40, 'Курск'), (41, 'Улан-Удэ'), (42, 'Ставрополь'), (43, 'Севастополь'), (44, 'Магнитогорск'), (45, 'Тверь'), (46, 'Иваново'), (47, 'Брянск'), (48, 'Сочи'), (49, 'Белгород'), (50, 'Нижний Тагил'), (51, 'Владимир'), (52, 'Архангельск'), (53, 'Сургут'), (54, 'Калуга'), (55, 'Чита'), (56, 'Симферополь'), (57, 'Смоленск'), (58, 'Волжский'), (59, 'Курган'), (60, 'Орёл'), (61, 'Череповец'), (62, 'Вологда'), (63, 'Владикавказ'), (64, 'Саранск'), (65, 'Мурманск'), (66, 'Якутск'), (67, 'Подольск'), (68, 'Тамбов'), (69, 'Грозный'), (70, 'Стерлитамак'), (71, 'Кострома'), (72, 'Петрозаводск'), (73, 'Нижневартовск'), (74, 'Йошкар-Ола'), (75, 'Новороссийск'), (76, 'Балашиха'), (77, 'Таганрог'), (78, 'Комсомольск-на-Амуре'), (79, 'Сыктывкар'), (80, 'Химки'), (81, 'Нальчик'), (82, 'Шахты'), (83, 'Братск'), (84, 'Нижнекамск'), (85, 'Дзержинск'), (86, 'Орск'), (87, 'Ангарск'), (88, 'Благовещенск'), (89, 'Великий Новгород'), (90, 'Энгельс'), (91, 'Старый Оскол'), (92, 'Королёв'), (93, 'Псков'), (94, 'Бийск'), (95, 'Мытищи'), (96, 'Прокопьевск'), (97, 'Балаково'), (98, 'Рыбинск'), (99, 'Южно-Сахалинск'), (100, 'Армавир'), (101, 'Люберцы'), (102, 'Северодвинск'), (103, 'Петропавловск-Камчатский'), (104, 'Норильск'), (105, 'Абакан'), (106, 'Сызрань'), (107, 'Новочеркасск'), (108, 'Каменск-Уральский'), (109, 'Волгодонск'), (110, 'Златоуст'), (111, 'Уссурийск'), (112, 'Электросталь'), (113, 'Находка'), (114, 'Салават'), (115, 'Миасс'), (116, 'Альметьевск'), (117, 'Березники'), (118, 'Керчь'), (119, 'Рубцовск'), (120, 'Пятигорск'), (121, 'Копейск'), (122, 'Красногорск'), (123, 'Майкоп'), (124, 'Коломна'), (125, 'Одинцово'), (126, 'Ковров'), (127, 'Нефтекамск'), (128, 'Хасавюрт'), (129, 'Кисловодск'), (130, 'Новомосковск'), (131, 'Серпухов'), (132, 'Новочебоксарск'), (133, 'Нефтеюганск'), (134, 'Первоуральск'), (135, 'Щёлково'), (136, 'Черкесск'), (137, 'Дербент'), (138, 'Орехово-Зуево'), (139, 'Батайск'), (140, 'Невинномысск'), (141, 'Димитровград'), (142, 'Новый Уренгой'), (143, 'Кызыл'), (144, 'Камышин'), (145, 'Октябрьский'), (146, 'Домодедово'), (147, 'Муром'), (148, 'Обнинск'), (149, 'Назрань'), (150, 'Каспийск'), (151, 'Раменское'), (152, 'Новошахтинск'), (153, 'Жуковский'), (154, 'Северск'), (155, 'Пушкино'), (156, 'Ноябрьск'), (157, 'Евпатория'), (158, 'Ачинск'), (159, 'Ессентуки'), (160, 'Елец'), (161, 'Артём'), (162, 'Сергиев Посад'), (163, 'Арзамас'), (164, 'Элиста'), (165, 'Новокуйбышевск'), (166, 'Бердск'), (167, 'Ногинск'), (168, 'Долгопрудный'), (169, 'Железногорск'), (170, 'Сарапул'), (171, 'Ухта'), (172, 'Междуреченск'), (173, 'Ленинск-Кузнецкий'), (174, 'Зеленодольск'), (175, 'Воткинск'), (176, 'Тобольск'), (177, 'Серов'), (178, 'Гатчина'), (179, 'Мичуринск'), (180, 'Великие Луки'), (181, 'Соликамск'), (182, 'Ханты-Мансийск'), (183, 'Глазов'), (184, 'Саров'), (185, 'Реутов'), (186, 'Воскресенск'), (187, 'Киселёвск'), (188, 'Магадан'), (189, 'Канск'), (190, 'Новотроицк'), (191, 'Каменск-Шахтинский'), (192, 'Губкин'), (193, 'Бугульма'), (194, 'Ейск'), (195, 'Кинешма'), (196, 'Кузнецк'), (197, 'Бузулук'), (198, 'Железногорск'), (199, 'Лобня'), (200, 'Чайковский'), (201, 'Усть-Илимск'), (202, 'Михайловск'), (203, 'Новоуральск'), (204, 'Азов'), (205, 'Юрга'), (206, 'Озёрск'), (207, 'Выборг'), (208, 'Кропоткин'), (209, 'Усолье-Сибирское'), (210, 'Клин'), (211, 'Балашов'), (212, 'Бор'), (213, 'Шадринск'), (214, 'Ялта'), (215, 'Троицк'), (216, 'Минеральные Воды'), (217, 'Дубна'), (218, 'Кирово-Чепецк'), (219, 'Биробиджан'), (220, 'Белово'), (221, 'Черногорск'), (222, 'Анжеро-Судженск'), (223, 'Елабуга'), (224, 'Чапаевск'), (225, 'Новоалтайск'), (226, 'Егорьевск'), (227, 'Георгиевск'), (228, 'Анапа'), (229, 'Геленджик'), (230, 'Ивантеевка'), (231, 'Феодосия'), (232, 'Чехов'), (233, 'Минусинск'), (234, 'Туймазы'), (235, 'Сосновый Бор'), (236, 'Кстово'), (237, 'Белогорск'), (238, 'Кунгур'), (239, 'Белорецк'), (240, 'Ступино'), (241, 'Всеволожск'), (242, 'Ишимбай'), (243, 'Асбест'), (244, 'Павловский Посад'), (245, 'Верхняя Пышма'), (246, 'Дмитров'), (247, 'Славянск-на-Кубани'), (248, 'Гуково'), (249, 'Ишим'), (250, 'Заречный'), (251, 'Донской'), (252, 'Вольск'), (253, 'Борисоглебск'), (254, 'Лениногорск'), (255, 'Лысьва'), (256, 'Туапсе'), (257, 'Зеленогорск'), (258, 'Будённовск'), (259, 'Буйнакск'), (260, 'Полевской'), (261, 'Россошь'), (262, 'Сибай'), (263, 'Горно-Алтайск'), (264, 'Наро-Фоминск'), (265, 'Ревда'), (266, 'Когалым'), (267, 'Кумертау'), (268, 'Клинцы'), (269, 'Чистополь'), (270, 'Котлас'), (271, 'Лабинск'), (272, 'Воркута'), (273, 'Ржев'), (274, 'Александров'), (275, 'Лесосибирск'), (276, 'Тихорецк'), (277, 'Мелеуз'), (278, 'Белебей'), (279, 'Видное'), (280, 'Сальск'), (281, 'Фрязино'), (282, 'Шуя'), (283, 'Алексин'), (284, 'Павлово'), (285, 'Краснотурьинск'), (286, 'Михайловка'), (287, 'Щёкино'), (288, 'Тихвин'), (289, 'Прохладный'), (290, 'Нерюнгри'), (291, 'Искитим'), (292, 'Апатиты'), (293, 'Крымск'), (294, 'Избербаш'), (295, 'Гусь-Хрустальный'), (296, 'Нягань'), (297, 'Лыткарино'), (298, 'Берёзовский'), (299, 'Урус-Мартан'), (300, 'Жигулёвск'), (301, 'Свободный'), (302, 'Лиски'), (303, 'Волжск'), (304, 'Вязьма'), (305, 'Краснокамск'), (306, 'Краснокаменск'), (307, 'Выкса'), (308, 'Арсеньев'), (309, 'Узловая'), (310, 'Тимашёвск'), (311, 'Солнечногорск'), (312, 'Кириши'), (313, 'Белореченск'), (314, 'Боровичи'), (315, 'Рославль'), (316, 'Черемхово'), (317, 'Дзержинский'), (318, 'Шали'), (319, 'Гудермес'), (320, 'Назарово'), (321, 'Сертолово'), (322, 'Яблоновский'), (323, 'Энем'), (324, 'Гиагинская'), (325, 'Адыгейск'), (326, 'Ханская'), (327, 'Тульский'), (328, 'Майма'), (329, 'Бирск'), (330, 'Учалы'), (331, 'Благовещенск'), (332, 'Дюртюли'), (333, 'Янаул'), (334, 'Давлеканово'), (335, 'Чишмы'), (336, 'Приютово'), (337, 'Раевский'), (338, 'Баймак'), (339, 'Иглино'), (340, 'Межгорье'), (341, 'Агидель'), (342, 'Красноусольский'), (343, 'Чекмагуш'), (344, 'Кандры'), (345, 'Месягутово'), (346, 'Буздяк'), (347, 'Толбазы'), (348, 'Северобайкальск'), (349, 'Гусиноозёрск'), (350, 'Кяхта'), (351, 'Селенгинск'), (352, 'Закаменск'), (353, 'Онохой'), (354, 'Кизляр'), (355, 'Кизилюрт'), (356, 'Дагестанские Огни'), (357, 'Карабудахкент'), (358, 'Ленинкент'), (359, 'Бабаюрт'), (360, 'Тарки'), (361, 'Семендер'), (362, 'Нижнее Казанище'), (363, 'Ахты'), (364, 'Касумкент'), (365, 'Альбурикент'), (366, 'Ботлих'), (367, 'Шамхал'), (368, 'Белиджи'), (369, 'Новый Хушет'), (370, 'Каякент'), (371, 'Мамедкала'), (372, 'Леваши'), (373, 'Шамхал-Термен'), (374, 'Южно-Сухокумск'), (375, 'Новый Кяхулай'), (376, 'Карабулак'), (377, 'Малгобек'), (378, 'Нестеровская'), (379, 'Троицкая'), (380, 'Экажево'), (381, 'Кантышево'), (382, 'Плиево'), (383, 'Сурхахи'), (384, 'Барсуки'), (385, 'Сагопши'), (386, 'Баксан'), (387, 'Нарткала'), (388, 'Майский'), (389, 'Тырныауз'), (390, 'Дыгулыбгей'), (391, 'Терек'), (392, 'Чегем'), (393, 'Нартан'), (394, 'Исламей'), (395, 'Заюково'), (396, 'Чегем Второй'), (397, 'Шалушка'), (398, 'Хасанья'), (399, 'Лагань'), (400, 'Троицкое'), (401, 'Усть-Джегута'), (402, 'Карачаевск'), (403, 'Зеленчукская'), (404, 'Учкекен'), (405, 'Сторожевая'), (406, 'Кондопога'), (407, 'Костомукша'), (408, 'Сегежа'), (409, 'Сортавала'), (410, 'Медвежьегорск'), (411, 'Кемь'), (412, 'Питкяранта'), (413, 'Беломорск'), (414, 'Печора'), (415, 'Усинск'), (416, 'Инта'), (417, 'Сосногорск'), (418, 'Емва'), (419, 'Выльгорт'), (420, 'Вуктыл'), (421, 'Воргашор'), (422, 'Джанкой'), (423, 'Алушта'), (424, 'Бахчисарай'), (425, 'Красноперекопск'), (426, 'Саки'), (427, 'Армянск'), (428, 'Судак'), (429, 'Белогорск'), (430, 'Гвардейское'), (431, 'Приморский'), (432, 'Черноморское'), (433, 'Красногвардейское'), (434, 'Щёлкино'), (435, 'Советский'), (436, 'Гаспра'), (437, 'Октябрьское'), (438, 'Козьмодемьянск'), (439, 'Медведево'), (440, 'Звенигово'), (441, 'Советский'), (442, 'Рузаевка'), (443, 'Ковылкино'), (444, 'Комсомольский'), (445, 'Зубова Поляна'), (446, 'Мирный'), (447, 'Ленск'), (448, 'Алдан'), (449, 'Айхал'), (450, 'Удачный'), (451, 'Вилюйск'), (452, 'Моздок'), (453, 'Беслан'), (454, 'Алагир'), (455, 'Ардон'), (456, 'Заводской'), (457, 'Эльхотово'), (458, 'Сунжа'), (459, 'Ногир'), (460, 'Кизляр'), (461, 'Дигора'), (462, 'Октябрьское'), (463, 'Заинск'), (464, 'Азнакаево'), (465, 'Нурлат'), (466, 'Менделеевск'), (467, 'Бавлы'), (468, 'Буинск'), (469, 'Агрыз'), (470, 'Арск'), (471, 'Кукмор'), (472, 'Васильево'), (473, 'Мензелинск'), (474, 'Камские Поляны'), (475, 'Мамадыш'), (476, 'Джалиль'), (477, 'Алексеевское'), (478, 'Тетюши'), (479, 'Уруссу'), (480, 'Нижняя Мактама'), (481, 'Каа-Хем'), (482, 'Ак-Довурак'), (483, 'Шагонар'), (484, 'Можга'), (485, 'Игра'), (486, 'Ува'), (487, 'Балезино'), (488, 'Кез'), (489, 'Камбарка'), (490, 'Кизнер'), (491, 'Завьялово'), (492, 'Саяногорск'), (493, 'Абаза'), (494, 'Усть-Абакан'), (495, 'Сорск'), (496, 'Белый Яр'), (497, 'Шира'), (498, 'Аргун'), (499, 'Курчалой'), (500, 'Ачхой-Мартан'), (501, 'Цоци-Юрт'), (502, 'Бачи-Юрт'), (503, 'Гойты'), (504, 'Автуры'), (505, 'Катыр-Юрт'), (506, 'Гелдагана'), (507, 'Гехи'), (508, 'Майртуп'), (509, 'Самашки'), (510, 'Шелковская'), (511, 'Аллерой'), (512, 'Алхан-Кала'), (513, 'Серноводская'), (514, 'Старые Атаги'), (515, 'Герменчук'), (516, 'Мескер-Юрт'), (517, 'Знаменское'), (518, 'Ассиновская'), (519, 'Ойсхара'), (520, 'Червлённая'), (521, 'Канаш'), (522, 'Алатырь'), (523, 'Шумерля'), (524, 'Цивильск'), (525, 'Кугеси'), (526, 'Вурнары'), (527, 'Заринск'), (528, 'Камень-на-Оби'), (529, 'Славгород'), (530, 'Алейск'), (531, 'Южный'), (532, 'Тальменка'), (533, 'Яровое'), (534, 'Белокуриха'), (535, 'Павловск'), (536, 'Кулунда'), (537, 'Алтайское'), (538, 'Горняк'), (539, 'Шипуново'), (540, 'Поспелиха'), (541, 'Благовещенка'), (542, 'Сибирский'), (543, 'Михайловское'), (544, 'Змеиногорск'), (545, 'Волчиха'), (546, 'Борзя'), (547, 'Агинское'), (548, 'Петровск-Забайкальский'), (549, 'Нерчинск'), (550, 'Могоча'), (551, 'Шилка'), (552, 'Чернышевск'), (553, 'Забайкальск'), (554, 'Карымское'), (555, 'Шерловая Гора'), (556, 'Балей'), (557, 'Горный'), (558, 'Первомайский'), (559, 'Хилок'), (560, 'Могойтуй'), (561, 'Атамановка'), (562, 'Новокручининский'), (563, 'Елизово'), (564, 'Вилючинск'), (565, 'Курганинск'), (566, 'Каневская'), (567, 'Усть-Лабинск'), (568, 'Кореновск'), (569, 'Апшеронск'), (570, 'Темрюк'), (571, 'Ленинградская'), (572, 'Абинск'), (573, 'Новокубанск'), (574, 'Динская'), (575, 'Гулькевичи'), (576, 'Горячий Ключ'), (577, 'Приморско-Ахтарск'), (578, 'Павловская'), (579, 'Староминская'), (580, 'Кущёвская'), (581, 'Полтавская'), (582, 'Тбилисская'), (583, 'Мостовской'), (584, 'Северская'), (585, 'Елизаветинская'), (586, 'Новотитаровская'), (587, 'Ильский'), (588, 'Отрадная'), (589, 'Хадыженск'), (590, 'Брюховецкая'), (591, 'Ахтырский'), (592, 'Холмская'), (593, 'Анапская'), (594, 'Гостагаевская'), (595, 'Витязево'), (596, 'Белая Глина'), (597, 'Выселки'), (598, 'Старомышастовская'), (599, 'Нововеличковская'), (600, 'Пластуновская'), (601, 'Васюринская'), (602, 'Кавказская'), (603, 'Казанская'), (604, 'Калининская'), (605, 'Старовеличковская'), (606, 'Стародеревянковская'), (607, 'Новоминская'), (608, 'Платнировская'), (609, 'Трудобеликовский'), (610, 'Марьянская'), (611, 'Новомышастовская'), (612, 'Ивановская'), (613, 'Старонижестеблиевская'), (614, 'Крыловская'), (615, 'Октябрьская'), (616, 'Варениковская'), (617, 'Киевское'), (618, 'Михайловская'), (619, 'Псебай'), (620, 'Новопокровская'), (621, 'Афипский'), (622, 'Петровская'), (623, 'Анастасиевская'), (624, 'Старотитаровская'), (625, 'Тамань'), (626, 'Медведовская'), (627, 'Новомихайловский'), (628, 'Успенское'), (629, 'Ладожская'), (630, 'Старощербиновская'), (631, 'Шарыпово'), (632, 'Сосновоборск'), (633, 'Дивногорск'), (634, 'Дудинка'), (635, 'Боготол'), (636, 'Берёзовка'), (637, 'Енисейск'), (638, 'Шушенское'), (639, 'Бородино'), (640, 'Кодинск'), (641, 'Иланский'), (642, 'Ужур'), (643, 'Богучаны'), (644, 'Емельяново'), (645, 'Курагино'), (646, 'Заозерный'), (647, 'Уяр'), (648, 'Чусовой'), (649, 'Добрянка'), (650, 'Чернушка'), (651, 'Кудымкар'), (652, 'Верещагино'), (653, 'Оса'), (654, 'Губаха'), (655, 'Нытва'), (656, 'Кизел'), (657, 'Красновишерск'), (658, 'Очёр'), (659, 'Александровск'), (660, 'Полазна'), (661, 'Горнозаводск'), (662, 'Яйва'), (663, 'Кондратово'), (664, 'Спасск-Дальний'), (665, 'Большой Камень'), (666, 'Партизанск'), (667, 'Лесозаводск'), (668, 'Дальнегорск'), (669, 'Дальнереченск'), (670, 'Фокино'), (671, 'Лучегорск'), (672, 'Трудовое'), (673, 'Кавалерово'), (674, 'Славянка'), (675, 'Черниговка'), (676, 'Чугуевка'), (677, 'Камень-Рыболов'), (678, 'Хороль'), (679, 'Покровка'), (680, 'Пограничный'), (681, 'Изобильный'), (682, 'Светлоград'), (683, 'Горячеводский'), (684, 'Зеленокумск'), (685, 'Благодарный'), (686, 'Иноземцево'), (687, 'Александровское'), (688, 'Новоалександровск'), (689, 'Новопавловск'), (690, 'Кочубеевское'), (691, 'Нефтекумск'), (692, 'Ипатово'), (693, 'Железноводск'), (694, 'Лермонтов'), (695, 'Ессентукская'), (696, 'Незлобная'), (697, 'Свободы'), (698, 'Краснокумское'), (699, 'Суворовская'), (700, 'Красногвардейское'), (701, 'Солнечнодольск'), (702, 'Зольская'), (703, 'Курская'), (704, 'Левокумское'), (705, 'Юца'), (706, 'Донское'), (707, 'Надежда'), (708, 'Курсавка'), (709, 'Дивное'), (710, 'Арзгир'), (711, 'Прасковея'), (712, 'Александрийская'), (713, 'Лысогорская'), (714, 'Амурск'), (715, 'Советская Гавань'), (716, 'Николаевск-на-Амуре'), (717, 'Бикин'), (718, 'Ванино'), (719, 'Вяземский'), (720, 'Солнечный'), (721, 'Чегдомын'), (722, 'Эльбан'), (723, 'Тында'), (724, 'Зея'), (725, 'Шимановск'), (726, 'Райчихинск'), (727, 'Завитинск'), (728, 'Прогресс'), (729, 'Магдагачи'), (730, 'Новодвинск'), (731, 'Коряжма'), (732, 'Мирный'), (733, 'Вельск'), (734, 'Няндома'), (735, 'Онега'), (736, 'Вычегодский'), (737, 'Коноша'), (738, 'Плесецк'), (739, 'Каргополь'), (740, 'Ахтубинск'), (741, 'Знаменск'), (742, 'Харабали'), (743, 'Камызяк'), (744, 'Красный Яр'), (745, 'Нариманов'), (746, 'Володарский'), (747, 'Икряное'), (748, 'Шебекино'), (749, 'Алексеевка'), (750, 'Валуйки'), (751, 'Строитель'), (752, 'Новый Оскол'), (753, 'Разумное'), (754, 'Чернянка'), (755, 'Борисовка'), (756, 'Волоконовка'), (757, 'Ровеньки'), (758, 'Ракитное'), (759, 'Северный'), (760, 'Новозыбков'), (761, 'Дятьково'), (762, 'Унеча'), (763, 'Стародуб'), (764, 'Карачев'), (765, 'Жуковка'), (766, 'Сельцо'), (767, 'Почеп'), (768, 'Навля'), (769, 'Трубчевск'), (770, 'Климово'), (771, 'Фокино'), (772, 'Клетня'), (773, 'Сураж'), (774, 'Кольчугино'), (775, 'Вязники'), (776, 'Киржач'), (777, 'Юрьев-Польский'), (778, 'Собинка'), (779, 'Радужный'), (780, 'Покров'), (781, 'Лакинск'), (782, 'Карабаново'), (783, 'Меленки'), (784, 'Петушки'), (785, 'Струнино'), (786, 'Гороховец'), (787, 'Камешково'), (788, 'Судогда'), (789, 'Урюпинск'), (790, 'Фролово'), (791, 'Калач-на-Дону'), (792, 'Котово'), (793, 'Городище'), (794, 'Котельниково'), (795, 'Суровикино'), (796, 'Новоаннинский'), (797, 'Жирновск'), (798, 'Краснослободск'), (799, 'Палласовка'), (800, 'Ленинск'), (801, 'Николаевск'), (802, 'Елань'), (803, 'Дубовка'), (804, 'Средняя Ахтуба'), (805, 'Петров Вал'), (806, 'Светлый Яр'), (807, 'Иловля'), (808, 'Сокол'), (809, 'Великий Устюг'), (810, 'Шексна'), (811, 'Грязовец'), (812, 'Бабаево'), (813, 'Кадуй'), (814, 'Вытегра'), (815, 'Острогожск'), (816, 'Нововоронеж'), (817, 'Новая Усмань'), (818, 'Семилуки'), (819, 'Бутурлиновка'), (820, 'Павловск'), (821, 'Бобров'), (822, 'Калач'), (823, 'Поворино'), (824, 'Анна'), (825, 'Грибановский'), (826, 'Таловая'), (827, 'Богучар'), (828, 'Кантемировка'), (829, 'Эртиль'), (830, 'Вичуга'), (831, 'Фурманов'), (832, 'Тейково'), (833, 'Кохма'), (834, 'Родники'), (835, 'Приволжск'), (836, 'Южа'), (837, 'Заволжск'), (838, 'Шелехов'), (839, 'Усть-Кут'), (840, 'Тулун'), (841, 'Саянск'), (842, 'Нижнеудинск'), (843, 'Тайшет'), (844, 'Зима'), (845, 'Железногорск-Илимский'), (846, 'Вихоревка'), (847, 'Слюдянка'), (848, 'Маркова'), (849, 'Чунский'), (850, 'Усть-Ордынский'), (851, 'Бодайбо'), (852, 'Свирск'), (853, 'Байкальск'), (854, 'Киренск'), (855, 'Советск'), (856, 'Черняховск'), (857, 'Балтийск'), (858, 'Гусев'), (859, 'Светлый'), (860, 'Гурьевск'), (861, 'Зеленоградск'), (862, 'Гвардейск'), (863, 'Светлогорск'), (864, 'Пионерский'), (865, 'Неман'), (866, 'Людиново'), (867, 'Киров'), (868, 'Малоярославец'), (869, 'Балабаново'), (870, 'Козельск'), (871, 'Кондрово'), (872, 'Сухиничи'), (873, 'Товарково'), (874, 'Жуков'), (875, 'Боровск'), (876, 'Сосенский'), (877, 'Кремёнки'), (878, 'Воротынск'), (879, 'Ермолино'), (880, 'Берёзовский'), (881, 'Осинники'), (882, 'Мыски'), (883, 'Мариинск'), (884, 'Топки'), (885, 'Полысаево'), (886, 'Тайга'), (887, 'Гурьевск'), (888, 'Таштагол'), (889, 'Калтан'), (890, 'Промышленная'), (891, 'Новый Городок'), (892, 'Яшкино'), (893, 'Бачатский'), (894, 'Грамотеино'), (895, 'Инской'), (896, 'Краснобродский'), (897, 'Яя'), (898, 'Тяжинский'), (899, 'Шерегеш'), (900, 'Слободской'), (901, 'Вятские Поляны'), (902, 'Котельнич'), (903, 'Омутнинск'), (904, 'Яранск'), (905, 'Советск'), (906, 'Сосновка'), (907, 'Зуевка'), (908, 'Белая Холуница'), (909, 'Луза'), (910, 'Буй'), (911, 'Шарья'), (912, 'Нерехта'), (913, 'Волгореченск'), (914, 'Галич'), (915, 'Мантурово'), (916, 'Ветлужский'), (917, 'Шумиха'), (918, 'Куртамыш'), (919, 'Далматово'), (920, 'Катайск'), (921, 'Петухово'), (922, 'Щучье'), (923, 'Курчатов'), (924, 'Льгов'), (925, 'Щигры'), (926, 'Рыльск'), (927, 'Обоянь'), (928, 'Кингисепп'), (929, 'Волхов'), (930, 'Тосно'), (931, 'Луга'), (932, 'Сланцы'), (933, 'Кировск'), (934, 'Отрадное'), (935, 'Пикалёво'), (936, 'Коммунар'), (937, 'Лодейное Поле'), (938, 'Никольское'), (939, 'Приозерск'), (940, 'Подпорожье'), (941, 'Бокситогорск'), (942, 'Светогорск'), (943, 'Шлиссельбург'), (944, 'Рощино'), (945, 'Сясьстрой'), (946, 'Сиверский'), (947, 'Вырица'), (948, 'Волосово'), (949, 'Ульяновка'), (950, 'Новое Девяткино'), (951, 'Посёлок имени Морозова'), (952, 'Мга'), (953, 'Ивангород'), (954, 'Грязи'), (955, 'Лебедянь'), (956, 'Данков'), (957, 'Усмань'), (958, 'Чаплыгин'), (959, 'Волоколамск'), (960, 'Белоозёрский'), (961, 'Яхрома'), (962, 'Некрасовский'), (963, 'Зарайск'), (964, 'Истра'), (965, 'Дедовск'), (966, 'Глебовский'), (967, 'Высоковск'), (968, 'Нахабино'), (969, 'Развилка'), (970, 'Луховицы'), (971, 'Томилино'), (972, 'Малаховка'), (973, 'Красково'), (974, 'Октябрьский'), (975, 'Можайск'), (976, 'Апрелевка'), (977, 'Калининец'), (978, 'Селятино'), (979, 'Старая Купавна'), (980, 'Электроугли'), (981, 'Обухово'), (982, 'Большие Вязёмы'), (983, 'Голицыно'), (984, 'Кубинка'), (985, 'Новый городок'), (986, 'Ликино-Дулёво'), (987, 'Куровское'), (988, 'Дрезна'), (989, 'Давыдово'), (990, 'Софрино'), (991, 'Правдинский'), (992, 'Быково'), (993, 'Ильинский'), (994, 'Удельная'), (995, 'Тучково'), (996, 'Руза'), (997, 'Хотьково'), (998, 'Пересвет'), (999, 'Краснозаводск'), (1000, 'Андреевка'), (1001, 'Михнево'), (1002, 'Талдом'), (1003, 'Запрудня'), (1004, 'Шатура'), (1005, 'Монино'), (1006, 'Фряново'), (1007, 'Бронницы'), (1008, 'Звенигород'), (1009, 'Кашира'), (1010, 'Котельники'), (1011, 'Красноармейск'), (1012, 'Лосино-Петровский'), (1013, 'Озёры'), (1014, 'Протвино'), (1015, 'Пущино'), (1016, 'Рошаль'), (1017, 'Черноголовка'), (1018, 'Шаховская'), (1019, 'Электрогорск'), (1020, 'Краснознаменск'), (1021, 'Власиха'), (1022, 'Североморск'), (1023, 'Мончегорск'), (1024, 'Кандалакша'), (1025, 'Кировск'), (1026, 'Оленегорск'), (1027, 'Ковдор'), (1028, 'Полярный'), (1029, 'Заполярный'), (1030, 'Полярные Зори'), (1031, 'Мурмаши'), (1032, 'Снежногорск'), (1033, 'Никель'), (1034, 'Гаджиево'), (1035, 'Балахна'), (1036, 'Заволжье'), (1037, 'Богородск'), (1038, 'Кулебаки'), (1039, 'Городец'), (1040, 'Семёнов'), (1041, 'Лысково'), (1042, 'Сергач'), (1043, 'Шахунья'), (1044, 'Навашино'), (1045, 'Лукоянов'), (1046, 'Первомайск'), (1047, 'Урень'), (1048, 'Чкаловск'), (1049, 'Ворсма'), (1050, 'Володарск'), (1051, 'Старая Русса'), (1052, 'Пестово'), (1053, 'Валдай'), (1054, 'Чудово'), (1055, 'Малая Вишера'), (1056, 'Окуловка'), (1057, 'Куйбышев'), (1058, 'Барабинск'), (1059, 'Обь'), (1060, 'Карасук'), (1061, 'Татарск'), (1062, 'Краснообск'), (1063, 'Тогучин'), (1064, 'Черепаново'), (1065, 'Линёво'), (1066, 'Коченёво'), (1067, 'Болотное'), (1068, 'Сузун'), (1069, 'Кольцово'), (1070, 'Купино'), (1071, 'Маслянино'), (1072, 'Колывань'), (1073, 'Чулым'), (1074, 'Криводановка'), (1075, 'Тара'), (1076, 'Исилькуль'), (1077, 'Калачинск'), (1078, 'Таврическое'), (1079, 'Называевск'), (1080, 'Черлак'), (1081, 'Тюкалинск'), (1082, 'Муромцево'), (1083, 'Большеречье'), (1084, 'Любинский'), (1085, 'Бугуруслан'), (1086, 'Гай'), (1087, 'Сорочинск'), (1088, 'Соль-Илецк'), (1089, 'Медногорск'), (1090, 'Кувандык'), (1091, 'Абдулино'), (1092, 'Саракташ'), (1093, 'Ясный'), (1094, 'Акбулак'), (1095, 'Тоцкое Второе'), (1096, 'Новоорск'), (1097, 'Илек'), (1098, 'Новосергиевка'), (1099, 'Ливны'), (1100, 'Мценск'), (1101, 'Знаменка'), (1102, 'Болхов'), (1103, 'Нарышкино'), (1104, 'Каменка'), (1105, 'Сердобск'), (1106, 'Никольск'), (1107, 'Нижний Ломов'), (1108, 'Мокшан'), (1109, 'Башмаково'), (1110, 'Бессоновка'), (1111, 'Остров'), (1112, 'Невель'), (1113, 'Опочка'), (1114, 'Печоры'), (1115, 'Донецк'), (1116, 'Аксай'), (1117, 'Белая Калитва'), (1118, 'Красный Сулин'), (1119, 'Миллерово'), (1120, 'Морозовск'), (1121, 'Зерноград'), (1122, 'Семикаракорск'), (1123, 'Зверево'), (1124, 'Пролетарск'), (1125, 'Орловский'), (1126, 'Зимовники'), (1127, 'Константиновск'), (1128, 'Егорлыкская'), (1129, 'Матвеев Курган'), (1130, 'Багаевская'), (1131, 'Чалтырь'), (1132, 'Кулешовка'), (1133, 'Самарское'), (1134, 'Покровское'), (1135, 'Обливская'), (1136, 'Персиановский'), (1137, 'Кривянская'), (1138, 'Каменоломни'), (1139, 'Песчанокопское'), (1140, 'Гигант'), (1141, 'Усть-Донецкий'), (1142, 'Целина'), (1143, 'Цимлянск'), (1144, 'Чертково'), (1145, 'Касимов'), (1146, 'Скопин'), (1147, 'Сасово'), (1148, 'Ряжск'), (1149, 'Рыбное'), (1150, 'Новомичуринск'), (1151, 'Шилово'), (1152, 'Кораблино'), (1153, 'Михайлов'), (1154, 'Отрадный'), (1155, 'Кинель'), (1156, 'Похвистнево'), (1157, 'Октябрьск'), (1158, 'Безенчук'), (1159, 'Нефтегорск'), (1160, 'Кинель-Черкассы'), (1161, 'Суходол'), (1162, 'Рощинский'), (1163, 'Усть-Кинельский'), (1164, 'Алексеевка'), (1165, 'Пугачёв'), (1166, 'Ртищево'), (1167, 'Приволжский'), (1168, 'Маркс'), (1169, 'Петровск'), (1170, 'Аткарск'), (1171, 'Красноармейск'), (1172, 'Ершов'), (1173, 'Новоузенск'), (1174, 'Калининск'), (1175, 'Красный Кут'), (1176, 'Хвалынск'), (1177, 'Степное'), (1178, 'Светлый'), (1179, 'Аркадак'), (1180, 'Корсаков'), (1181, 'Холмск'), (1182, 'Оха'), (1183, 'Поронайск'), (1184, 'Долинск'), (1185, 'Невельск'), (1186, 'Лесной'), (1187, 'Верхняя Салда'), (1188, 'Качканар'), (1189, 'Красноуфимск'), (1190, 'Алапаевск'), (1191, 'Реж'), (1192, 'Ирбит'), (1193, 'Сухой Лог'), (1194, 'Тавда'), (1195, 'Артёмовский'), (1196, 'Богданович'), (1197, 'Кушва'), (1198, 'Заречный'), (1199, 'Карпинск'), (1200, 'Североуральск'), (1201, 'Камышлов'), (1202, 'Невьянск'), (1203, 'Красноуральск'), (1204, 'Среднеуральск'), (1205, 'Сысерть'), (1206, 'Нижняя Тура'), (1207, 'Кировград'), (1208, 'Нижняя Салда'), (1209, 'Туринск'), (1210, 'Ивдель'), (1211, 'Рефтинский'), (1212, 'Талица'), (1213, 'Дегтярск'), (1214, 'Буланаш'), (1215, 'Троицкий'), (1216, 'Белоярский'), (1217, 'Арти'), (1218, 'Верхняя Синячиха'), (1219, 'Новая Ляля'), (1220, 'Пышма'), (1221, 'Арамиль'), (1222, 'Верхний Тагил'), (1223, 'Еланский'), (1224, 'Ярцево'), (1225, 'Сафоново'), (1226, 'Гагарин'), (1227, 'Десногорск'), (1228, 'Верхнеднепровский'), (1229, 'Дорогобуж'), (1230, 'Рассказово'), (1231, 'Моршанск'), (1232, 'Котовск'), (1233, 'Уварово'), (1234, 'Строитель'), (1235, 'Кирсанов'), (1236, 'Жердевка'), (1237, 'Первомайский'), (1238, 'Вышний Волочёк'), (1239, 'Торжок'), (1240, 'Кимры'), (1241, 'Конаково'), (1242, 'Удомля'), (1243, 'Бежецк'), (1244, 'Бологое'), (1245, 'Нелидово'), (1246, 'Осташков'), (1247, 'Кашин'), (1248, 'Калязин'), (1249, 'Торопец'), (1250, 'Лихославль'), (1251, 'Редкино'), (1252, 'Озёрный'), (1253, 'Стрежевой'), (1254, 'Асино'), (1255, 'Колпашево'), (1256, 'Ефремов'), (1257, 'Богородицк'), (1258, 'Кимовск'), (1259, 'Киреевск'), (1260, 'Суворов'), (1261, 'Ясногорск'), (1262, 'Плавск'), (1263, 'Венёв'), (1264, 'Белёв'), (1265, 'Заводоуковск'), (1266, 'Ялуторовск'), (1267, 'Голышманово'), (1268, 'Боровский'), (1269, 'Винзили'), (1270, 'Богандинский'), (1271, 'Новоульяновск'), (1272, 'Барыш'), (1273, 'Инза'), (1274, 'Новоспасское'), (1275, 'Ишеевка'), (1276, 'Чердаклы'), (1277, 'Снежинск'), (1278, 'Сатка'), (1279, 'Чебаркуль'), (1280, 'Кыштым'), (1281, 'Южноуральск'), (1282, 'Коркино'), (1283, 'Трёхгорный'), (1284, 'Аша'), (1285, 'Еманжелинск'), (1286, 'Верхний Уфалей'), (1287, 'Карталы'), (1288, 'Усть-Катав'), (1289, 'Бакал'), (1290, 'Куса'), (1291, 'Пласт'), (1292, 'Катав-Ивановск'), (1293, 'Касли'), (1294, 'Сим'), (1295, 'Роза'), (1296, 'Красногорский'), (1297, 'Юрюзань'), (1298, 'Карабаш'), (1299, 'Нязепетровск'), (1300, 'Первомайский'), (1301, 'Аргаяш'), (1302, 'Переславль-Залесский'), (1303, 'Тутаев'), (1304, 'Углич'), (1305, 'Ростов'), (1306, 'Гаврилов-Ям'), (1307, 'Данилов'), (1308, 'Нарьян-Мар'), (1309, 'Мегион'), (1310, 'Радужный'), (1311, 'Лангепас'), (1312, 'Пыть-Ях'), (1313, 'Урай'), (1314, 'Лянтор'), (1315, 'Югорск'), (1316, 'Советский'), (1317, 'Пойковский'), (1318, 'Фёдоровский'), (1319, 'Белоярский'), (1320, 'Излучинск'), (1321, 'Покачи'), (1322, 'Белый Яр'), (1323, 'Нижнесортымский'), (1324, 'Междуреченский'), (1325, 'Солнечный'), (1326, 'Анадырь'), (1327, 'Салехард'), (1328, 'Надым'), (1329, 'Муравленко'), (1330, 'Лабытнанги'), (1331, 'Губкинский'), (1332, 'Тарко-Сале'), (1333, 'Пангоды'), (1334, 'Уренгой')]