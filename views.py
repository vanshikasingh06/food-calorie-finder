from django.shortcuts import render

#LGnZi5q50pW+CeJSmeEv3A==fctu1FF9ysONEpML
#LGnZi5q50pW+CeJSmeEv3A==ObdakzgWjPKwek60
#new api key
# Create your views here.
def home(request):
    import json
    import requests
   
        
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
        api_request = requests.get(
            api_url + query, headers={'X-Api-Key': 'LGnZi5q50pW+CeJSmeEv3A==ObdakzgWjPKwek60'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! There was an error"
            print(e)
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'query': 'Enter a valid query'})