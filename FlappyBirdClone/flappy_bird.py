import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (135, 206, 250)
GREEN = (0, 255, 0)

# Define screen dimensions
WIDTH, HEIGHT = 400, 600

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird Clone 🐦")

# Define fonts
font = pygame.font.Font(None, 50)

# Load images
bird_img = pygame.image.load("bird.png")  # Replace with your bird image file
bird_img = pygame.transform.scale(bird_img, (40, 30))

pipe_img = pygame.image.load("pipe.png")  # Replace with your pipe image file
pipe_img = pygame.transform.scale(pipe_img, (70, 400))

# Define constants
GRAVITY = 0.5
BIRD_JUMP = -8
PIPE_SPEED = 4
GAP_HEIGHT = 150

def draw_bird(x, y):
    """Draws the bird on the screen."""
    screen.blit(bird_img, (x, y))

def draw_pipes(pipes):
    """Draws the pipes on the screen."""
    for pipe in pipes:
        screen.blit(pipe_img, (pipe['x'], pipe['top']))
        screen.blit(pygame.transform.flip(pipe_img, False, True), (pipe['x'], pipe['bottom']))

def display_score(score):
    """Displays the player's score on the screen."""
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def check_collision(bird_x, bird_y, pipes):
    """Checks for collisions between the bird and pipes or boundaries."""
    if bird_y < 0 or bird_y > HEIGHT:
        return True
    for pipe in pipes:
        if bird_x < pipe['x'] + 70 and bird_x + 40 > pipe['x']:
            if bird_y < pipe['top'] + 400 or bird_y + 30 > pipe['bottom']:
                return True
    return False

def game_loop():
    """Main game loop."""
    # Bird properties
    bird_x, bird_y = 50, HEIGHT // 2
    bird_velocity = 0

    # Pipe properties
    pipes = []
    pipe_spawn_timer = 0
    score = 0

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_velocity = BIRD_JUMP

        # Apply gravity to the bird
        bird_velocity += GRAVITY
        bird_y += bird_velocity

        # Spawn pipes
        pipe_spawn_timer += 1
        if pipe_spawn_timer > 100:
            gap_y = random.randint(50, HEIGHT - GAP_HEIGHT - 50)
            pipes.append({'x': WIDTH, 'top': gap_y - 400, 'bottom': gap_y + GAP_HEIGHT})
            pipe_spawn_timer = 0

        # Move pipes
        for pipe in pipes:
            pipe['x'] -= PIPE_SPEED

        # Remove off-screen pipes
        pipes = [pipe for pipe in pipes if pipe['x'] + 70 > 0]

        # Check for collisions
        if check_collision(bird_x, bird_y, pipes):
            break

        # Update score
        for pipe in pipes:
            if bird_x > pipe['x'] + 70 and not pipe.get('scored', False):
                score += 1
                pipe['scored'] = True

        # Draw everything
        screen.fill(BLUE)
        draw_bird(bird_x, bird_y)
        draw_pipes(pipes)
        display_score(score)

        # Update the display
        pygame.display.flip()

        # Control the game speed
        pygame.time.Clock().tick(60)

# Start the game
game_loop()