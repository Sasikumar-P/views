from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View
from ttt.forms import DemoForm, Demo1Form,Demo2Form
from ttt.models import Demo,Demo1,Demo2
from django.views.generic import FormView
def home(request):
	return render(request, 'home.html')
def function_based_view(request):
    """
    Function based views take a request and are very explicit in the actions.
    They have more code in some regards, but they go step by step in execution.
    """
    form = DemoForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('function')
        else:
            return HttpResponse('Error!')

    context = {'form': form}

    return render(request, 'my_template.html', context)



class ClassBasedView(View):
    """
    Class Based Views allow you to explicitly state your HTTP methods such as
    GET and POST. If a method is not specified then it a request of that type
    will be served a 405 error.
    """
    def get(self, request):
        form = DemoForm(None)
        context = {'form': form}
        return render(request, 'my_template1.html', context)

    def post(self, request):
        form = DemoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('cbv')

        return HttpResponse('Error!')

class ClassBasedGenericView(FormView):
    """
    Class Based Generic Views allow you to use a typical pattern and write
    minimal code as Django will handle the boilerplate for you behind the
    scenes.
    """
    template_name = 'my_template2.html'
    form_class = DemoForm
    success_url = '/cbgv/'

    def form_valid(self, form):
        form.save()
        return super(ClassBasedGenericView, self).form_valid(self)

    def form_invalid(self, form):
        return HttpResponse('Error!')
