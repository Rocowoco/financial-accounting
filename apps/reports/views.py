from django.views.generic import TemplateView

class ReportListView(TemplateView):
    template_name = 'reports/report_list.html'

class ReportDetailView(TemplateView):
    template_name = 'reports/report_detail.html'
