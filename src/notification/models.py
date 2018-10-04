from django.db import models
from django.utils import timezone

# Create your models here.

TAG_CHOICE = (
    (0, 'Erro'),
    (1, 'Aviso'),
    (2, 'Recomendação')
)

class Notification(models.Model):
    title = models.CharField("Título", max_length=45)
    message = models.TextField("Mensagem", max_length=155)
    author = models.CharField("Autor", max_length=100)
    tag = models.IntegerField("Categoria", choices=TAG_CHOICE)
    time_active = models.IntegerField("Tempo ativa", default=15)
    creation_date = models.DateTimeField("Data de Criação", editable=False, default=timezone.now().isoformat())
    send_date = models.DateTimeField("Data de Envio", null=True, blank=True)

    class Meta:
        verbose_name = "Notificação"
        verbose_name_plural = "Notificações"

    def __str__(self):
        return self.title
