import imp


from apps.admin_panel.models import WebsiteSettingModel

def get_logo(request):
    site_logo = WebsiteSettingModel.objects.first().logo_image.url
    return {'site_logo':site_logo}