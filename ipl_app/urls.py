from django.urls import path
from ipl_app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('', views.teamdisplay, name="teamdisplay"),
    path('create_team', views.teamInsert, name="teamInsert"),
    path('edit/<int:id>', views.teamedit, name="teamedit"),
    path('update/<int:id>', views.teamupdate, name="teamupdate"),
    path('delete/<int:id>', views.teamdel, name="teamdel"),
    path('detail/<int:id>', views.teamdetails, name="teamdetails"),

    path('add_player', views.add_player, name="add_player"),
    path('detail/playerdetail/<int:id>', views.playerdetails, name="playerdetails"),
    path('search', views.search, name="search"),
    
]+ static(settings.LOGO_URL, document_root=settings.LOGO_ROOT) + \
static(settings.PLAYER_URL, document_root=settings.PLAYER_ROOT)