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

    def add_room(self, room):
        """
        Add a room to the graph.
        """
        self.rooms[room] = {}

        for exit in player.current_room.get_exits():
            self.rooms[room][exit] = '?'

        if self.travelled_from is not None:
            if self.traveled_from  == 'n':
                self.rooms[room]['s'] == self.last_room
            elif self.traveled_from  == 's':
                self.rooms[room]['n'] == self.last_room
            elif self.traveled_from  == 'e':
                self.rooms[room]['w'] == self.last_room
            else:
                self.rooms[room]['e'] == self.last_room
            


        return self.rooms[room]

    def travel(self, starting_room):
        # this adds the first room
        current_room = self.add_room(starting_room)

        q = Queue()
        q.enqueue(starting_room)

        visited = []

        while q.size() > 0:



    def bft(self, starting_room):
        q = Queue()
        q.enqueue(starting_room)

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if self.vertices.get(v1) == None or self.vertices.get(v2) == None:
            raise IndexError(f"{v1} is not in the graph, bruh. try running add_vertex({v1} first.) ")
        self.vertices[v1].add(v2)


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
