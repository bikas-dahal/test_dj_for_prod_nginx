from django.core.management.base import BaseCommand
from myapp.models import Feature
from faker import Faker


class Command(BaseCommand):
    help = 'Add initial features to the database'
    def handle(self, *args, **kwargs):
        fake = Faker()
        features = []

        for i in range(1, 8):  # Creates 7 feature entries
            feature = Feature(
                name=fake.word(),
                title=fake.sentence(nb_words=3),
                details=fake.paragraph(nb_sentences=4, variable_nb_sentences=False)
            )
            features.append(feature)

        Feature.objects.bulk_create(features)
        self.stdout.write(self.style.SUCCESS('Successfully added initial features'))
