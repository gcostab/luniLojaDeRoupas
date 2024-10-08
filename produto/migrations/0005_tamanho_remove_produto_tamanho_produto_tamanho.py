# Generated by Django 5.0.6 on 2024-08-27 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_alter_tipoproduto_nome'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tamanho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tamanho', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='produto',
            name='tamanho',
        ),
        migrations.AddField(
            model_name='produto',
            name='tamanho',
            field=models.ManyToManyField(related_name='produto', to='produto.tamanho'),
        ),
    ]
