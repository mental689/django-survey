# -*- coding: utf-8 -*-

from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View

from survey.forms import ResponseForm
from survey.models import Category, Survey, Video, Response


class SurveyDetail(View):

    def get(self, request, *args, **kwargs):
        survey = get_object_or_404(Survey, is_published=True, id=kwargs['id'])
        if request.GET.get("videoID") is not None:
            video = get_object_or_404(Video, id=request.GET.get("videoID"))
        else:
            video = Video.objects.random(survey.video_cat.id)
        responses = Response.objects.filter(video=video)
        if survey.template is not None and len(survey.template) > 4:
            template_name = survey.template
        else:
            if survey.display_by_question:
                template_name = 'survey/survey.html'
            else:
                template_name = 'survey/one_page_survey.html'
        if survey.need_logged_user and not request.user.is_authenticated:
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        categories = Category.objects.filter(survey=survey).order_by('order')
        form = ResponseForm(survey=survey, user=request.user, video=video,
                            step=kwargs.get('step', 0))
        context = {
            'response_form': form,
            'survey': survey,
            'categories': categories,
            'video': video,
            'num_responses': len(responses), # to display the number of votes for this video
        }

        return render(request, template_name, context)

    def post(self, request, *args, **kwargs):
        survey = get_object_or_404(Survey, is_published=True, id=kwargs['id'])
        if survey.need_logged_user and not request.user.is_authenticated:
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        categories = Category.objects.filter(survey=survey).order_by('order')
        video = get_object_or_404(Video, id=request.POST.get("videoID"))
        form = ResponseForm(request.POST, survey=survey, video=video, user=request.user,
                            step=kwargs.get('step', 0))
        context = {'response_form': form, 'survey': survey,
                   'categories': categories, 'video': video}
        if form.is_valid():
            session_key = 'survey_%s' % (kwargs['id'],)
            if session_key not in request.session:
                request.session[session_key] = {}
            for key, value in list(form.cleaned_data.items()):
                request.session[session_key][key] = value
                request.session.modified = True

            next_url = form.next_step_url()
            response = None
            if survey.display_by_question:
                if not form.has_next_step():
                    save_form = ResponseForm(request.session[session_key], video=video,
                                             survey=survey, user=request.user)
                    response = save_form.save()
            else:
                response = form.save()

            if next_url is not None:
                return redirect(next_url)
            else:
                del request.session[session_key]
                if response is None:
                    return redirect('/')
                else:
                    next_ = request.session.get('next', None)
                    if next_ is not None:
                        if 'next' in request.session:
                            del request.session['next']
                        return redirect(next_)
                    else:
                        return redirect('survey-confirmation',
                                        uuid=response.interview_uuid)
        if survey.template is not None and len(survey.template) > 4:
            template_name = survey.template
        else:
            if survey.display_by_question:
                template_name = 'survey/survey.html'
            else:
                template_name = 'survey/one_page_survey.html'
        return render(request, template_name, context)
