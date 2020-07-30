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
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

##### THE TRAVERSAL PATH #####

# We start with zero and make that our initial graph
# After one movement, we update the graph by updating nodes with that connected edges
# Keep going until current node as no question marks
# THEN traverse until a node is found with question marks and continue in that direction

class Graph:

    def __init__(self):
        self.rooms = {}
        self.traversal_path = []
        self.travelled_from = None
        self.last_room = None

    def add_room(self, room_id):
        """
        Add a room to the graph.
        """

        # Only adds a room if it has not been marked yet
        if room_id not in self.rooms:
            self.rooms[room_id] = {}

            # defaults every exit to ?
            for exit in player.current_room.get_exits():
                self.rooms[room_id][exit] = '?'

            # checks the last room we came from to make connection
            if self.travelled_from is not None:
                if self.traveled_from  == 'n':
                    self.rooms[room_id]['s'] == self.last_room
                elif self.traveled_from  == 's':
                    self.rooms[room_id]['n'] == self.last_room
                elif self.traveled_from  == 'e':
                    self.rooms[room_id]['w'] == self.last_room
                else:
                    self.rooms[room_id]['e'] == self.last_room

        # returns the whole room and exits
        return self.rooms[room_id]

    def travel(self):
        # this adds the current room
        current_room = self.add_room(player.current_room.id)

        # travels as long as the current room has a question mark in any direction
        if '?' in current_room.values():
            for direction, value in current_room.items():
                # the first mystery direction is followed, we travel, updated where we came from, and add to path
                # we then travel again from the new room
                if value is '?':
                    player.travel(direction)
                    self.travelled_from = direction
                    self.last_room = current_room
                    self.traversal_path.append(direction)
                    self.travel()
                    break

        # this is when we must traverse to find a new starting room
        # every direction has been found or one doesn't exist
        # no mystery directions
        elif '?' not in current_room.values():

            # implement BFT to find first room with a question mark
            self.bft(current_room)


    def bft(self, starting_room):
        start =
        q = Queue()
        q.enqueue(start)

            visited = []

            while q.size() > 0:
                current_room = q.dequeue()
                visited.append(current_room)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
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
