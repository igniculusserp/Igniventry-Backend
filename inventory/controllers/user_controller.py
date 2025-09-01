from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from ..services.user_service import create_user_service

@csrf_exempt
def insert_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            result = create_user_service(data)
            if result:
                return JsonResponse({"status": "success", "message": "User inserted"})
            else:
                return JsonResponse({"status": "error", "message": "DB not connected"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
    else:
        return JsonResponse({"status": "error", "message": "Only POST allowed"})