from firebase import firebase


firebase = firebase.FirebaseApplication("https://pythondbtest-83b03.firebaseio.com/",None)

firebase.delete('/pythondbtest-83b03/Customer','-M1nZuLn0kwn6pYJs4mW')


print('record deleted')