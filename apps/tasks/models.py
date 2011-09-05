# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.


STATUS_CHOISES = (
    ('active', u'Активен'),
    ('complate', u'Выполнен'),
    ('paused', u'Приостановлен'),
    ('canceled', u'Отменен')
)

def get_statis_label(choice):

    for status, label in STATUS_CHOISES:
        if status == choice: return  label
    return choice


class Project(models.Model):
    name = models.CharField(
        verbose_name=u'Название проекта',
        unique=True,
        max_length=256,
    )

    descriprion = models.TextField(
        verbose_name=u'Описание проекта',
        max_length=102400
    )

    status = models.CharField(
        verbose_name=u'Статус',
        max_length=16,
        choices=STATUS_CHOISES,
        default=STATUS_CHOISES[0],
        db_index=True,
    )

    start_date = models.DateTimeField(
        verbose_name=u'Дата начала',
        db_index=True,
    )

    end_date = models.DateTimeField(
        verbose_name=u'Дата завершения',
        db_index=True,
    )

    def __unicode__(self):
        return self.name

    def active_miles_count(self):
        return self.milestone_set.filter(status='active').count()

class Milestone(models.Model):
    project = models.ForeignKey(
        Project,
        verbose_name=u"Проект"
    )
    name = models.CharField(
        verbose_name=u'Название этапа',
        unique=True,
        max_length=256,
    )

    descriprion = models.TextField(
        verbose_name=u'Описание этапа',
        max_length=102400
    )

    status = models.CharField(
        verbose_name=u'Статус',
        max_length=16,
        db_index=True,
        choices=STATUS_CHOISES,
        default=STATUS_CHOISES[0]
    )

    priority = models.IntegerField(
        verbose_name=u"Приоритет",
        default=100,
        db_index=True,
    )

    start_date = models.DateTimeField(
        verbose_name=u'Дата начала',
        db_index=True,
    )

    end_date = models.DateTimeField(
        verbose_name=u'Дата завершения',
        db_index=True,
    )

    depends_from = models.ManyToManyField(
        'self',
        verbose_name=u'Зависит от этапов',
        blank=True, null=True
    )

    def __unicode__(self):
        return unicode(self.project.name) + ': ' + self.name

    def complated_task_count(self):
        return self.task_set.filter(status='complate').count()

    def get_active_tasks_count(self):
        return self.task_set.filter(status='active').count()

    def status_label(self):
        return get_statis_label(self.status)


class Task(models.Model):
    milestone = models.ForeignKey(
        Milestone,
        verbose_name=u'Этап'
    )
    name = models.CharField(
        verbose_name=u'Название задачи',
        unique=True,
        max_length=256,
    )

    descriprion = models.TextField(
        verbose_name=u'Описание задачи',
        max_length=102400
    )

    status = models.CharField(
        verbose_name=u'Статус',
        max_length=16,
        choices=STATUS_CHOISES,
        default=STATUS_CHOISES[0],
        db_index=True,
    )

    priority = models.IntegerField(
        verbose_name=u"Приоритет",
        default=100,
        db_index=True,
    )

    responsible = models.ManyToManyField(
        User,
        verbose_name=u'Ответственные'
    )

    start_date = models.DateTimeField(
        verbose_name=u'Дата начала',
        db_index=True,
    )

    end_date = models.DateTimeField(
        verbose_name=u'Дата завершения',
        db_index=True,
    )

    depends_from = models.ManyToManyField(
        'self',
        verbose_name=u'Зависит от задач',
        blank=True, null=True
    )

    def __unicode__(self):
        return unicode(self.milestone) + u': ' + self.name


def check_milestone_for_complate(sender, instance, created, **kwargs):
    active_tasks_count = Task.objects.filter(milestone=instance.milestone, status=u'active').count()
    print active_tasks_count
    if active_tasks_count > 0: return
    instance.milestone.status = 'complate'
    instance.milestone.save()

post_save.connect(check_milestone_for_complate, sender=Task)