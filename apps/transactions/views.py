from django.shortcuts import render
from django.views.generic import TemplateView

class TransactionListView(TemplateView):
    template_name = 'transactions/transaction_list.html'

class TransactionCreateView(TemplateView):
    template_name = 'transactions/transaction_form.html'

class TransactionUpdateView(TemplateView):
    template_name = 'transactions/transaction_form.html'

class TransactionDeleteView(TemplateView):
    template_name = 'transactions/transaction_confirm_delete.html'
