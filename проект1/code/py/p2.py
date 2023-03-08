import requests
from bs4 import BeautifulSoup





# parse opencve.io---------------------------------------------------------------------------------------------------- 
def parsing_opencve():
    url1 = 'https://www.opencve.io/login/'
    url2 = 'https://www.opencve.io/login'
    csrf_token = ''
    s = requests.Session()
    response = s.get(url1)
    soup = BeautifulSoup(response.text, 'lxml')

    # Get CSRF
    for a in soup.find_all('meta'):
        if 'name' in a.attrs:
            if a.attrs['name'] == 'csrf-token':
                csrf_token = a.attrs['content']



# parsgo Uname
# 1478963258Pg  passW
#
    # Authentication
    s.post(
        url2,
        data={
            'username': USERNAME,
            'password': PASSWORD,
            'csrf_token': csrf_token,
        },
        headers={'referer': 'https://www.opencve.io/login'},
        verify=False
    )
    # Get new CVE
    cve_line = []
    for page_num in range(1, 20):
        pagination = f'https://www.opencve.io/?page={page_num}'
        resp = s.get(pagination)
        parse = BeautifulSoup(resp.text, 'lxml')
        for cve in parse.find_all('h3', class_='timeline-header'):
            index = cve.text.find('has changed')
            if index == -1:
                cve_line.append(cve.text.replace(' is a new CVE', ''))

    cve_line_no_replic = []
    for item in cve_line:
        if item not in cve_line_no_replic:
            cve_line_no_replic.append(item[:-1])
    return cve_line_no_replic

cve_line = parsing_opencve()  # Получение списка новых cve с сайта opencve.io
print(cve_line)