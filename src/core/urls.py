from django.urls import path

from core.views import IndexView, AboutView, ExperienceView, EducationView, SkillsView, ProjectsView

app_name = "core"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("about/", AboutView.as_view(), name="about"),
    path("experience/", ExperienceView.as_view(), name="experience"),
    path("education/", EducationView.as_view(), name="education"),
    path("skills/", SkillsView.as_view(), name="skills"),
    path("projects/", ProjectsView.as_view(), name="projects"),
]
