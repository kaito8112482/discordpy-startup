import urllib.request

def download():
    url = 'https://services9.arcgis.com/XenOZPW9k4gDSO12/arcgis/rest/services/COVID19_JapanCaseData/FeatureServer/0/query?where=%E9%80%9A%E3%81%97%3E-1&returnIdsOnly=false&returnCountOnly=false&&f=pgeojson&outFields=*&orderByFields=%E9%80%9A%E3%81%97'
    title = 'COVID-19_data.json'
    urllib.request.urlretrieve(url, "{0}".format(title))
