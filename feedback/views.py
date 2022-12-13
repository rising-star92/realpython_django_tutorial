from django.shortcuts import render
from feedback.forms import FeedbackForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

# Create your views here.
class FeedbackFormView(FormView):
    template_name = "feedback/feedback.html"
    form_class = FeedbackForm
    success_url = "/feedback/success/"

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

class SuccessView(TemplateView):
    template_name = "feedback/success.html"