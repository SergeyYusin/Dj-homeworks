from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv

def index(request):
    return redirect(reverse('bus_stations'))


def f_csv():
    csv_list = []

    with open('dj-homeworks/1.2-requests-templates/pagination/data-398-2018-08-30.csv', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] != 'Name' or row[4] != 'Street' or row[6] != 'District':
                csv_list.append({
                    'Name': row[1],
                    'Street': row[4],
                    'District': row[6]
                })

    return csv_list


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    content = f_csv()
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(content, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
