from django.http import HttpResponse
from django.shortcuts import RequestContext
from django.template import loader
import json

from DirectoryService.models import servicelist
# Create your views here.
def generateOutput(request,page,data):
    template = loader.get_template(page)
    context =  RequestContext(request, data)
    return template.render(context)

def register(request,json_msg):
    j_obj=json.loads(json_msg)
    entries = servicelist.objects.filter(pk=j_obj["key"])
    if len(entries) > 0:
        entries[0].name = j_obj["name"]
        entries[0].port = j_obj["port"]
        entries[0].version = j_obj["version"]
        entries[0].address = j_obj["address"]
        entries[0].save()
        return HttpResponse(generateOutput(request,"jsons/registration.json",{"data_key":entries[0].pk,"data_status":"Update"}))
    else:
        s =servicelist(name=j_obj["name"],port=j_obj["port"],version=j_obj["version"],address=j_obj["address"])
        s.save()
        return HttpResponse(generateOutput(request,"jsons/registration.json",{"data_key":s.pk,"data_status":"Registered"}))

def deregister(request,json_msg):
    j_obj=json.loads(json_msg)
    entries = servicelist.objects.filter(pk=j_obj["key"])
    if len(entries) > 0:
        entries[0].delete()
        return HttpResponse(generateOutput(request,"jsons/result.json",{"op_result":"Deregistered"}))
    return HttpResponse(generateOutput(request,"jsons/result.json",{"op_result":"Failed Deregister"}))

def listservices(request):
    services_list = servicelist.objects.all()
    #print "services_list %s"%services_list
    return HttpResponse(generateOutput(request,"jsons/service_list.json",{"list":services_list}))

def getservice(request,json_msg):
    j_obj=json.loads(json_msg)
    entries = servicelist.objects.filter(pk=j_obj["key"])
    if len(entries) > 0:
        return HttpResponse(generateOutput(request,"jsons/service_item.json",{"item":entries[0]}))
    return HttpResponse(generateOutput(request,"jsons/result.json",{"op_result":"Failed to Get Sevice Invalid key"}))


