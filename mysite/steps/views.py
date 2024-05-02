from django.shortcuts import render
from steps.models import Step


def main_page(request):
    return render(request, 'steps/main_page.html', {})


def list_steps(request):
    steps = Step.objects.prefetch_related('directions').order_by('id')
    return render(request, 'steps/getting_started.html', {'steps': steps})