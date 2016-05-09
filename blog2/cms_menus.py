#from menus.base import Menu, NavigationNode
from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu

#class BlogMenu(Menu):
class PostMenu(CMSAttachMenu):
 
    #Menu Name (shows in dropdown)
       name = _("post menu")

       def get_nodes(self, request):
        nodes = []
        n1 = NavigationNode(_('Test1'), "/newpost1/", 4)
        n2 = NavigationNode(_('Test2'), "/newpost2/", 5)
        n3 = NavigationNode(_('Test3'), "/newpost3/", 6)
        nodes.append(n1)
        nodes.append(n2)
        nodes.append(n3)

        return nodes

#menu_pool.register_menu(BlogMenu)
menu_pool.register_menu(PostMenu)
