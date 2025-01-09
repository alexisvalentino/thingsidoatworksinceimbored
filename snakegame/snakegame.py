import pygame
import random

# Initialize pygame
pygame.init()

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Display dimensions
dis_width = 800
dis_height = 600

# Create the display
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game with Maze Obstacles and Pixel Font')

# Clock
clock = pygame.time.Clock()

# Snake block size and speed
snake_block = 10
snake_speed = 15

# Load a pixelated arcade-style font
pixel_font = pygame.font.Font("ARCADECLASSIC.TTF", 35)  # Replace with the path to your pixel font file

# Function to display the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# Function to display messages
def message(msg, color):
    mesg = pixel_font.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Function to display the score (only the number)
def display_score(score):
    value = pixel_font.render(str(score), True, yellow)  # Only render the score number
    dis.blit(value, [10, 10])

# Function to generate random obstacles with different sizes
def generate_obstacles(num_obstacles):
    obstacles = []
    for _ in range(num_obstacles):
        # Random width and height for obstacles
        obstacle_width = random.randint(2, 5) * snake_block  # 2 to 5 blocks wide
        obstacle_height = random.randint(2, 5) * snake_block  # 2 to 5 blocks tall

        # Random position for obstacles
        obstacle_x = round(random.randrange(0, dis_width - obstacle_width) / 10.0) * 10.0
        obstacle_y = round(random.randrange(0, dis_height - obstacle_height) / 10.0) * 10.0

        obstacles.append([obstacle_x, obstacle_y, obstacle_width, obstacle_height])
    return obstacles

# Function to generate maze-like walls with better randomization
def generate_maze_walls():
    walls = []
    grid_size = snake_block * 5  # Grid size for wall placement

    # Generate vertical walls
    for x in range(0, dis_width, grid_size):
        if random.random() < 0.5:  # 50% chance to place a wall
            wall_height = random.randint(1, 5) * snake_block
            wall_y = random.randint(0, dis_height - wall_height)
            walls.append([x, wall_y, snake_block, wall_height])

    # Generate horizontal walls
    for y in range(0, dis_height, grid_size):
        if random.random() < 0.5:  # 50% chance to place a wall
            wall_width = random.randint(1, 5) * snake_block
            wall_x = random.randint(0, dis_width - wall_width)
            walls.append([wall_x, y, wall_width, snake_block])

    return walls

# Function to generate food that doesn't overlap with obstacles or walls
def generate_food(obstacles, walls):
    while True:
        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

        # Check if food overlaps with any obstacle
        overlap = False
        for obstacle in obstacles:
            if (foodx >= obstacle[0] and foodx < obstacle[0] + obstacle[2] and
                foody >= obstacle[1] and foody < obstacle[1] + obstacle[3]):
                overlap = True
                break

        # Check if food overlaps with any wall
        for wall in walls:
            if (foodx >= wall[0] and foodx < wall[0] + wall[2] and
                foody >= wall[1] and foody < wall[1] + wall[3]):
                overlap = True
                break

        if not overlap:
            return foodx, foody

# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Generate random obstacles and maze walls
    obstacles = generate_obstacles(10)  # Number of obstacles
    walls = generate_maze_walls()  # Generate maze walls

    # Generate initial food
    foodx, foody = generate_food(obstacles, walls)

    # Score
    score = 0

    # Counter for food items eaten
    food_counter = 0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("GAME OVER!", red)
            display_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Check if snake hits the walls
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)

        # Draw food
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        # Draw obstacles (all red)
        for obstacle in obstacles:
            pygame.draw.rect(dis, red, [obstacle[0], obstacle[1], obstacle[2], obstacle[3]])

        # Draw maze walls (all red)
        for wall in walls:
            pygame.draw.rect(dis, red, [wall[0], wall[1], wall[2], wall[3]])

        # Snake head
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Check if snake collides with itself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Check if snake collides with obstacles
        for obstacle in obstacles:
            if (snake_Head[0] >= obstacle[0] and snake_Head[0] < obstacle[0] + obstacle[2] and
                snake_Head[1] >= obstacle[1] and snake_Head[1] < obstacle[1] + obstacle[3]):
                game_close = True

        # Check if snake collides with maze walls
        for wall in walls:
            if (snake_Head[0] >= wall[0] and snake_Head[0] < wall[0] + wall[2] and
                snake_Head[1] >= wall[1] and snake_Head[1] < wall[1] + wall[3]):
                game_close = True

        our_snake(snake_block, snake_List)
        display_score(score)  # Display only the numeric score
        pygame.display.update()

        # Check if snake eats food
        if x1 == foodx and y1 == foody:
            foodx, foody = generate_food(obstacles, walls)
            Length_of_snake += 1
            score += 1
            food_counter += 1

            # Check if 3 food items have been eaten
            if food_counter == 3:
                obstacles = generate_obstacles(10)  # Regenerate obstacles
                walls = generate_maze_walls()  # Regenerate maze walls
                food_counter = 0  # Reset the counter

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
gameLoop()