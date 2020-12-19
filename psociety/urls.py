''' P-Society Urls '''

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from users import views as users_views
from questions import views as questions_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',questions_views.list_questions, name="q_feed"),
    path('new_question/', questions_views.new_question, name='new_question'),
    path('question/<int:id>', questions_views.question_detail, name='question_detail'),

    # Users views
    path('login/', users_views.login_view, name='login' ),
    path('singup/', users_views.sing_up_view, name='singup' ),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
