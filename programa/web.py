from flask import Flask, render_template #Importar flask

app = Flask("holaMundo")  #Variable (Objeto)

# Definimos la ruta principal (el home)
@app.route('/')  #Para tener diferentes rutas
def home():
    return render_template('index.html') #para el html

# Iniciamos el servidor
if __name__ == '__main__': 
    app.run(debug=True,host='0.0.0.0', port='5000') #Corre la aplicacion en un servidor
    
