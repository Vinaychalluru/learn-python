from django.shortcuts import render, get_object_or_404

from .models import Topic, Entry


# Create your views here.

def index(request):
    """The home page for Learning Log"""
    print(f'request is {request}')
    return render(request,'index.html')

def topic(request, topic_id):
    """Show a topic and all its entries"""
    topic = get_object_or_404(Topic, id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {
        'topic':topic,
        'entries':entries
    }
    return render(request, 'topic.html', context)