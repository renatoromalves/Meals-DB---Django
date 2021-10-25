import requests, json



class Request_meals():

    def __init__(self):
        self._url = 'https://www.themealdb.com/api/json/v1/1/search.php?s='
        self.request = requests.get(self._url)
        if self.request.status_code == 200:
            self.request = self.request.json()['meals']
        else:
            self.request = False


    def search(self, search_key:str):
        self._url = 'https://www.themealdb.com/api/json/v1/1/search.php?s='
        self.search_list = requests.get(self._url+search_key)
        self.search_key = search_key
        if self.search_list.status_code == 200:
            self.search_list = self.search_list.json()['meals']
        else:
            self.search_list = False


