from shapely.geometry import Polygon, LineString
from shapely.ops import unary_union
import matplotlib.pyplot as plt
from descartes import PolygonPatch

def create_polygon_from_rectangles(rectangles, pipe_width=0.5):
    shapes = []
    
    for rect in rectangles:
        x1, y1, x2, y2 = rect  # Unpacking rectangle coordinates
        shapes.append(Polygon([(x1, y1), (x2, y1), (x2, y2), (x1, y2)]))
    
    # Connecting rectangles with thin pipes
    for i in range(len(rectangles) - 1):
        x1, y1, x2, y2 = rectangles[i]
        x3, y3, x4, y4 = rectangles[i + 1]
        
        # Finding center points to connect with a thin pipe
        center1 = ((x1 + x2) / 2, (y1 + y2) / 2)
        center2 = ((x3 + x4) / 2, (y3 + y4) / 2)
        
        # Creating a thin rectangle as a pipe
        if center1[0] == center2[0]:  # Vertical connection
            pipe = Polygon([
                (center1[0] - pipe_width / 2, center1[1]),
                (center1[0] + pipe_width / 2, center1[1]),
                (center2[0] + pipe_width / 2, center2[1]),
                (center2[0] - pipe_width / 2, center2[1])
            ])
        else:  # Horizontal connection
            pipe = Polygon([
                (center1[0], center1[1] - pipe_width / 2),
                (center1[0], center1[1] + pipe_width / 2),
                (center2[0], center2[1] + pipe_width / 2),
                (center2[0], center2[1] - pipe_width / 2)
            ])
        
        shapes.append(pipe)
    
    # Merging all shapes into one polygon
    merged_polygon = unary_union(shapes)
    return merged_polygon

def plot_polygon(polygon):
    fig, ax = plt.subplots()
    if polygon.geom_type == 'Polygon':
        ax.add_patch(PolygonPatch(polygon, alpha=0.5, edgecolor='black'))
    elif polygon.geom_type == 'MultiPolygon':
        for poly in polygon.geoms:
            ax.add_patch(PolygonPatch(poly, alpha=0.5, edgecolor='black'))
    ax.set_xlim(-1, 15)
    ax.set_ylim(-1, 3)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Example usage:
rectangles = [
    (0, 0, 4, 2),
    (5, 0, 9, 2),
    (10, 0, 14, 2)
]

polygon = create_polygon_from_rectangles(rectangles)
plot_polygon(polygon)