from django.urls import path,include
from .views import *

urlpatterns = [
    path('',main,name="main"),
    path('assamese/',home_assamese, name="as-home"),
    path('bodo/',home, name="bodo-home"),
    path('add_metadata/',add_metadata, name="add_metadata"),
    path('add_sentences/',add_sentences, name="add_sentences"),
    
    path('assamese_sentences/',assamese_raw_sentences, name="assamese-raw-sentences"),
    path('bodo_sentences/',bodo_raw_sentences, name="bodo-raw-sentences"),

    path('edit_assamese_sentences/<int:id>/',edit_assamese_raw_sentences, name="edit-assamese-raw-sentences"),
    path('edit_bodo_sentences/<int:id>/',edit_bodo_raw_sentences, name="edit-bodo-raw-sentences"),
    path('view_assamese_sentences/<int:id>/',view_assamese_raw_sentences, name="view-assamese-raw-sentences"),
    path('view_bodo_sentences/<int:id>/',view_bodo_raw_sentences, name="view-bodo-raw-sentences"),

    path('assamese_tagged_sentences/',assamese_tagged_sentences, name="assamese-tagged-sentences"),
    path('bodo_tagged_sentences/',bodo_tagged_sentences, name="bodo-tagged-sentences"),

    path('tagged_sentences_assamese_user/',tagged_assamese_user, name="tagged-assamese-user"),
    path('tagged_sentences_bodo_user/',tagged_bodo_user, name="tagged-bodo-user"),

    path('tagged_sentences_assamese_admin/',tagged_assamese_admin, name="tagged-assamese-admin"),
    path('tagged_sentences_bodo_admin/',tagged_bodo_admin, name="tagged-bodo-admin"),

    path('edit_tagged_assamese_sentences/<int:id>/',edit_tagged_assamese_sentences, name="edit-tagged-assamese-sentences"),
    path('edit_tagged_bodo_sentences/<int:id>/',edit_tagged_bodo_sentences, name="edit-tagged-bodo-sentences"),
    
    path('view_tagged_assamese_sentences/<int:id>/',view_assamese_tagged_sentences, name="view-tagged-assamese-sentences"),
    path('view_tagged_bodo_sentences/<int:id>/',view_bodo_tagged_sentences, name="view-tagged-bodo-sentences"),

    path('verified_assamese_sentences/',list_verified_assamese_sentences, name="verified-assamese-sentences"),
    path('verified_bodo_sentences/',list_verified_bodo_sentences, name="verified-bodo-sentences"),
    
    path('export_to_csv/',export_to_csv,name="export-to-csv"),
    path('export_to_text/',export_to_text,name="export-to-text"),
    path('download_text_file/',batch_text_download,name="download-text-file"),
]