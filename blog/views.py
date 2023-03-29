from django.shortcuts import render

# Create your views here.
def home(request):
    author = 'Wallium Ladrian'
    age = 49
    address ='The Citadel'
    ctx = {'athr': author, 'age':age, 'addr':address}
    return render(request,'home.html',context=ctx)

def categories(request):
    cats =['Python','Django','Web Development','programming']
    return render(request, 'categories.html',
                   context={'categories':cats} )
def articles(request):
    data = [
        {'title' : 'First Article',
        'authon' : 'Waxllium Ladrian' ,
        'date': '2020-01-01'},
        {'title' : 'The Basin of Life',
         'author':'Steris',
         'date':'2022-01-02'} ,
         {'title' : 'The Second Article',
          'author':'Waxllium Ladrian',
          'date' : '2020-01-03'}
            ]
    return render(request,'articles.html',
                      context={'articles':data})