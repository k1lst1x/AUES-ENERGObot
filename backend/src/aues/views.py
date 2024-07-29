import random
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseNotFound, HttpResponseRedirect
import os
import ast

from . import models
# Create your views here.

class TextSerializator(serializers.ModelSerializer):
    class Meta:
        model = models.Texts
        fields = ['pk', 'name', 'text', 'translation']

class RandomText(APIView):
    def get(self, *args, **kwargs):
        all_texts = models.Texts.objects.all()
        random_text = random.choice(all_texts)
        serialized_random_text = TextSerializator(random_text, many=False)
        return Response(serialized_random_text.data)

class NextText(APIView):
    def get(self, request, pk, format=None):
        text = models.Texts.objects.filter(pk__gt=pk).first()
        if not text:
            return HttpResponseNotFound()
        ser_text = TextSerializator(text, many=False)
        return Response(ser_text.data)

class EditFileView(APIView):
    file_path = '../../bot/src/bot_app/translation_dict.py'

    def _parse_translations(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Извлечение словаря translations из файла
        try:
            tree = ast.parse(content, mode='exec')
            translations = {}
            for node in tree.body:
                if isinstance(node, ast.Assign):
                    if isinstance(node.targets[0], ast.Name) and node.targets[0].id == 'translations':
                        translations = ast.literal_eval(node.value)
            return translations
        except Exception as e:
            print(f"Error parsing translations: {e}")
            return {}

    def _write_translations(self, translations):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            content = f"translations = {translations}\n"
            file.write(content)

    def get(self, request):
        translations = self._parse_translations()
        return render(request, 'edit_file.html', {'translations': translations})

    def post(self, request):
        translations = self._parse_translations()
        updated_translations = translations.copy()

        # Обновляем только те ключи, которые присутствуют в POST-запросе
        for key in request.POST:
            if key != 'csrfmiddlewaretoken':  # Пропустить CSRF токен
                updated_translations['kz'][key] = request.POST.get(key).strip()

        self._write_translations(updated_translations)
        return HttpResponseRedirect(request.path)
        