from django.http import HttpResponse


def errors_index(request):
    division_by_zero = 345435 / 0
    # thisis an error
    
    return HttpResponse({'division':division_by_zero})
    # return render(request, 'index.html', {'division': 0})