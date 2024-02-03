# Intergers
integer = 2
float = 2.59

class User: 
  def __init__(this, user_name, password): 
    this.name = user_name
    this.password = password

def __str__(this):
  return f"The name is {this.name} and the password is {this.password[:3] + '******'}"
