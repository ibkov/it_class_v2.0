from django.urls import path, include

from . import views
from .views import PostDetailView, AddEventView, WorksView, ApplicantListView


urlpatterns = [
    path("", views.MainView.as_view()),
    path("rate/", views.PuplesView.as_view()),
    path("check_list/", views.CheckList.as_view(), name="check_list"),
    path("documents_to_10_class/", views.PhotoGalleryView.as_view(), name="photo_gallery"),
    path("<int:pk>/", PostDetailView.as_view(), name="puples"),
    path('<int:pk>/img-change/', views.ImgChangeView.as_view(), name='img_change'),
    path("<int:pk>/add_events", AddEventView.as_view(), name="add_event"),
    path("works/", WorksView.as_view(), name="works"),
    path("download/", views.verificationFileDownload, name="verification_file_download"),
    path("account/", views.account, name="puples"),
    path("intensiv/", views.IntensivView.as_view(), name="intensiv"),
    path("test_applicant/", views.ApplicantView.as_view(), name="applicant"),
    path("hacaton/", views.HacatonView.as_view()),
    path("applicant_list/", ApplicantListView.as_view(), name="applicant_list"),
    path("login/success/", views.account, name="applicant_list"),
    path("summer_practice/", views.SummerPracticeView.as_view(), name="summer_practice"),
    path("summer_practice/admin", views.SummerPracticeAdminView.as_view(), name="summer_practice_admin"),
    path("notifications/", views.NotificationsView.as_view(), name="summer_practice_admin"),
    path("check_class_v1/", views.CheckClassv1.as_view(), name="check_class_v1"),
    path("check_list_v1/", views.CheckListv1.as_view(), name="check_list_v1"),
    path("it_week2021/", views.ItWeek2021.as_view(), name="it_week2021"),
    path("market/", include('market.urls')),
    path("daytask/", include('daytask.urls')),
    path("test_ib/", views.test, name="test_ib"),

]
