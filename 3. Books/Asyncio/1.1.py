import requests

response = requests.get('https://www.example.com')

items = response.headers.items()

headers = [f'{key}: {header}' for key, header in items]

formatted_headers = '\n'.join(headers)

print(items, '\n')
print(headers, '\n')
print(formatted_headers)