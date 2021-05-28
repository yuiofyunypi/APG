from forms import StudioForm
from common.db_tools import from_dict
from models import Studio

def get_globals():
    return globals()


def add_studio(name):
    Studio.objects.create(name=name)
    return {'status':'ok'}


def save_studio(studio):
    form=StudioForm(studio)
    if form.is_valid():
        studio.update(form.cleaned_data )
        obj=from_dict(studio)
        obj.save()
        return {'status':'success'}
    else:
        return {'errors':form.errors}