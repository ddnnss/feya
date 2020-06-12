from .models import LeftMenuItem, RightMenuItem

def side_menus(request):
    leftMenu = LeftMenuItem.objects.filter(is_active=True)
    rightMenu = RightMenuItem.objects.filter(is_active=True)
    print(rightMenu)
    return locals()

