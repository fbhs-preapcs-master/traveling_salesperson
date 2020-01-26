import arcade
from itertools import permutations
from random import randint
import math
import time


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Traveling Salesperson"


class TravelingSales(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)
        self.num_cities = 3


    def setup(self):
        self.cities = []
        for i in range(self.num_cities):
            city = arcade.Point(randint(0,SCREEN_WIDTH-1), randint(0,SCREEN_HEIGHT-1))
            self.cities.append(city)
        self.shortest = self.get_total_dist(self.cities)
        self.permutations = list(permutations(self.cities))
        self.current_permutation = 0
        self.start_time = time.time()
        self.done = False

    def on_draw(self):
        arcade.start_render()
        arcade.draw_points(self.cities,arcade.color.WHITE,10)
        arcade.draw_line_strip(self.cities, arcade.color.WHITE, 2)
        percent_done = self.current_permutation / (len(self.permutations)-1) * 100
        arcade.draw_text(f'{percent_done:.3f}%',SCREEN_WIDTH//2,30,arcade.color.WHITE,24,anchor_x='center')
        arcade.draw_text(f"Shortest Path: {self.shortest:.3f}",SCREEN_WIDTH//2, SCREEN_HEIGHT-30, arcade.color.WHITE, anchor_x='center')
        if self.done:
            arcade.draw_text(f"Time to Find Shortest Path: {self.total_time:.3f} seconds", 
                                SCREEN_WIDTH//2,                                                     
                                SCREEN_HEIGHT - 60,
                                arcade.color.WHITE,
                                anchor_x='center')

    def on_update(self, delta_time):
        if self.current_permutation < len(self.permutations)-1:
            self.current_permutation += 1
            next_path = self.permutations[self.current_permutation]
            dist = self.get_total_dist(next_path)
            if dist < self.shortest:
                self.shortest = dist
                self.cities = next_path
        elif not self.done:
            self.total_time = time.time() - self.start_time
            self.done = True

    def on_key_press(self, key, modifiers):
        if key == arcade.key.R:
            self.setup()

        if key == arcade.key.MINUS:
            if self.num_cities > 3:
                self.num_cities -= 1
                self.setup()

        if key == arcade.key.PLUS or key == arcade.key.EQUAL:
            self.num_cities += 1
            self.setup()

        

    def distance_between_points(self, point1, point2):
        ''' 
        returns the linear distance between point1 and point2
        '''
        x1,y1 = point1
        x2,y2 = point2
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)

    def get_total_dist(self, points):
        '''
        returns the total distance of the current path
        '''
        total_dist = 0
        for i in range(len(points)-1):
            # add the distance from the current point to the next point
            total_dist += self.distance_between_points(points[i], points[i+1])
        return total_dist




def main():
    ts = TravelingSales(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    ts.setup()
    arcade.run()

if __name__ == "__main__":
    main()
