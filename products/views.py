from django.shortcuts import render
import pyrebase

# Create your views here.

config = {
    'apiKey': "AIzaSyAsWqQy2VLYrl9PC29vDFR8Kj8RJyRdafg",
    'authDomain': "ecommerce-acf50.firebaseapp.com",
    'databaseURL': "https://ecommerce-acf50-default-rtdb.firebaseio.com",
    'projectId': "ecommerce-acf50",
    'storageBucket': "ecommerce-acf50.appspot.com",
    'messagingSenderId': "121271982795",
    'appId': "1:121271982795:web:24c749fbff46d479a7194e"
}

# Firebase authentication
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


def products(request):
    name = database.child('Data').child('Name').get().val()
    stack = database.child('Data').child('Stack').get().val()
    framework = database.child('Data').child('Framework').get().val()

    context = {
        'name':name,
        'stack':stack,
        'framework':framework
    }
    return render(request, 'products.html', context)

