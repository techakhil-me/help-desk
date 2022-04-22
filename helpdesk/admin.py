from django.contrib import admin
from helpdesk.models import Ticket
# Register your models here.


class TicketAdmin(admin.ModelAdmin):
     list_display = ( 'subject',
    'author',
    'description',
    'date',
    'priority',
    'status',
    'category')

    
admin.site.register(Ticket, TicketAdmin)