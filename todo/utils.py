menu = [{'title': 'Главная страница', 'url_name': 'index'},
        {'title': 'Добавить задачу', 'url_name': 'addtask'},
        ]


class DataMixin:
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context
