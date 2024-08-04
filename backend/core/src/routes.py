from django.urls import include, path

routes = [
    path("api/memo/", include("src.memos.urls")),
    path("", include("src.pages.urls")),
]
