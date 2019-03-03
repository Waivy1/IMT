
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from core import models


class IndexPageView(View):
    def get(self, request):

        return render(request, 'index_page.html', {


        })

    def post(self, request):
        input_age = int(request.POST['age'])
        input_height = int(request.POST['height'])
        input_weight = int(request.POST['weight'])


        body_mass_index = (input_weight / ((input_height/100) ** 2))

        print(body_mass_index)

        user = models.User.objects.get(id=request.session['user_id'])

        user_resalt = models.Result(age=input_age, height=input_height, weight=input_weight,
                                    body_mass_index=body_mass_index, user_id=user )
        user_resalt.save()

        bmi_epxplain = [('insufficient weight', 0, 18), ('normal weight', 19, 25), ('obesity 1 degree', 26, 30),
                        ('obesity 2 degree', 31, 35), ('obesity 3 degree', 36, 100)]

        level = bmi_epxplain[-1][0]
        for i in bmi_epxplain:
            if i[1] > body_mass_index <= i[2]:
                level = i[0]
                break

        return render(request, 'index_result.html', {
            'index_result': body_mass_index,
            'level': level

        })

class SignUp(View):
    def get(self, request):
        return render(request, 'sign_up.html')

    def post(self, request):
        print(request.POST)  # {'email': 'kek', 'password': 567, 'csrf': 'aaaaaaaa'}

        name = request.POST['name']
        password = request.POST['password']

        new_user = models.User(name=name, password=password)
        new_user.save()

        return redirect('/')

class Login(View):
    def get(self, request):
        print('1111 ', request.session.get('user_id'))

        if request.session.get('user_id'): # get returns value or None if not exists
            print('0000 ',request.session.get('user_id'))

            return redirect('/')

        return render(request, 'sign_up.html')

    def post(self, request):

        input_name = request.POST['name'] #post це властивість. request is an object. it has post. post is a dict
        input_password = request.POST['password']
        user = models.User.objects.get(name=input_name, password=input_password)
        print('555', user.id)

        request.session['user_id'] = user.id  # writes user.id to user_id key

        return redirect('/')

class History(View):
    def get(self, request):
        user_id = request.session.get('user_id')

        user = models.User.objects.get(id=user_id)
        history = models.Result.objects.filter(user_id=user)
        print(history.values())

        return redirect('/')



