from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.models import Story, UserStoryFile, StoryFile


@api_view(['GET'])
def stories_list(request, project_id, subs_id):
    """Получаем предварительный просмотр историй"""
    stories = Story.objects.filter(project_id=project_id).values('preview', 'order_num', 'id', 'storyfile__story_id')
    for i in stories:
        i['flag'] = len(UserStoryFile.objects.filter(is_watched=True, user=subs_id)) == \
                    len(UserStoryFile.objects.filter(user=subs_id))
    return Response(data=stories)



# @api_view(['GET'])
# def stories_case(request, story_id):
#     certain_stories = StoryFile.objects
