import imp


from apps.admin_panel.models import WebsiteSettingModel

def get_logo(request):
    site_data = WebsiteSettingModel.objects.first()
    site_logo = site_data.logo_image.url
    site_copyright = site_data.copyright
    return {'site_logo':site_logo,'copy_right':site_copyright}