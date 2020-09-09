# Формируем массив с данными для таблицы [момент, номер шага, m, n, текст]
my_table = []

# Шаг 1
m = int(input())
n = int(input())

moment = 1
my_table.append([moment, 1, m, n, "Взяли " + str(m) + " и " + str(n) + ", обозначили их m и n; перешли к шагу 2"])

# Шаг 2
while m!=n:
	# Шаг 3
	moment += 1
	my_table.append([moment, 2, m, n, "Сравнили " + str(m) + " != " + str(n) + "; перешли к шагу 3"])

	if m > n:
		moment += 1
		m_dop = m - n
		my_table.append([moment, 3, m_dop, n, str(m) + " > " + str(n) + "; переобозначили через m разность " + str(m) + "-" + str(n) + "; перешли к шагу 2"])
		m = m_dop
	else:
		moment += 1
		n_dop = n - m
		my_table.append([moment, 3, m, n_dop, str(n) + " > " + str(m) + "; переобозначили через n разность " + str(n) + "-" + str(m) + "; перешли к шагу 2"])
		n = n_dop

moment += 1
my_table.append([moment, 2, m, n, "Сравнили " + str(m) + " == " + str(n) + "; остановились"])

table_text = ["Момент врем.", "Номер шага", "Значен. m", "Знач. n", "Действие исполнителя"]

# Максимальная ширина колонок, чтобы таблица корректно отображалась
table_width = []

# Получаем ширину заголовков
for u in table_text:
	table_width.append(len(u))

# Находим максимульную ширину для каждого столбца
for line in my_table:
	for num in range(len(table_text)):
		if(len(str(line[num])) > table_width[num]):
			table_width[num] = len(str(line[num]))

# Разделители
vert_split = "|"
horiz_split = "—"
split = "+"

# Шапка таблицы
h_line = split
h_text = vert_split
i = 0
for ss in table_text:
	h_line += (table_width[i]*horiz_split)
	h_text += ss
	# Добавить нужное количество пробелов
	cvv = table_width[i] - len(str(ss))
	if(cvv > 0):
		h_text += " " * cvv
	h_text += vert_split
	h_line += split
	i += 1
print(h_line)
print(h_text)
print(h_line)

# Тело таблицы
for i in my_table:
	line_txt = vert_split
	horizontal_line = split
	indx = 0
	for ny in i:
		line_txt += str(ny)
		# Добавить нужное количество пробелов
		uu = table_width[indx] - len(str(ny))
		if(uu > 0):
			line_txt += " " * uu
		line_txt += vert_split
		horizontal_line += (table_width[indx]*horiz_split) + split
		indx += 1

	print(line_txt)
	print(horizontal_line)

