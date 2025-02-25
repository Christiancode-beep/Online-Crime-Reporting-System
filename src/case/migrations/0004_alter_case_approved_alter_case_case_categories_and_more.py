# Generated by Django 4.0.5 on 2022-06-18 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('citizen', '0001_initial'),
        ('police', '0002_alter_contact_ward_alter_criminal_ward_and_more'),
        ('case', '0003_case_ward_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='approved',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='case_categories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='case.casecategory'),
        ),
        migrations.AlterField(
            model_name='case',
            name='cyber_case_categories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='case.cybercasecategories'),
        ),
        migrations.AlterField(
            model_name='case',
            name='solved',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='userid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='citizen.citizen'),
        ),
        migrations.AlterField(
            model_name='case',
            name='ward_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='police.ward'),
        ),
        migrations.AlterField(
            model_name='evidence',
            name='case',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='case.case'),
        ),
        migrations.AlterField(
            model_name='witness',
            name='case',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='case.case'),
        ),
    ]
