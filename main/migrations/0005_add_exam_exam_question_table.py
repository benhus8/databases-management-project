# Generated by Django 4.2.6 on 2023-10-30 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_add_table_course'),
        ('main', '0002_add_user_tables'),
        ('main', '0003_add_asset_table'),
        ('main', '0004_add_exam_tables')
    ]

    operations = [
        migrations.RunSQL(
            'CREATE TABLE IF NOT EXISTS main_exam_exam_question('
            'exam_exam_question_id  INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,'
            'exam_id  INTEGER NOT NULL,'
            'exam_question_id  INTEGER NOT NULL,'
            'CONSTRAINT fk_exam FOREIGN KEY (exam_id) REFERENCES main_exam(exam_id),'
            'CONSTRAINT fk_exam_question FOREIGN KEY (exam_question_id) REFERENCES main_exam_question(exam_question_id)'
            ');'
        )
    ]
