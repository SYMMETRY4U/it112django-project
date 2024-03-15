from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# views.py
from django.http import JsonResponse
from .default_data import load_default_data
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Invention
from django.views.generic import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Invention, Category
from .forms import InventionForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request):
  return HttpResponse("<h1>Hello Django!</h1>")

def about(request):
  return HttpResponse("<h1>About Page</h1>")

def function_view(request):
    context = {
        'page_title': 'Function-Based View',
        'page_heading': 'Welcome to the Function-Based View',
        'page_content': 'This is the content generated by the function-based view which we will be moving away from.',
    }
    return render(request, 'bootswatch.html', context)

#class from which all class based views inherit
class BaseView(TemplateView):
    default_title = 'My Website'
    default_image = 'images/django-logo.png'  # Default image path
    default_alt_text = 'Django' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.setdefault('title', self.default_title)
        context['page_image'] = self.default_image
        return context

class ClassView(BaseView):
  template_name = 'bootswatch.html'
  default_image = 'images/django2.png'  # Specific image
  default_alt_text = 'Django Class View' 

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context.update({
          'title': 'Class-Based View',
          'page_heading': 'Welcome to the Class-Based View',
          'page_content': 'This is the content generated by the class-based view.',
          'page_image': self.default_image,
          'default_alt_text': self.default_alt_text,
      })
      return context
      
class ThemeView(BaseView):
  template_name = 'theme.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      # Add additional context data if needed
      return context

  def post(self, request, *args, **kwargs):
      theme = request.POST.get('theme')
      response = HttpResponseRedirect(reverse('theme'))
      response.set_cookie('theme', theme)
      return response

class AboutView(BaseView):
    template_name = 'bootswatch.html'
    default_image = 'images/django2.png'
    default_alt_text = 'About Django' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'About View',
            'page_heading': 'Welcome to my About Page',
            'page_content': 'This is the content generated by the class-based view.',
            'page_image': self.default_image,
            'default_alt_text': self.default_alt_text,
        })
        return context


class HomeView(BaseView):
  template_name = 'bootswatch.html'
  default_alt_text = 'About Django' 
  
  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context.update({
          'title': 'Home View',
          'page_heading': 'Welcome to the Future Home Page',
          'page_content': 'This is the content generated by the class-based view.',
          'page_image': self.default_image,
          'default_alt_text': self.default_alt_text,
      })
      return context

class FunctionView(BaseView):
  template_name = 'bootswatch.html'
  default_image = 'images/1974-yz125.png'  # Specific image
  default_alt_text = 'My 1974 YZ' 

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context.update({
          'title': 'Function View',
          'page_heading': 'Welcome to the Future Home Page',
          'page_content': 'This is the content generated by the class-based view. We have moved away from the function view',
          'page_image': self.default_image,
          'default_alt_text': self.default_alt_text,
      })
      return context

class Cr250View(BaseView):
    template_name = 'bootswatch.html'
    default_image = 'images/mycr250.png'  # Specific image
    default_alt_text = '1991 CR250'  # Alt text for the image

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'CR 250',
            'page_heading': 'The 1991 Honda CR250 Motocross Bike',
            'page_content': 'This is the content generated by the class-based view.',
            'page_image': self.default_image,
            'default_alt_text': self.default_alt_text,
        })
        return context


class NoguchiView(BaseView):
  template_name = 'bootswatch.html'
  default_image = 'images/noguchi-125.png'  # Specific image
  default_alt_text = 'Noguchi 125' 

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context.update({
          'title': 'Noguchi 125',
          'page_heading': 'Japans Best Yamaha Custom Modifications',
          'page_content': 'This is the content generated by the class-based view.',
          'page_image': self.default_image,
          'default_alt_text': self.default_alt_text,
      })
      return context

class Yz125View(BaseView):
  template_name = 'bootswatch.html'
  default_image = 'images/1974-yz125.png'  # Specific image
  default_alt_text = 'YZ 125' 

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context.update({
          'title': 'YZ 125',
          'page_heading': 'Yamaha YZ 125',
          'page_content': 'This is the content generated by the class-based view.',
          'page_image': self.default_image,
          'default_alt_text': self.default_alt_text,
      })
      return context
class MotocrossView(BaseView):
  template_name = 'bootswatch.html'
  default_image = 'images/pi-motocross.png'  # Specific image
  default_alt_text = 'Friends' 

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context.update({
          'title': 'PI Motocross',
          'page_heading': '2006 Bauang Motocross Champs',
          'page_content': 'This is the content generated by the class-based view.',
          'page_image': self.default_image,
          'default_alt_text': self.default_alt_text,
      })
      return context

def load_default_data_view(request):
    load_default_data()  # Call the load_default_data function
    return JsonResponse({'status': 'success'})

class InventionListView(ListView):
    model = Invention
    template_name = 'invention_list.html'
    context_object_name = 'inventions'

class InventionDetailView(DetailView):
    model = Invention
    template_name = 'invention_view.html'
    context_object_name = 'invention'
# this is to require login        
class InventionCreateView(LoginRequiredMixin, CreateView):
    model = Invention
    form_class = InventionForm
    template_name = 'create_invention.html'
    success_url = reverse_lazy('invention-list')

class InventionUpdateView(LoginRequiredMixin, UpdateView):
    model = Invention
    form_class = InventionForm
    template_name = 'update_invention.html'
    success_url = reverse_lazy('invention-list')

class InventionDeleteView(LoginRequiredMixin, DeleteView):
  model = Invention
  success_url = reverse_lazy('invention-list')
