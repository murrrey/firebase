from firebase import firebase


firebase = firebase.FirebaseApplication('https://pythondbtest-83b03.firebaseio.com/',None)

result = firebase.put('/pythondbtest-83b03/Customer/-M1nZuLn0kwn6pYJs4mW','Name','Brian murrey')

print('recored updated')