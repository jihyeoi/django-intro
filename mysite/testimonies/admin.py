from django.contrib import admin
from .models import Testimonials


class TestimonialForm(admin.ModelAdmin):
    fields = ['name', 'testimonial']


admin.site.register(Testimonials, TestimonialForm)