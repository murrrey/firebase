from firebase import firebase



firebase = firebase.FirebaseApplication("https://pythondbtest-83b03.firebaseio.com/",None)


data = {

  'Name':'paul kariuki',
  'Email':'kariuki08@gmail.com',
  'phone': 244799567474

}

result = firebase.post('/pythondbtest-83b03/Customer',data)
print(result)