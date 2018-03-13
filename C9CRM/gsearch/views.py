# Create your views here.
import simplejson as json
from django.http import HttpResponse
from haystack.query import SearchQuerySet


def autocomplete(request):
    sqs = SearchQuerySet().filter(content=request.GET.get('q', ''))[:5]
    suggestions = [result.object.title for result in sqs]
    # Make sure you return a JSON object, not a bare list.
    # Otherwise, you could be vulnerable to an XSS attack.
    the_data = json.dumps({
        'results': suggestions
    })
    print(the_data)
    return HttpResponse(the_data, content_type='application/json')
