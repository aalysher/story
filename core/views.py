from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.models import Story


@api_view(['GET'])
def stories_list(request, project_id, subs_id):
    """Получаем предварительный просмотр историй"""
    stories = Story.objects.filter(project_id=project_id).values('preview', 'order_num', 'id')
    return Response(data=stories)

def watched_all():
    pass
