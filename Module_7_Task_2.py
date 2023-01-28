import csv

films = []      #Список, в який завантажується вся фільмотека

class film_base:
    def __init__(self,
                type: str,
                name: str,
                year: int,
                genre: str,
                number_of_views: int,
                season: int,
                series: int                
               ):
        self.type = type
        self.name = name
        self.year = year
        self.genre = genre
        self.number_of_views = number_of_views        
        self.season = season
        self.series = series
    
    def __str__(self):
        return f' {self.year} {self.name} \t Genre: {self.genre}.  Views: {self.number_of_views}'

    #Збільшення кількості переглядів на 1
    def increasing_number_of_views(self):
        self.number_of_views += 1          

    #Виводить список фільмів
    def get_movies():
        print("List of movies")
        list_by_name = sorted(films, key=lambda film: film.name)  #Сортування фільмів за назвою
        for film in list_by_name:
            if (film.type == 'f'):
                print(film) 
    
    #Виводить список серіалів
    def get_series():
        print("List of series")
        list_by_name = sorted(films, key=lambda film: film.name)  #Сортування серіалів за назвою
        for film in list_by_name:
            if (film.type == 's'):
                print(film)

    #Пошук фільму чи серіалу за назвою
    def search():
        movie_name = input("Enter the name of the movie or series to search: ")
        for film in films:
            if movie_name == film.name:
                print(film)

    #Збереження фільмотеки у файл films.csv
    def save_films_to_csv():
        with open('films.csv', 'w', newline='') as csvfile:
            fieldnames = ['type', 'name', 'year', 'genre', 'number_of_views', 'season', 'series']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for film in films:
                writer.writerow({'type': film.type,
                                'name': film.name,
                                'year': film.year, 
                                'genre': film.genre, 
                                'number_of_views': film.number_of_views,
                                'season': film.season, 
                                'series': film.series})

    #Завантаження фільмотеки з файлу films.csv
    def load_films_from_csv():
        with open('films.csv', newline='') as csvfile:            
            reader = csv.DictReader(csvfile)
            for row in reader:
                films.append(film_base(type = row['type'],
                                        name = row['name'],
                                        year = int(row['year']),
                                        genre = row['genre'],
                                        number_of_views = int(row['number_of_views']),
                                        season = int(row['season']),
                                        series = int(row['series'])
                                        ))

    #Перегляд фільму або серіалу
    def play_film():
        name_of_film = input("Enter the name of the movie or series to watch: ")
        for film in films:
            if name_of_film == film.name:
                if (film.type == 'f'):
                    print(f'Now watching a movie {film.name} \n Year: {film.year} \n Genre: {film.genre}')
                    film_base.increasing_number_of_views(film)
                    print(f'Finished watching the movie {film.name} ({film.year})')
                elif (film.type == 's'):
                    print(f'Now watching the series {film.name} \n Year: {film.year} \n Genre: {film.genre}')
                    print(f' Season: {film.season}\n Series: {film.series}')
                    film_base.increasing_number_of_views(film)
                    print(f'Finished watching the series {film.name} S{film.season}E{film.series}')

command_string = ""
film_base.load_films_from_csv()     #Завантаження файлу при запуску програми
print("\n ---=== Film Library ===---\n")
while command_string != 'exit':
    command_string = input("What would you like to do? (Enter ""help"" to get a list of commands): ")
    if command_string in ('exit', 'help', 'show', 'load', 'save', 'play', 'find'):
        if command_string == 'exit':
            film_base.save_films_to_csv()   #Збереження у файл при завершені програми
            print("Exiting... Bye!")
        if command_string == 'help':
            print("\nAvalaible commands:\nhelp - this help\nexit - stop running a programm" + 
                  "\nshow - show a list of available movies and series" +
                  "\nplay - watching a movie or series\nfind - find a movie or series by title\n")
        if command_string == 'show':
            show_command_string = input(" What would you like to display (f - movies, s - series)?: ")
            if (show_command_string == 'f'):
                film_base.get_movies()
            elif (show_command_string == 's'):
                film_base.get_series()
        if command_string == 'play':
            film_base.play_film()
        if command_string == 'find':
            film_base.search()
