from django.shortcuts import render
import requests
API_KEY = '8eb8932ad2c04014af5a86de87ba6795'
def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')
    api_link = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'
    if country:
        api_link = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
    if category:
        api_link = f'https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={API_KEY}'
    response = requests.get(api_link)
    data = response.json()
    articles = data['articles']
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)
