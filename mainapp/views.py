from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Some title'
        return context_data


class NewsView(TemplateView):
    template_name = 'mainapp/news.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # context_data['title'] = 'Новость раз'
        context_data['object_list'] = [
            {
                'title': 'Новость раз',
                'preview': 'Превью к новости раз',
                'date': '2022-01-01',
            }, {
                'title': 'Новость два',
                'preview': 'Превью к новости два',
                'date': '2022-01-01',
            }, {
                'title': 'Новость три',
                'preview': 'Превью к новости три',
                'date': '2022-01-01',
            }, {
                'title': 'Новость 4',
                'preview': 'Превью к новости 4',
                'date': '2022-01-01',
            }, {
                'title': 'Новость 6',
                'preview': 'Превью к новости 5',
                'date': '2022-01-01',
            }, {
                'title': 'Новость 7',
                'preview': 'Превью к новости 7',
                'date': '2022-01-01',
            },
        ]
        # context_data['preview'] = 'Превью к новости раз'
        # context_data['date'] = '2022-01-01'
        return context_data

class DocSiteView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class CoursesListView(TemplateView):
    template_name = 'mainapp/courses_list.html'


class LoginView(TemplateView):
    template_name = 'mainapp/login.html'


class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'

