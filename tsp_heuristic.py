import arcade
from random import randint
import math
import time
import copy


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Traveling Salesperson"

class TSP_Heuristic(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)
        self.auto = True
        self.num_cities = 3

    def setup(self):
        self.cities = []
        
        for i in range(self.num_cities):
            city = arcade.Point(randint(0,SCREEN_WIDTH-1), randint(0,SCREEN_HEIGHT-1))
            self.cities.append(city)

        self.unvisited = copy.deepcopy(self.cities)
        self.path = [self.unvisited.pop()]
        # remove element at index 0
        self.start_time = time.time()
        self.curr_city = 0
        self.done = False
        

    def on_draw(self):
        arcade.start_render()
        arcade.draw_points(self.cities,arcade.color.WHITE,10)
        if len(self.path) > 1:
            arcade.draw_line_strip(self.path, arcade.color.WHITE, 2)

        if self.done:
            arcade.draw_text(f"Shortest Path: {self.shortest:.3f}",SCREEN_WIDTH//2, SCREEN_HEIGHT-30, arcade.color.WHITE, anchor_x='center')
            arcade.draw_text(f"Time to Find Shortest Path: {self.total_time:.3f} seconds", 
                                SCREEN_WIDTH//2,                                                     
                                SCREEN_HEIGHT - 60,
                                arcade.color.WHITE,
                                anchor_x='center')

    def on_key_press(self, key, modifiers):
        if key == arcade.key.A:
            self.auto = True
            print('auto mode')

        if key == arcade.key.M:
            self.auto = False
            print('manual mode')

        if key == arcade.key.ENTER and not self.auto:
            self.find_next_city()

        if key == arcade.key.R and self.done:
            self.setup()

        if key == arcade.key.MINUS:
            if self.num_cities > 3:
                self.num_cities -= 1
                self.setup()

        if key == arcade.key.PLUS or key == arcade.key.EQUAL:
            self.num_cities += 1
            self.setup()

    def find_next_city(self):
        if len(self.unvisited) > 0: # there are still cities to visit!
            next_city = self.find_closest(self.path[self.curr_city],self.unvisited)
            self.path.append(next_city)
            self.unvisited.remove(next_city)
            self.curr_city += 1
        
        elif not self.done:
            self.shortest = self.get_total_dist(self.path)
            self.total_time = time.time() - self.start_time
            self.done = True


    def on_update(self, delta_time):
        if self.auto:
            self.find_next_city()
        


    def distance_between_points(self, point1, point2):
        ''' 
        returns the linear distance between point1 and point2
        '''
        x1,y1 = point1
        x2,y2 = point2
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)

    def find_closest(self, curr_point, points):
        ''' 
        returns the point in points that is closest to curr_point
        '''
        
        closest = self.distance_between_points(curr_point, points[0])
        closest_point = points[0]
        for i in range(1,len(points)):
            dist = self.distance_between_points(curr_point, points[i])
            if dist < closest:
                closest = dist
                closest_point = points[i]
        return closest_point

    
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
    ts = TSP_Heuristic(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    ts.setup()
    arcade.run()

if __name__ == "__main__":
    main()
