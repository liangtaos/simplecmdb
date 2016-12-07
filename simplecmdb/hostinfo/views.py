from django.shortcuts import render
from hostinfo.models import Host, HostGroup
from django.http import HttpResponse
import json
from django.template import loader, Context
# Create your views here.

def homepage(reqest):
    t = loader.get_template('index.html')
    c = Context({})
    return HttpResponse(t.render(c))

def collect(req):
    if req.POST:
        hostname = req.POST.get('hostname')
        ip = req.POST.get('ip')
        osver = req.POST.get('osver')
        vendor = req.POST.get('vendor')
        product = req.POST.get('product')
        cpu_model = req.POST.get('cpu_model')
        cpu_num = req.POST.get('cpu_num')
        memory = req.POST.get('memory')
        sn = req.POST.get('sn')
        try:
            host = Host.objects.get(ip=ip)
        except:
            host = Host()
        
        host.hostname = hostname
        host.ip = ip
        host.osver = osver
        host.product = product
        host.cpu_model = cpu_model
        host.cpu_num = cpu_num
        host.memory = memory
        host.sn = sn
        host.vendor = vendor
        host.save()
        return HttpResponse('post ok')
    #else:
    #    return HttpResponse('not data')
    elif req.GET:
        hostname = req.GET.get('hostname')
        ip = req.GET.get('ip')
        osver = req.GET.get('osver')
        vendor = req.GET.get('vendor')
        product = req.GET.get('product')
        cpu_model = req.GET.get('cpu_model')
        cpu_num = req.GET.get('cpu_num')
        memory = req.GET.get('memory')
        sn = req.GET.get('sn')

        host = Host()
        host.hostname = hostname
        host.ip = ip
        host.osver = osver
        host.product = product
        host.cpu_model = cpu_model
        host.cpu_num = cpu_num
        host.memory = memory
        host.sn = sn
        host.vendor = vendor
        host.save()
        return HttpResponse('get ok')
    else:
        return HttpResponse('not data')    




def getjson(req):
    #if req.GET:
    #    hostname = req.GET.get('hostname')
    #    ip = req.GET.get('ip')
    #    groupname = req.GET.get('groupname')
    ret_list = []
    hg = HostGroup.objects.all()
    for g in hg:
        ret = {'groupname':g.groupname,'members':[]}
        for h in g.member.all():
            ret_h = {'hostname':h.hostname,'ip':h.ip}
            ret['members'].append(ret_h)
        ret_list.append(ret)
    
    return HttpResponse(json.dumps(ret_list))
    
    #return HttpResponse(json.dumps(re))
    #hn = Host.objects.all()
    #print hostname,'*' * 50
    #for i in hn:
    #    out = {}
    #    ho = i.ip
    #    if ip == ho:
    #        out['ip'] = i.ip
    #        out['cpu_model'] = i.cpu_model
    #        out['cpu_num'] = i.cpu_num
    #        out['memory'] = i.memory
    #        out['sn'] = i.sn
    #        out['hostname'] = i.hostname
    #        out['osver'] = i.osver
    #        break
    #print out
    #out = [out]
    #return HttpResponse(json.dumps(out))




def gettxt(req):
    res = ''
    hg = HostGroup.objects.all()
    for g in hg:
        groupname = g.groupname
        for h in g.member.all():
            hostname = h.hostname
            ip = h.ip
            res += groupname+' '+hostname+' '+ip+'\n'
    return HttpResponse(res)
