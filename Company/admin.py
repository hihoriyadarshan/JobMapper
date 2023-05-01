from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from Company.models import jobpost

@admin.register(jobpost)
class jobpostAdmin(ImportExportActionModelAdmin):
    list_display = ('companyname','job_title','salary','experience_required','jobtype','skill_required','education_level','last_date','job_description')

# Register your models here.
