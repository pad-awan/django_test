from django.urls import path
from .views import (
            LeadCreateView, lead_update, lead_delete,lead_list,lead_create,
            LeadListView,LeadDetailView,LeadUpdateView,LeadDeleteView
            )

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name="lead-list"),
    path('<int:pk>/', LeadDetailView.as_view(), name="lead-detail"),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name="lead-update"),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name="lead-delete"),
    path('create/', LeadCreateView.as_view(), name="lead-create"),
]