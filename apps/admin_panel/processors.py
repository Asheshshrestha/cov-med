from apps.admin_panel.models import WebsiteSettingModel

def web_credential(request):
    context = {
        'website':WebsiteSettingModel.objects.first()
    }
    return context