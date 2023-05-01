from import_export import resources
from .models import jobpost

class jobpostResource(resources.ModelResource):
        class meta:
            model = jobpost