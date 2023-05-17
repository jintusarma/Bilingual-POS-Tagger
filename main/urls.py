from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home, name="home"),
    path('add_sentences/',add_sentences, name="add_sentences"),
    path('sentences/',raw_sentences, name="raw-sentences"),
    path('edit_sentences/<int:id>/',edit_raw_sentences, name="edit-raw-sentences"),
    path('view_sentences/<int:id>/',view_raw_sentences, name="view-raw-sentences"),
    path('tagged_sentences/',tagged_sentences, name="tagged-sentences"),
    path('tagged_sentences_user/',tagged_user, name="tagged-user"),
    path('tagged_sentences_admin/',tagged_admin, name="tagged-admin"),
    path('edit_tagged_sentences/<int:id>/',edit_tagged_sentences, name="edit-tagged-sentences"),
    path('view_tagged_sentences/<int:id>/',view_tagged_sentences, name="view-tagged-sentences"),
    path('verified_sentences/',list_verified_sentences, name="verified-sentences"),
    path('export_to_csv/',export_to_csv,name="export-to-csv"),
    path('export_to_text/',export_to_text,name="export-to-text"),
]