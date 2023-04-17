from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Chat, Course, IncompleteQuestion, Intent, User
from .serializers import ChatSerializer, CourseSerializer, IncompleteQuestionSerializer, IntentSerializer, UserSerializer

# Create your views here.


class ChatListViewSet(ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def get_serializer_context(self):
        return {'request': self.request}

@api_view(['GET'])
def chat_list(request):
    if request.method == 'GET':
        queryset = Chat.objects.all()
        serializer = ChatSerializer(queryset, many=True, context = {'request': request})
        return Response(serializer.data)
    

@api_view(['GET'])
def chat_detail(request, id):
    chat = get_object_or_404(Chat, pk=id)
    if request.method == 'GET':
        serializer = ChatSerializer(chat)
        return Response(serializer.data)   
    

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer 

    def get_serializer_context(self):
        return {'request': self.request}


@api_view(['GET'])
def course_list(request):
    if request.method == 'GET':
        queryset = Course.objects.select_related('instructor').all()
        serializer = CourseSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    
    
@api_view(['GET'])
def course_detail(request, id):
    course = get_object_or_404(Course, pk=id)
    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    

class IncompleteQuestionViewSet(ModelViewSet):
    queryset = IncompleteQuestion.objects.all()
    serializer_class = IncompleteQuestionSerializer

    def get_serializer_context(self):
        return {'request': self.request}
    

@api_view(['GET'])
def incompletequestion_list(request):
    if request.method == 'GET':
        queryset = IncompleteQuestion.objects.all()
        serializer = IncompleteQuestionSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    

@api_view(['GET'])    
def incompletequestion_detail(request, id):
    incompletequestion = get_object_or_404(IncompleteQuestion, pk=id)
    if request.method == 'GET':
        serializer = IncompleteQuestionSerializer(incompletequestion)
        return Response(serializer.data)
    

class IntentViewSet(ModelViewSet):
    queryset = Intent.objects.all()
    serializer_class = IntentSerializer

    def get_serializer_context(self):
        return {'request': self.request}

    
@api_view(['GET'])
def intent_list(request):
    if request.method == 'GET':
        queryset = Intent.objects.all()
        serializer = IntentSerializer(queryset, many=True, context={'request':request})
        return Response(serializer.data)
    

@api_view(['GET'])
def intent_detail(request, id):
    intent = get_object_or_404(Intent, pk=id)
    if request.method == 'GET':
        serializer = IntentSerializer(intent)
        return Response(serializer.data)
    

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_context(self):
        return {'request': self.request}
    
    
@api_view(['GET'])
def user_list(request):
    if request.method == 'GET': 
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True, context={'request':request})
        return Response(serializer.data)


@api_view(['GET', 'DELETE'])
def user_detail(request, id):
    user = get_object_or_404(User, pk=id)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        pass


def login(request):

    """username = ""
    password = ""
    user = get_object_or_404(User, email=username)
    if(username == user.email and password == user.password):
        #send request back 
  
    else:
        #raise exception"""

    return render(request, 'login.html')



def chatscreen(request):
    return render(request, 'chatscreen.html')

def signup(request):
    return render(request, 'signup.html')

