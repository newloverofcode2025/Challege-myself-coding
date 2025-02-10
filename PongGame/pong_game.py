import pygame
import sys

# Initialize pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define screen dimensions
WIDTH, HEIGHT = 800, 600

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game 🏓")

# Define the clock to control the game speed
clock = pygame.time.Clock()

# Define paddle properties
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 7

# Define ball properties
BALL_SIZE = 15
BALL_SPEED_X, BALL_SPEED_Y = 5, 5

# Define fonts
font = pygame.font.Font(None, 74)

def draw_paddle(x, y):
    """Draws a paddle on the screen."""
    pygame.draw.rect(screen, WHITE, (x, y, PADDLE_WIDTH, PADDLE_HEIGHT))

def draw_ball(x, y):
    """Draws the ball on the screen."""
    pygame.draw.ellipse(screen, WHITE, (x, y, BALL_SIZE, BALL_SIZE))

def display_score(player1_score, player2_score):
    """Displays the scores of both players."""
    score1 = font.render(str(player1_score), True, WHITE)
    score2 = font.render(str(player2_score), True, WHITE)
    screen.blit(score1, (WIDTH // 4, 50))
    screen.blit(score2, (WIDTH * 3 // 4, 50))

def game_loop():
    """Main game loop."""
    # Initial positions
    paddle1_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
    paddle2_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
    ball_x, ball_y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
    ball_speed_x, ball_speed_y = BALL_SPEED_X, BALL_SPEED_Y

    # Scores
    player1_score, player2_score = 0, 0

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Get key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and paddle1_y > 0:
            paddle1_y -= PADDLE_SPEED
        if keys[pygame.K_s] and paddle1_y < HEIGHT - PADDLE_HEIGHT:
            paddle1_y += PADDLE_SPEED
        if keys[pygame.K_UP] and paddle2_y > 0:
            paddle2_y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and paddle2_y < HEIGHT - PADDLE_HEIGHT:
            paddle2_y += PADDLE_SPEED

        # Move the ball
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Ball collision with top and bottom walls
        if ball_y <= 0 or ball_y >= HEIGHT - BALL_SIZE:
            ball_speed_y = -ball_speed_y

        # Ball collision with paddles
        if ball_x <= PADDLE_WIDTH and paddle1_y <= ball_y + BALL_SIZE <= paddle1_y + PADDLE_HEIGHT:
            ball_speed_x = -ball_speed_x
        if ball_x >= WIDTH - PADDLE_WIDTH - BALL_SIZE and paddle2_y <= ball_y + BALL_SIZE <= paddle2_y + PADDLE_HEIGHT:
            ball_speed_x = -ball_speed_x

        # Ball out of bounds
        if ball_x <= 0:
            player2_score += 1
            ball_x, ball_y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
            ball_speed_x, ball_speed_y = BALL_SPEED_X, BALL_SPEED_Y
            pygame.time.wait(500)  # Pause before restarting
        if ball_x >= WIDTH:
            player1_score += 1
            ball_x, ball_y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
            ball_speed_x, ball_speed_y = -BALL_SPEED_X, BALL_SPEED_Y
            pygame.time.wait(500)  # Pause before restarting

        # Draw everything
        screen.fill(BLACK)
        draw_paddle(20, paddle1_y)  # Player 1 paddle
        draw_paddle(WIDTH - 30, paddle2_y)  # Player 2 paddle
        draw_ball(ball_x, ball_y)
        display_score(player1_score, player2_score)

        # Update the display
        pygame.display.flip()

        # Control the game speed
        clock.tick(60)

# Start the game
game_loop()