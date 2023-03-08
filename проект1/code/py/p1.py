import requests
from bs4 import BeautifulSoup
import os
import time
import re
import json
import PyPDF2

#from pathlib import Path

#from PyPDF2 import PdfFileReader, PdfFileWriter
#import pypdf2 as PyPDF2

# from django.urls import path #as PATH
#from django.urls  django-url-framework
#from django.urls import include, path

# parse bulletine NKCKI------------------------------------------------------------------------------------------------
def get_cve_list(name_list):
    cve_list = []
    cve_list_repeat = []
    for name in name_list:
        pdf_file = open(f'{PATH}/{name}', 'rb')
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        number_of_pages = read_pdf.getNumPages()
        data = ''
        for i in range(number_of_pages):
            page = read_pdf.getPage(i)
            page_content = page.extractText()
            data1 = json.dumps(page_content)
            data += data1

        rez = ''
        for n, item in enumerate(data, start=0):
            if item != '\\':
                rez += data[n]

        result = ''
        for n, item in enumerate(rez, start=0):
            if item != 'n':
                result += rez[n]
        rez1 = result.replace(" ", "")

        regex = re.findall(r'CVE-\d{4}-\d{4,8}', rez1)
        for cve in regex:
            cve_list_repeat.append(cve)
    for item in cve_list_repeat:
        if item not in cve_list:
            cve_list.append(item)
    return cve_list


def get_links_for_bulletine():
    links = []
    for page in range(3):
        r = requests.get("https://safe-surf.ru/specialists/bulletins-nkcki/?PAGEN_1={}".format(page))
        soup = BeautifulSoup(r.text, "html.parser")
        for vuln in soup.find_all("div", "blockBase blockBulletine"):
            bulletin_pdf_url = "https://safe-surf.ru{}".format(vuln.find('h4').find('a')['href'])
            links.append(bulletin_pdf_url)
    return links


def create_pdf_file(links):
    for str in links:
        get = requests.get(str)
        name = str.replace("https://safe-surf.ru/upload/VULN/", "")
        check_file = os.path.exists(f'{PATH}/{name}')
        if check_file == 0:
            with open(f'{PATH}/{name}', 'wb') as f:
                f.write(get.content)
        else:
            print(f'file {name} already exists')


def get_name_list(path):
    name_list = os.listdir(path)
    return name_list


def remove_pdf_file(path):
    for item in path:
        os.remove(item)

links = get_links_for_bulletine()
create_pdf_file(links)

#PATH #D:\Pars 


name_list = get_name_list(PATH) # Получение имен скаченных файлов для парсинга
cve_line = get_cve_list(name_list)  # Получение списка cve из биллютеня НКЦКИ
print(cve_line)

# remove pdf buffer--------------------------------------------------------------------------------------------------- 
time.sleep(1)
path_to_remove_pdf = []
for item in name_list:
    path_to_remove_pdf.append(f'{PATH}/{item}')
remove_pdf_file(path_to_remove_pdf)