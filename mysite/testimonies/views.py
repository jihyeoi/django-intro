from django.shortcuts import render
from testimonies.models import Testimonials
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.
def show_testimonials(request):
    testimonies = Testimonials.objects.all().order_by('id')
    return render(request, 'testimonies/testimonials.html', {'testimonies': testimonies})


def post_new(request):

    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('show_testimonials')

    else:
        form = PostForm()

    return render(request, 'testimonies/post_form.html', {'form': form})