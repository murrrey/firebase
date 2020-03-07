from firebase import firebase



firebase = firebase.FirebaseApplication('https://pythondbtest-83b03.firebaseio.com/',None)


result = firebase.get('/pythondbtest-83b03/Customer','')

print(result)

