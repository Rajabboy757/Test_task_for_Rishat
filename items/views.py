from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import generics
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from .serializers import ItemSerializer
from .models import Items
from rest_framework.response import Response


class ItemView(generics.GenericAPIView):
    serializer_class = ItemSerializer
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', '')
        item = Items.objects.get(pk=pk)
        data = self.serializer_class(item).data
        if request.accepted_renderer.format == 'html':
            return Response(data, template_name='item.html')

        return Response(data)


class BuyView(generics.GenericAPIView):
    serializer_class = ItemSerializer
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer,)
    queryset = Items.objects.all()

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', '')
        item = Items.objects.get(pk=pk)
        data = self.serializer_class(item).data
        if request.accepted_renderer.format == 'html':
            return Response(data, template_name='buy.html')

        return render(request, 'buy.html')


class ItemsListView(ListView):
    model = Items
    template_name = 'home.html'
