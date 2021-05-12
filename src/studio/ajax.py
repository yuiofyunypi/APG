from forms import StudioForm
from common.db_tools import from_dict
def get_globals():
    return globals()


def add_studio(name):
    return {'status':'ok'}


def save_studio(studio):
    form=StudioForm(studio)
    if form.is_valid():
        studio.update(form.cleaned_data )
        obj=from_dict(studio)
        obj.save()
        return {'status':'success'}