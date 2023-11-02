# Generated by Django 4.2.6 on 2023-10-29 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_add_table_course'),
        ('main', '0002_add_user_tables'),
        ('main', '0003_add_asset_table')
    ]

    operations = [
        migrations.RunSQL(
            'CREATE TABLE IF NOT EXISTS main_exam ('
            'exam_id  INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,'
            'score  INTEGER NOT NULL,'
            'max_score  INTEGER NOT NULL,'
            'passed  BOOLEAN NOT NULL DEFAULT FALSE);'

            'CREATE TABLE IF NOT EXISTS main_user_exam('
            'user_exam_id  INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,'
            'exam_id  INTEGER NOT NULL,'
            'user_id  INTEGER NOT NULL,'
            'CONSTRAINT fk_exam FOREIGN KEY (exam_id) REFERENCES main_exam(exam_id),'
            'CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES main_user(user_id)'
            ');'

            'CREATE TABLE IF NOT EXISTS main_exam_question ('
            'exam_question_id  INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,'
            'asset_id  INTEGER NOT NULL,'
            'description  VARCHAR(1000) NOT NULL,'
            'CONSTRAINT fk_asset FOREIGN KEY (asset_id) REFERENCES main_asset(asset_id));'

            'CREATE TABLE IF NOT EXISTS main_exam_question_answer ('
            'answer_id  INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,'
            'exam_question_id  INTEGER NOT NULL,'
            'asset_id  INTEGER NOT NULL,'
            'description  VARCHAR(1000) NOT NULL,'
            'correct  BOOLEAN NOT NULL,'
            'CONSTRAINT fk_question FOREIGN KEY (exam_question_id) REFERENCES main_exam_question(exam_question_id),'
            'CONSTRAINT fk_asset FOREIGN KEY (asset_id) REFERENCES main_asset(asset_id));'
        )
    ]