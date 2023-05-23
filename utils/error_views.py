
from django.http import JsonResponse

def error_404(request, exception):
    message = 'Page not found'
    
    response = JsonResponse(data={ 'error': '500', 'message': message }, status=404) 
    return response
    
def handler500(request):
    message = 'Internal server error'
    
    response = JsonResponse(data={ 'error': '500', 'message': message }, status=500) 
    return response