import numpy as np
import random

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None

def rrt_path(obstacles, start=(50, 50), goal=(550, 550), max_iter=1000):
    """Generate path using RRT (Rapidly-exploring Random Tree) algorithm.
    
    Args:
        obstacles: List of obstacle coordinates
        start: Start point coordinates
        goal: Goal point coordinates
        max_iter: Maximum iterations
        
    Returns:
        list: Path coordinates if found, None otherwise
    """
    nodes = [Node(start[0], start[1])]
    goal_node = Node(goal[0], goal[1])
    
    for _ in range(max_iter):
        # Random sampling
        if random.random() < 0.1:
            x_rand = Node(goal[0], goal[1])
        else:
            x_rand = Node(
                random.randint(0, 600),
                random.randint(0, 600)
            )
        
        # Find nearest node
        nearest_node = min(nodes, key=lambda n: np.hypot(
            n.x - x_rand.x,
            n.y - x_rand.y
        ))
        
        # Extend towards random point
        theta = np.arctan2(
            x_rand.y - nearest_node.y,
            x_rand.x - nearest_node.x
        )
        new_node = Node(
            nearest_node.x + 30 * np.cos(theta),
            nearest_node.y + 30 * np.sin(theta)
        )
        new_node.parent = nearest_node
        
        # Check collision
        collision = False
        for obs in obstacles:
            if np.hypot(
                new_node.x - obs[0],
                new_node.y - obs[1]
            ) < 30:
                collision = True
                break
                
        if not collision:
            nodes.append(new_node)
            
            # Check if goal reached
            if np.hypot(
                new_node.x - goal_node.x,
                new_node.y - goal_node.y
            ) < 30:
                goal_node.parent = new_node
                nodes.append(goal_node)
                break
                
    # Extract path
    if goal_node.parent is None:
        return None
        
    path = []
    node = goal_node
    while node is not None:
        path.append((node.x, node.y))
        node = node.parent
    path.reverse()
    
    return path