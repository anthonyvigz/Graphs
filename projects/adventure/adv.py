from room import Room
from player import Player
from world import World

from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


##### THE TRAVERSAL PATH #####

# We start with zero and make that our initial graph
# After one movement, we update the graph by updating nodes with that connected edges
# Keep going until current node as no question marks
# THEN traverse until a node is found with question marks and continue in that direction


class Graph:

    def __init__(self, room_graph):
        self.rooms = {}
        self.traversal_path = []
        self.travelled_from = None
        self.last_room = None
        self.current_room_id = None
        self.final_length = len(room_graph)
        self.completed = False

    def add_room(self, room_id):
        """
        Add a room to the graph.
        """
        self.current_room_id = room_id
        # Only adds a room if it has not been marked yet
        if room_id not in self.rooms:
            self.rooms[room_id] = {}
            print("adding room", room_id)

            # defaults every exit to ?
            for exit in player.current_room.get_exits():
                self.rooms[room_id][exit] = '?'

            # checks the last room we came from to make connection
            print(self.travelled_from)
            if self.travelled_from is not None:
                if self.travelled_from == 'n':
                    self.rooms[room_id]['s'] = self.last_room
                    self.rooms[self.last_room]['n'] = room_id
                elif self.travelled_from == 's':
                    self.rooms[room_id]['n'] = self.last_room
                    self.rooms[self.last_room]['s'] = room_id
                elif self.travelled_from == 'e':
                    self.rooms[room_id]['w'] = self.last_room
                    self.rooms[self.last_room]['e'] = room_id
                else:
                    self.rooms[room_id]['e'] = self.last_room
                    self.rooms[self.last_room]['w'] = room_id

        # returns the whole room and exits
        return self.rooms[room_id]

    def get_neighbor_rooms(self, current_room):
        # get all surrounding rooms of a room
        neighbors = []

        for neighbor in current_room.values():
            neighbors.append(neighbor)

        return neighbors

    def travel(self):
        # this adds the current room
        current_room = self.add_room(player.current_room.id)
        self.last_room = player.current_room.id

        # travels as long as the current room has a question mark in any direction
        if '?' in current_room.values():
            print(self.rooms)
            for direction, value in current_room.items():
                # the first mystery direction is followed, we travel, updated where we came from, and add to path
                # we then travel again from the new room
                if value == '?':
                    player.travel(direction)
                    self.travelled_from = direction
                    self.traversal_path.append(direction)
                    self.travel()
                    break

        # this is when we must traverse to find a new starting room
        # every direction has been found or one doesn't exist
        # no mystery directions
        elif '?' not in current_room.values():
            print(self.rooms)
            print("searching for a new mystery room")

            # implement BFT to find first room with a question mark
            if self.completed == False:
                self.bfs(player.current_room.id)

        return self.traversal_path

    def bfs(self, starting_room):
        q = Queue()
        q.enqueue([starting_room])

        # track visited rooms
        visited = []

        # look for shortest path to next ? room

        while q.size() > 0 and self.completed == False:
            # List of the current rooms in path
            path = q.dequeue()
            print("path:", path)

            # room at end of path
            id = path[-1]

            # we are done searching if there is a '?' in the values
            # and it's the shortest path found
            if '?' in self.rooms[id].values():
                # our shortest path is declared
                roomsTraverse = path
                directions = []
                print("checking room:", self.rooms[id])
                # for every room in the shortest path, find the directional
                # path
                for i in range(len(roomsTraverse)):
                    if i < (len(roomsTraverse) - 1):
                        next = self.rooms[roomsTraverse[i + 1]]
                        for direction, room in next.items():
                            # where the value of the next room appears in the current room
                            # make the connection and direct
                            if room == roomsTraverse[i]:
                                # right now appending direction of next room but need previous room
                                direct = None
                                if direction == 'n':
                                    direct = 's'
                                elif direction == 's':
                                    direct = 'n'
                                elif direction == 'w':
                                    direct = 'e'
                                else:
                                    direct = 'w'
                                directions.append(direct)
                    # once it gets to final room of current path
                    # stop appending, that's our new start
                    else:
                        pass
                print("directions:", directions)
                # use the directions to get to room with ?
                # and add to main traversal path
                for direction in directions:
                    self.traversal_path.append(direction)
                    player.travel(direction)

                self.travelled_from = player.current_room.id
                print("gonna travel from:", self.travelled_from)
                self.travel()

            else:
                # check the room for neighbors unvisited and travel
                # loop through curr
                if id not in visited:
                    visited.append(id)
                    print("visited", visited)

                    for room_id in self.rooms[id].values():
                        # Copy the path
                        path_copy = list(path)
                        path_copy.append(room_id)
                        # enqueue the neighbors we haven't visited
                        q.enqueue(path_copy)

                 # checks if all rooms visited
                if len(visited) == self.final_length:
                    print("all rooms visited")
                    print(self.traversal_path)
                    self.completed = True

        if self.completed == True:
            print('exiting')
            self.travel()


# Fill this out with directions to walk
# traversal_path = ['n', 'n']
g = Graph(room_graph)
traversal_path = g.travel()
print(traversal_path)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
