from flask import Flask, jsonify, request

# Crear la aplicación de Flask
app = Flask(__name__)

# Nuestra "base de datos" en memoria.
# Es una simple lista de diccionarios para empezar.
tasks = [
    {
        'id': 1,
        'title': 'Comprar leche',
        'description': 'Ir al supermercado y comprar un litro de leche',
        'done': False
    },
    {
        'id': 2,
        'title': 'Aprender Docker',
        'description': 'Completar el primer paso del proyecto personal',
        'done': True
    }
]

# Este es nuestro primer "endpoint" o punto de acceso.
# Devuelve todas las tareas cuando alguien visita /tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/task', methods=['POST'])
def add_task():
    # Creamos una nueva tarea con los datos que nos envían (en formato JSON)
    new_task = {
        'id': len(tasks) + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""), # .get para un campo opcional
        'done': False
    }
    # Añadimos la tarea a nuestra "base de datos" (la lista)
    tasks.append(new_task)
    # Devolvemos la tarea que acabamos de crear
    return jsonify({'task': new_task}), 201

# Esto es necesario para ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
