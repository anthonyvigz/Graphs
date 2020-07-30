rooms = {
  0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}
}

current_room = rooms[0]

if '?' in current_room.values():
    for direction, value in current_room.items():
        print(value)

if 0 not in rooms:    
    print(current_room.items())