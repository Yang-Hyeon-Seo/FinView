from django.shortcuts import render

# Create your views here.
def index(request):
    """
    전체 금융 게시글 목록 조회 및 출력
    """
    context = {
        
    }
    return render(request, 'index.html', context)