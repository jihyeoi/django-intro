from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

from .models import Testimonials

class PostForm(forms.ModelForm):

    class Meta:
        model = Testimonials
        fields = ('name', 'testimonial',)

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.fields['name'].label = '*name'
        self.fields['testimonial'].label = '*your Django thoughts'

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
