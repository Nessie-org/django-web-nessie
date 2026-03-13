from django.shortcuts import HttpResponse
from django.views.decorators.http import require_POST
from myapp.platform import platform
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def home(request , **kwargs):
    return HttpResponse(platform.index())

@csrf_exempt
@require_POST
def perform_action(request):
    #print("Received POST request with body:", request.body)
    action_data = dict(json.loads(request.body))
    print("Received action data:", action_data)
    print("Name:" , action_data.get("Action Name"))
    print("Payload:" , action_data.get("payload"))
    print("Plugin:" , action_data.get("Plugin Name"))
    result = platform.perform_action(action_data.get("Action Name"), action_data.get("payload"), action_data.get("Plugin Name") or None)

    return HttpResponse(result)

def get_plugins(request):
    request_action_name = request.GET.get("Action Name")
    print("Received request for plugins with Action Name:", request_action_name)
    plugins = platform.get_plugins(request_action_name)
    print("Returning plugins:", plugins)
    JSON_plugins = [plugin.to_dict() for plugin in plugins]
    return JsonResponse(JSON_plugins, safe=False)


