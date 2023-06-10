from django.urls import path,include
from .views import *

urlpatterns = [
    path('',main,name="main"),
    path('assamese/',home_assamese, name="as-home"),
    path('bodo/',home, name="bodo-home"),
    path('add_metadata/',add_metadata, name="add_metadata"),
    path('add_sentences/',add_sentences, name="add_sentences"),
    
    path('assamese/raw_sentences/',assamese_raw_sentences, name="assamese-raw-sentences"),
    path('bodo/raw_sentences/',bodo_raw_sentences, name="bodo-raw-sentences"),

    path('assamese/edit_raw_sentences/<int:id>/',edit_assamese_raw_sentences, name="edit-assamese-raw-sentences"),
    path('bodo/edit_raw_sentences/<int:id>/',edit_bodo_raw_sentences, name="edit-bodo-raw-sentences"),
    path('assamese/view_raw_sentences/<int:id>/',view_assamese_raw_sentences, name="view-assamese-raw-sentences"),
    path('bodo/view_raw_sentences/<int:id>/',view_bodo_raw_sentences, name="view-bodo-raw-sentences"),

    path('assamese/tagged_sentences/',assamese_tagged_sentences, name="assamese-tagged-sentences"),
    path('bodo/tagged_sentences/',bodo_tagged_sentences, name="bodo-tagged-sentences"),

    path('assamese/tagged_sentences_user/',tagged_assamese_user, name="tagged-assamese-user"),
    path('bodo/tagged_sentences_user/',tagged_bodo_user, name="tagged-bodo-user"),

    path('assamese/tagged_sentences_admin/',tagged_assamese_admin, name="tagged-assamese-admin"),
    path('bodo/tagged_sentences_admin/',tagged_bodo_admin, name="tagged-bodo-admin"),

    path('assamese/edit_tagged_sentences/<int:id>/',edit_tagged_assamese_sentences, name="edit-tagged-assamese-sentences"),
    path('bodo/edit_tagged_sentences/<int:id>/',edit_tagged_bodo_sentences, name="edit-tagged-bodo-sentences"),
    
    path('assamese/view_tagged_sentences/<int:id>/',view_assamese_tagged_sentences, name="view-tagged-assamese-sentences"),
    path('bodo/view_tagged_sentences/<int:id>/',view_bodo_tagged_sentences, name="view-tagged-bodo-sentences"),

    path('assamese/verified_sentences/',list_verified_assamese_sentences, name="verified-assamese-sentences"),
    path('bodo/verified_sentences/',list_verified_bodo_sentences, name="verified-bodo-sentences"),
    
    path('export_to_csv/',export_to_csv,name="export-to-csv"),
    path('export_to_text/',export_to_text,name="export-to-text"),
    path('download_text_file/',batch_text_download,name="download-text-file"),
]