# Generated by Django 4.2.6 on 2023-10-05 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=50)),
                ('titulo', models.CharField(max_length=100)),
                ('editora', models.CharField(max_length=50)),
                ('anoPublicacao', models.IntegerField()),
                ('numeroPagina', models.PositiveIntegerField()),
            ],
        ),
    ]
