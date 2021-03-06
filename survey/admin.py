# -*- coding: utf-8 -*-

from django.contrib import admin

from survey.models import Answer, Category, Question, Response, Survey, Video, VideoCategory

from .actions import make_published


class QuestionInline(admin.TabularInline):
    model = Question
    ordering = ('order', 'category',)
    extra = 1


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 0


class SurveyAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'need_logged_user', 'template')
    list_filter = ('is_published', 'need_logged_user')
    inlines = [CategoryInline, QuestionInline]
    actions = [make_published]


class AnswerBaseInline(admin.StackedInline):
    fields = ('question', 'body')
    readonly_fields = ('question',)
    extra = 0
    model = Answer


class ResponseAdmin(admin.ModelAdmin):
    list_display = ('interview_uuid', 'survey', 'created', 'user')
    list_filter = ('survey', 'created')
    date_hierarchy = 'created'
    inlines = [AnswerBaseInline]
    # specifies the order as well as which fields to act on
    readonly_fields = (
        'survey', 'created', 'updated', 'interview_uuid', 'user'
    )
    
    
class VideoAdmin(admin.ModelAdmin):
    model = Video
    extra = 0


# admin.site.register(Question, QuestionInline)
# admin.site.register(Category, CategoryInline)
admin.site.register(Survey, SurveyAdmin)
admin.site.register(Response, ResponseAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(VideoCategory)
