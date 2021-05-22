
from django.forms import Form,ModelForm,ValidationError
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
    
    
    def clean_email(self):
        email= self.cleaned_data.get('email')
        if not email:
            raise ValidationError('Need Email')
        else:
            return email
    
    
    def clean_link_gp(self):
        link_gp= self.cleaned_data.get('link_gp')
        if not link_gp:
            raise ValidationError('Need link_gp')
        else:
            return link_gp 
    
    def clean_link_face(self):
        link_face= self.cleaned_data.get('link_face')
        if not link_face:
            raise ValidationError('Need link_face')
        else:
            return link_face     
    