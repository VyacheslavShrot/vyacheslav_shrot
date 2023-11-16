from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"
    http_method_names = ["get"]


class AboutView(TemplateView):
    template_name = "about.html"
    http_method_names = ["get"]


class ExperienceView(TemplateView):
    template_name = "exp.html"
    http_method_names = ["get"]


class EducationView(TemplateView):
    template_name = "education.html"
    http_method_names = ["get"]


class SkillsView(TemplateView):
    template_name = "skills.html"
    http_method_names = ["get"]


class ProjectsView(TemplateView):
    template_name = "projects.html"
    http_method_names = ["get"]
