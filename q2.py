from django.db import models
import django


class Hit(models.Model):

    PAGEVIEW = 'PV'
    DOWNLOAD = 'DL'
    ACTIONS = (
        (PAGEVIEW, 'Article web page view'),
        (DOWNLOAD, 'Article download'),
    )

    publication = models.ForeignKey('Publication', on_delete=models.CASCADE, related_name='hits')
    date = models.DateTimeField(default=django.utils.timezone.now)
    ip_address = models.GenericIPAddressField()
    user_agent = models.ForeignKey('UserAgent', on_delete=models.SET_NULL,
                                   null=True, blank=True)
    action = models.CharField(max_length=2, choices=ACTIONS)


class Publication(models.Model):

    title = models.CharField(max_length=200)
    journal = models.ForeignKey('Journal', on_delete=models.CASCADE)
    # ... remaining fields omitted


def get_journal_statistics():
    # Construct summary dict in the form {journal_id -> (total_views, total_downloads)}
    statistics = {}
    publications = Publication.objects.all()
    for publication in publications:
        total_views = publication.hits.filter(action=Hit.PAGEVIEW).count()
        total_downloads = publication.hits.filter(action=Hit.DOWNLOAD).count()
        statistics[publication.pk] = (total_views, total_downloads)
    return statistics

