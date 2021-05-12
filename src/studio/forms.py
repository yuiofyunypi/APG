
from django.forms import Form,ModelForm
from models import Studio


# link_ios = models.CharField('link to IOS',max_length=400, blank=True)
    # link_gp = models.CharField('link to Google',max_length=400, blank=True)
    # link_face = models.CharField('link to Facebook page',max_length=400, blank=True)
    # link_twit = models.CharField('link to Twitter Page',max_length=400, blank=True)
    # email = models.CharField('contact us email', max_length=100, blank=True)
    # policy = models.TextField(verbose_name='private policy', blank=True)
    # ga_key = models.CharField('Google Analytics Key', max_length=300, blank=True)
    # fea_app = models.TextField(verbose_name='Featured App', blank=True)

class StudioForm(ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'
    class Meta:
        model = Studio
        fields = ['logo','dsp','link_ios','link_gp','link_face','link_twit','email','policy','ga_key','fea_app']
    