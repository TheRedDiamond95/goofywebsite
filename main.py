from flask import Flask, render_template

app=Flask(_name_)
def index():
  return render_template("main.html")

if _name_='_main_':
  app.run(host='0.0.0.0', port=5000)
