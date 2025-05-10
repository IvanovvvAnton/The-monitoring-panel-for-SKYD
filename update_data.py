@app.route('/update_users', methods=['POST'])
def update_users():
    global all_events

    data = request.json
    full_name = data.get("full_name")
    status = data.get("status")  
    event_type = "Вход" if status == 1 else "Выход"
    now = datetime.now()

    event_date = now.strftime("%d-%m-%Y")
    event_time = now.strftime("%H:%M:%S")

    all_events.append({
        "date": event_date,
        "time": event_time,
        "event_type": event_type,
        "full_name": full_name
    })

    log_to_users(full_name, event_type)

    socketio.emit('update_data', all_events)

    return jsonify({"status": "success"}), 200
