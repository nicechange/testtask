from django.contrib import admin
from .models import Question, Answer, Choice, Quiz


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'title',
         'type',
    )


class ChoiceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'question',
        'lock_other',
    )
    list_filter = ('question',)


class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'user_code',
        'question',
        'answr',

    )
    list_filter = ('user_code',)

class QuizAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'date_start',
        'date_end',
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('date_start',)
        return self.readonly_fields

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Quiz, QuizAdmin)