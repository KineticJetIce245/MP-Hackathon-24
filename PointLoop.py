from Point import Point
class PointLoop:
    def __init__(self, loop: list[Point]) -> None:
        self.point_list = loop
        
    def __str__(self) -> str:
        ret_val = "["
        for k in self.point_list:
            ret_val += k.__str__() + ";"
        return ret_val