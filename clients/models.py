from django.contrib.auth.models import User
from django.db import models
from teams.models import Team
LOW = 'low'
MEDIUM = 'medium'
HIGH = 'high'

CHOICES_PRIORITY = (
    (LOW, 'Low'),
    (MEDIUM, 'Medium'),
    (HIGH, 'High'),
)

plot = 'plot'
readyTomove = 'readyToMove'
apartment = 'apartment'

Property_type = (
    (plot, 'plot'),
    (readyTomove, 'readyTomove'),
    (apartment, 'apartment'),
)
class Client(models.Model):
    team = models.ForeignKey(Team, related_name='clients', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=11, default=' ')
    Address = models.TextField(max_length=50, default=' ',blank=False,null=False)
    property_price = models.IntegerField(default='00')
    property_size = models.CharField(max_length=25,default=' ')
    property_locality = models.CharField(max_length=25, default=' ')
    property_type = models.CharField(max_length=11, choices=Property_type, default=plot)
    converted_to_client = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=CHOICES_PRIORITY, default=MEDIUM)
    created_by = models.ForeignKey(User, related_name='clients', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name



