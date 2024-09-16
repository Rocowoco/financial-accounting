from django.views.generic import TemplateView

class CategoryListView(TemplateView):
    template_name = 'categories/category_list.html'

class CategoryCreateView(TemplateView):
    template_name = 'categories/category_form.html'

class CategoryUpdateView(TemplateView):
    template_name = 'categories/category_form.html'

class CategoryDeleteView(TemplateView):
    template_name = 'categories/category_confirm_delete.html'
