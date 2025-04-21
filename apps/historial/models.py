from django.db import models
from apps.vinculaciones.models import EmploymentLink
from apps.usuarios.models import User  # quien hizo el cambio

class WorkHistory(models.Model):
    employment_link = models.ForeignKey(EmploymentLink, on_delete=models.CASCADE)
    modified_field = models.CharField(max_length=50)
    old_value = models.TextField(blank=True, null=True)
    new_value = models.TextField()
    change_date = models.DateTimeField(auto_now_add=True)
    changed_by = models.ForeignKey(User, on_delete=models.RESTRICT)

    class Meta:
        db_table = 'work_history'

    def __str__(self):
        return f"{self.modified_field} - {self.change_date}"
