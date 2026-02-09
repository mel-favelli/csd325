def city_country(city, country, population=None, language=None):
    
    base = f"{city.title()}, {country.title()}"

    if population is not None:
       base = f"{base} - population {population}"

    if language is not None:
        base = f"{base} - {language.title()}"

    return base


print(city_country("santiago", "chile",))
print(city_country("bangkok", "thailand", 11000000))
print(city_country("tokyo", "japan", 37000000, "japanese"))

