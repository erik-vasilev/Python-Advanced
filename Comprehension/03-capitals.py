country_names = input().split(', ')
country_capitals = input().split(', ')
zipped_countries = zip(country_names, country_capitals)

result = {k: v for k, v in zipped_countries}
print('\n'.join([f'{country} -> {city}' for country, city in result.items()]))
