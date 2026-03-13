from django.shortcuts import HttpResponse
from django.views.decorators.http import require_POST
from myapp.platform import platform
from django.http import HttpResponseServerError, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.defaults import server_error, bad_request
import json

def home(request , **kwargs):
    try:
        return HttpResponse(platform.index())
    except Exception as e:
        print("Error in home view:", str(e))
        return server_error("An error occurred while processing the request.")
@csrf_exempt
@require_POST
def perform_action(request):
    try:
        #print("Received POST request with body:", request.body)
        action_data = dict(json.loads(request.body))
        #print("Received action data:", action_data)
        #print("Name:" , action_data.get("Action Name"))
        #print("Payload:" , action_data.get("payload"))
        #print("Plugin:" , action_data.get("Plugin Name"))
        result = platform.perform_action(action_data.get("Action Name"), action_data.get("payload"), action_data.get("Plugin Name") or None)
        return HttpResponse(result)
    except json.JSONDecodeError:
        return bad_request("Invalid JSON")
    except Exception:
        return server_error("An error occurred while processing the request.")



def get_plugins(request):
    try:
        request_action_name = request.GET.get("Action Name")
        print("Received request for plugins with Action Name:", request_action_name)
        plugins = platform.get_plugins(request_action_name)
        print("Returning plugins:", plugins)
        JSON_plugins = [plugin.to_dict() for plugin in plugins]
        return JsonResponse(JSON_plugins, safe=False)
    except Exception as e:
        print("Error in get_plugins:", str(e))
        return JsonResponse({"error": "An error occurred while fetching plugins."}, status=500)


