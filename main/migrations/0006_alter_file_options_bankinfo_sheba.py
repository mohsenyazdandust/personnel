# Generated by Django 5.0 on 2023-12-13 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_bankinfo_file'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='file',
            options={'ordering': ['-uploaded_at']},
        ),
        migrations.AddField(
            model_name='bankinfo',
            name='sheba',
            field=models.CharField(default='0', max_length=100),
            preserve_default=False,
        ),
    ]
