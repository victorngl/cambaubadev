# Generated by Django 3.1.7 on 2021-04-20 16:40

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('materiais_didaticos', '0004_materialdidatico_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunicado',
            name='descricao',
            field=django_quill.fields.QuillField(blank=True, null=True, verbose_name='Descrição'),
        ),
    ]
