# city_functions.py

def city_country(city, country, population=None, language=None):
    """Return a formatted city string with optional population and language."""
    result = f"{city.title()}, {country.title()}"

    if population is not None:
        result += f" - population {population}"

    if language is not None:
        result += f", {language.title()}"

    return result


if __name__ == "__main__":
    # City, Country only
    print(city_country("santiago", "chile"))

    # City, Country, Population
    print(city_country("paris", "france", 2148000))

    # City, Country, Population, Language
    print(city_country("tokyo", "japan", 13960000, "japanese"))
