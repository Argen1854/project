from django.forms import forms
from . import kavano
from app import models
from django import forms


class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('KAVANO', 'KAVANO'),
        ('MANGA', 'MANGA'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]

    def parse_data(self):
        if self.data['media_type'] == 'KAVANO':
            kavano_parser = kavano.parser()
            for i in kavano_parser:
                models.Product.objects.create(**i)
        # elif self.data['media_type'] == 'MANGA':
        #     manga_parser = parser_manga.parser()
        #     for i in manga_parser:
        #         models.Manga.objects.create(**i)

        