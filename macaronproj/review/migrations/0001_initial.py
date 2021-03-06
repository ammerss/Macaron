
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('writer', models.CharField(default='', max_length=100)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.TextField(help_text='Title of review', max_length=50, primary_key=True, serialize=False)),
                ('content', models.TextField(help_text='Content of review', max_length=500)),
                ('rate', models.DecimalField(decimal_places=1, default=Decimal('0'), max_digits=10)),
                ('hit', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['-post_date'],
            },
        ),
    ]
