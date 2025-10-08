from matplotlib import pyplot as plt

years = [2006, 2007, 2008, 2009, 2010, 2011, 2012,
         2013, 2014, 2015, 2016, 2017, 2018, 2019,
         2020, 2021, 2022, 2023, 2024, 2025,]

freedom_house_total = [35, 34, 32, 31, 27, 27, 28,
                       27, 26, 23, 22, 20, 20, 20,
                       20, 20, 19, 16, 13, 12]


# Настройка стиля и размера графика
plt.figure(figsize=(14, 8))
plt.style.use('seaborn-v0_8')

# Построение графика
plt.plot(years, freedom_house_total, marker='o', linestyle='-',
         linewidth=2, markersize=6, color='#2E86AB', label='Общий балл Freedom House')

# Настройка внешнего вида
plt.title('Динамика общего балла Freedom House по годам', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Год', fontsize=12)
plt.ylabel('Общий балл Freedom House', fontsize=12)

# Настройка осей
plt.xticks(years, rotation=45)
plt.ylim(10, 40)
plt.grid(True, alpha=0.3)

# Добавление аннотаций для ключевых точек
for i, (year, value) in enumerate(zip(years, freedom_house_total)):
    if i % 3 == 0 or i == len(years)-1:  # Аннотируем каждую 3-ю точку и последнюю
        plt.annotate(f'{value}', (year, value),
                    textcoords="offset points",
                    xytext=(0,10),
                    ha='center',
                    fontsize=9)

# Легенда
plt.legend(fontsize=12)

# Улучшение компоновки
plt.tight_layout()

# Показать график
plt.show()

# Дополнительно: столбчатая диаграмма
plt.figure(figsize=(14, 8))
bars = plt.bar(years, freedom_house_total, color='#A23B72', alpha=0.7, edgecolor='black')

# Добавление значений на столбцы
for bar, value in zip(bars, freedom_house_total):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
             str(value), ha='center', va='bottom', fontsize=9)

plt.title('Динамика общего балла Freedom House по годам (столбчатая диаграмма)',
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Год', fontsize=12)
plt.ylabel('Общий балл Freedom House', fontsize=12)
plt.xticks(years, rotation=45)
plt.ylim(0, 40)
plt.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.show()