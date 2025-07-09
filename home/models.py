from django.db import models
from django.core.validators import EmailValidator, RegexValidator

class Contact(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Full Name")
    email = models.EmailField(
        max_length=122,
        validators=[EmailValidator()],
        verbose_name="Email Address"
    )
    phone = models.CharField(
        max_length=20,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$')],
        blank=True,
        null=True,
        verbose_name="Phone Number"
    )
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(verbose_name="Your Message")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new'
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Request"
        verbose_name_plural = "Contact Requests"

    def __str__(self):
        return f"{self.name} - {self.subject or 'No Subject'}"