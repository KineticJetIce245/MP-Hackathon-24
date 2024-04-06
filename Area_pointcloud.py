# function to caluclate triangles

def calculate_triangle_area(A, B, C):
    # Vector AB
    AB = (B[0] - A[0], B[1] - A[1], B[2] - A[2])
    # Vector AC
    AC = (C[0] - A[0], C[1] - A[1], C[2] - A[2])
    
    # Cross product of vectors AB and AC
    cross_product = (AB[1]*AC[2] - AB[2]*AC[1],
                     AB[2]*AC[0] - AB[0]*AC[2],
                     AB[0]*AC[1] - AB[1]*AC[0])
    
    # Magnitude of the cross product vector
    magnitude = (cross_product[0]**2 + cross_product[1]**2 + cross_product[2]**2)**0.5
    
    # Area of the triangle
    area = 0.5 * magnitude
    return area

def calculate_mesh_area(mesh):
    total_area = 0
    for triangle in mesh:
        A, B, C = triangle
        total_area += calculate_triangle_area(A, B, C)
    return total_area

# Example mesh (list of triangles, where each triangle is defined by three vertices)
mesh = [
    [(0, 0, 0), (1, 0, 0), (0, 1, 0)],  # Triangle 1
    [(1, 0, 0), (1, 1, 0), (0, 1, 0)],  # Triangle 2
    # Add more triangles as needed
]

# Calculate the surface area of the mesh
area = calculate_mesh_area(mesh)

