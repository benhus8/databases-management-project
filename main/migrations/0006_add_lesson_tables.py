from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_add_table_course'),
        ('main', '0002_add_user_tables'),
        ('main', '0003_add_asset_table'),
        ('main', '0004_add_exam_tables'),
        ('main', '0005_add_exam_exam_question_table')
    ]

    operations = [
        migrations.RunSQL(
            'CREATE TABLE IF NOT EXISTS main_subject ('
            'subject_id  INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,'
            'course_id  INTEGER NOT NULL,'
            'title  VARCHAR(100) NOT NULL,'
            'seqence  VARCHAR(1000) NOT NULL,'
            'CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES main_course(course_id));'

            'CREATE TABLE IF NOT EXISTS main_lesson ('
            'lesson_id  INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,'
            'subject_id  INTEGER NOT NULL,'
            'seqence  VARCHAR(1000),'
            'short_description  VARCHAR(100),'
            'description  VARCHAR(1000),'
            'CONSTRAINT fk_subject FOREIGN KEY (subject_id) REFERENCES main_subject(subject_id));'

            'CREATE TABLE IF NOT EXISTS main_lesson_content ('
            'lesson_content_id  INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,'
            'lesson_id  INTEGER NOT NULL,'
            'asset_id  INTEGER NOT NULL,'
            'seqence  VARCHAR(1000),'
            'content_type  VARCHAR(100),'
            'CONSTRAINT fk_lesson FOREIGN KEY (lesson_id) REFERENCES main_lesson(lesson_id),'
            'CONSTRAINT fk_asset FOREIGN KEY (asset_id) REFERENCES main_asset(asset_id));'
        )
    ]