from django.views.generic import TemplateView

class BudgetListView(TemplateView):
    template_name = 'budgets/budget_list.html'

class BudgetCreateView(TemplateView):
    template_name = 'budgets/budget_form.html'

class BudgetUpdateView(TemplateView):
    template_name = 'budgets/budget_form.html'

class BudgetDeleteView(TemplateView):
    template_name = 'budgets/budget_confirm_delete.html'
