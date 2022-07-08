
from mainapp.models import PostPortfolio
from mainapp.models import Opcion, Blog

def get_opcion(request):
    pages = Opcion.objects.all().values_list('title','slug')
    return {
        'pages': pages
    }

def get_portfolio(request):
    projects = PostPortfolio.objects.all().values_list('title', 'text','languajes','framework','project_date','image')
    return {
        'projects': projects
    }

def get_blog(request):
    blog = Blog.objects.all().values_list('title','description','image','created_at','updated_at')
    return {
        'blog': blog
    }
