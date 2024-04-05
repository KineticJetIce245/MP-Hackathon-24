from Point import Point

# Point Clouds
class PointStage:
    # Initiate with an array of points
    def __init__(self, point_cloud: list[Point]) -> None:
        self.point_cloud = point_cloud
        
s = PointStage()