from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []
next_id = 3


@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        return jsonify(task)
    return jsonify({'error': 'Задача не найдена'}), 404


@app.route('/tasks', methods=['POST'])
def create_task():
    global next_id
    data = request.get_json()

    new_task = {
        'id': next_id,
        'title': data.get('title'),
        'completed': data.get('completed', False)
    }
    tasks.append(new_task)
    next_id += 1

    return jsonify(new_task), 201


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        return jsonify({'error': 'Задача не найдена'}), 404

    data = request.get_json()
    task['title'] = data.get('title', task['title'])
    task['completed'] = data.get('completed', task['completed'])

    return jsonify(task)


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        return jsonify({'error': 'Задача не найдена'}), 404

    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({'message': 'Задача удалена'}), 200


if __name__ == '__main__':
    app.run(debug=True)