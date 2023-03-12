import openai
from django.shortcuts import render
from django.conf import settings
from .models import Post

# openai API 키 설정
openai.api_key = settings.OPEN_API_KEY

def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(title=title, content=content)
    else:
        post = None
    return render(request, 'index.html', {'post': post})

def create_content(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        # 한국어로 번역
        response = openai.Completion.create(
            engine='text-davinci-002',
            prompt=f'제목: {title}\n상세내용: {content}\n위 두 가지 내용을 토대로 SNS 홍보용 컨텐츠를 제작해주세요.\n원하는 항목은 제목, 내용, 해시태그 세가지 항목으로 답해주세요',
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        content = response.choices[0].text

        return render(request, 'result.html', {'content': content})
    else:
        return render(request, 'create_content.html')