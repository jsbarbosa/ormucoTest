from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import FormForm

def viewForm(request):
    if request.method == 'POST':
        form = FormForm(request.POST)
        success = form.is_valid()
        # data = form.cleaned_data
        data = form.cleaned_data
        if success:
            # pass
            form.save() # save to db
        else:
            data['name'] = form.data['name']
        fields = dict({'form': form, 'success': success}, **data)
        return render(request, 'sent.html', fields)
    else:
        form = FormForm()
    return render(request, 'form.html', {'form': form})
