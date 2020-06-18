from .models import LeftMenuItem, RightMenuItem,TopMenuItem

def side_menus(request):
    leftMenu = LeftMenuItem.objects.filter(is_active=True)
    rightMenu = RightMenuItem.objects.filter(is_active=True)
    topMenu = TopMenuItem.objects.all()

    return locals()

