import math
import sqlite3

class Figures:
    def __init__(self):
        pass

    def get_name(self):
        return self.__class__.__name__

    def get_lenght_vector(self, first_point:tuple, second_point:tuple)->float:
        result = (second_point[0]-first_point[0])**2+(second_point[1]-first_point[1])**2
        return (result)**(1/2)

    def get_area(self):
        pass

    def get_perimeter(self):
        pass

    def count_popular(self):
        return f"{self.get_name()}_{self.count_populations}"

class DotedFigures(Figures):
    def __init__(self, lst_points:tuple):
        self.lst_points = lst_points

    def get_perimeter(self)->float:
        lst_lenghts = []
        for i in range(len(self.lst_points)-1):
            lst_lenghts.append(self.get_lenght_vector(self.lst_points[i],self.lst_points[i+1]))
        lst_lenghts.append(self.get_lenght_vector(self.lst_points[0],self.lst_points[-1]))
        return sum(lst_lenghts)

class SmoothFigures(Figures):
    def __init__(self, centre: tuple, radius: float):
        self.centre = centre
        self.radius = radius

    def get_area(self):
        return (self.radius**2) * math.pi

    def get_perimeter(self):
        return 2*math.pi*self.radius

class Circle(SmoothFigures):
    count_populations = 0
    def __init__(self, centre, radius):
        super(Circle, self).__init__(centre, radius)
        Circle.count_populations += 1
        self.name = self.count_popular()

    def __str__(self):
        return f"{self.name} Круг!"

class Quadrilateral(DotedFigures):
    count_populations = 0

    def __init__(self, lst_points):
        super(Quadrilateral, self).__init__(lst_points)
        Quadrilateral.count_populations += 1
        self.name = self.count_popular()

    def get_area(self):
        a = self.get_lenght_vector(self.lst_points[1],self.lst_points[2])
        b = self.get_lenght_vector(self.lst_points[2],self.lst_points[3])
        result_area = a*b
        return result_area

    def __str__(self):
        return f"{self.name} Квадрат!"

class Triangle(DotedFigures):
    count_populations = 0
    def __init__(self, lst_points):
        super(Triangle, self).__init__(lst_points)
        Triangle.count_populations += 1
        self.name = self.count_popular()

    def get_height(self):
        p = self.get_perimeter()/2
        x = 1
        for i in range(len(self.lst_points)-1):
            x *= p - self.get_lenght_vector(self.lst_points[i], self.lst_points[i+1])
        x *= (p - self.get_lenght_vector(self.lst_points[0], self.lst_points[-1]))*p
        x = (2*(x)**(1/2))/self.get_lenght_vector(self.lst_points[0], self.lst_points[-1])
        return x

    def get_area(self):
        b = self.get_lenght_vector(self.lst_points[0], self.lst_points[-1])
        h = self.get_height()
        return b*h/2

    def __str__(self):
        return f"{self.name} Треугольник!"

class Polygon(DotedFigures):
    count_populations = 0

    def __init__(self, lst_points):
        super(Polygon, self).__init__(lst_points)
        Polygon.count_populations += 1
        self.name = self.count_popular()
        self.check_right()

    def check_right(self):
        copy_lst_points = self.lst_points
        copy_lst_points.append(self.lst_points[0])
        copy_lst_points.append(self.lst_points[1])
        for i in range(len(self.lst_points)-2):
            vector = (copy_lst_points[i+1][0]-copy_lst_points[i][0], copy_lst_points[i+1][1]-copy_lst_points[i][1])
            test_vector = (copy_lst_points[i+2][0]-copy_lst_points[i][0], copy_lst_points[i+2][1]-copy_lst_points[i][1])
            dot_product = vector[0] * test_vector[0] + vector[1] * test_vector[1]
            if dot_product <= 0:
                raise Exception('Многоуголник не выпуклый, либо введите точки в другом порядке.')
        return True

    def get_area(self):
        n = len(self.lst_points)
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += self.lst_points[i][0] * self.lst_points[j][1]
            area -= self.lst_points[i][1] * self.lst_points[j][0]
        area /= 2.0
        return abs(area)

class DBHelper:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.cursor.execute(query)
        self.conn.commit()

    def insert_data(self, table_name, values):
        placeholders = ", ".join("?" * len(values))
        query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        self.cursor.execute(query, values)
        self.conn.commit()

    def fetch_data(self, table_name, conditions=None):
        query = f"SELECT * FROM {table_name}"
        if conditions:
            query += f" WHERE {conditions}"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    def update_data(self, table_name, set_clause, conditions=None):
        query = f"UPDATE {table_name} SET {set_clause}"
        if conditions:
            query += f" WHERE {conditions}"
        self.cursor.execute(query)
        self.conn.commit()

    def delete_data(self, table_name, conditions=None):
        query = f"DELETE FROM {table_name}"
        if conditions:
            query += f" WHERE {conditions}"
        self.cursor.execute(query)
        self.conn.commit()

    def close(self):
        self.conn.close()

points1 = [(1,1), (0,3), (2,5), (4,3), (3,1)]
# points2 = [(2,2), 5]
trigan1 = Polygon(points1)
# trigan2 = Polygon(points2[0],points2[1])
print(trigan1.get_perimeter())
# print(trigan2)