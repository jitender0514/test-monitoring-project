from django.views.generic.base import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from .models import Links
import urllib3, json
import certifi


def check_link(request):
    ids = request.GET.get("notSync", None)
    links = Links.objects.filter(user=request.user).exclude(id=ids)
    for link in links:
        try:
            http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
            r = http.request('GET', link.link)
            link.status = r.status
            link.save()
        except Exception as e:
            return JsonResponse({"msg": "Unable to fetch :" + link.link}, status=400)
    return JsonResponse({"data": list(links.values("id", "link", "status"))}, status=200)


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'links/dashboard.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        links = Links.objects.filter(user = user)
        context['links'] = json.dumps(list(links.values("id", "link", "status")))
        return context

