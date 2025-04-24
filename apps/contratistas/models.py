from django.db import models


class ContractorCompany(models.Model):
    name = models.CharField(max_length=150)
    nit = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    contact_person = models.CharField(max_length=100, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Si quieres varios contactos por empresa:
class ContractorContact(models.Model):
    contractor = models.ForeignKey(ContractorCompany, on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    position = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.name} ({self.contractor.name})"
