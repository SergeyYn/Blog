import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Post
from django.contrib.auth.models import User
from .serializers import PostSerializer, UserSerializer
from collections import OrderedDict

def recursive_ordered_dict_to_dict(ordered_dict):
    simple_dict = {}

    for key, value in ordered_dict.items():
        if isinstance(value, OrderedDict):
            simple_dict[key] = recursive_ordered_dict_to_dict(value)
        else:
            simple_dict[key] = value

    return simple_dict


class PostConsumer(WebsocketConsumer):
    def connect(self):
        self.category_id = str(self.scope['url_route']['kwargs']['id'])
        self.group_name = 'post_list_%s' % self.category_id
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )

        self.accept()
        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'Connection to the socket is succesful'
        }))
        self.send_updated_list()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    #def receive(self, text_data):
    #    pass

    def send_updated_list(self):
        data = self.get_unordered_serialized_posts_dict()
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'send_data',
                'text': data
            }
        )

    def update_list(self, event):
        self.send_updated_list()

    def send_data(self, event):
        self.send(text_data=event["text"])

    def get_unordered_serialized_posts_dict(self):
        category = int(self.category_id)
        posts_list = []
        if category == 0:
            posts_list = self.get_post_list()
        else:
            posts_list = self.get_post_list_by_category(category)
        serialized_posts_list = []
        for post in posts_list:
            serialized_posts_list.append(PostSerializer(post).data)
        serialized_posts_dict = {}
        for i in range(0, len(serialized_posts_list)):
            serialized_posts_dict[str(i)] = serialized_posts_list[i]
        return json.dumps(recursive_ordered_dict_to_dict(serialized_posts_dict))

    def get_post_list(self):
        return Post.objects.all().order_by('-post_date')

    def get_post_list_by_category(self, cat):
        return Post.objects.filter(category_id=cat).order_by('-post_date')


class UserConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = 'admin'
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )

        self.accept()
        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'Connection to the admin socket is succesful'
        }))
        #self.send_updated_list()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    def receive(self, text_data):
        print(text_data)
        text_data_json = json.loads(text_data)
        if text_data_json['action'] == 'logout':
            data = text_data_json['id']
            print(data)
        elif text_data_json['action'] == 'login':
            data = self.get_user(text_data_json['id'])
        print(data)
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'send_data',
                'text': data
            }
        )

    def send_data(self, event):
        self.send(text_data=json.dumps(
            {
                'msg_type': 'user_change',
                'text': event["text"]
            }
        ))

    def get_user(self, id):
        return UserSerializer(User.objects.get(pk=id)).data
