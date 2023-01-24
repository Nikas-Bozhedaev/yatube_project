from django.http import HttpResponse

# Main Page
def index(request):
    return HttpResponse('Добро пожаловать в новую социальную сеть!')

def group_posts(request, slug):
    return HttpResponse(f'Здесь будет любая группа {slug}')
