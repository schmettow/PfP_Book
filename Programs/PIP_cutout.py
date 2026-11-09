import pygame

# --- Configuration ---------------------------------------------------------

WIDTH, HEIGHT = 800, 600
PANEL_W, PANEL_H = 420, 420
CUTOUT_R = 90
LAMP_R = 100
SPACING = 200
SLIDE_W, SLIDE_H = 900, 600

WHITE = (255, 255, 255)
PAPER = (238, 236, 228)
RED = (230, 45, 45)
YELLOW = (245, 210, 40)
GREEN = (40, 200, 90)

PANEL_RECT = pygame.Rect(
    (WIDTH - PANEL_W) // 2,
    (HEIGHT - PANEL_H) // 2,
    PANEL_W,
    PANEL_H,
)


def make_slide():
    """The hidden slide with three colored lamps."""
    slide = pygame.Surface((SLIDE_W, SLIDE_H))
    slide.fill(PAPER)
    for i, color in enumerate((RED, YELLOW, GREEN)):
        x = SLIDE_W // 2 + (i - 1) * SPACING
        pygame.draw.circle(slide, color, (x, SLIDE_H // 2), LAMP_R)
    return slide


def make_panel():
    """The black screen with a round alpha cutout."""
    # Learning point: SRCALPHA gives every pixel its own alpha.
    panel = pygame.Surface((PANEL_W, PANEL_H), pygame.SRCALPHA)
    panel.fill((0, 0, 0, 255))
    # Learning point: alpha 0 punches a transparent hole; the rest stays opaque.
    pygame.draw.circle(
        panel,
        (0, 0, 0, 0),
        (PANEL_W // 2, PANEL_H // 2),
        CUTOUT_R,
    )
    return panel


class TrafficLightPanel:
    """The black panel and the slide behind it."""

    def __init__(self, panel, slide, rect):
        self.panel = panel
        self.slide = slide
        self.rect = rect
        self.position = "middle"  # left | middle | right

    def shift_left(self):
        # Learning point: shifting is a state transition, not an animation.
        if self.position == "right":
            self.position = "middle"
        elif self.position == "middle":
            self.position = "left"

    def shift_right(self):
        if self.position == "left":
            self.position = "middle"
        elif self.position == "middle":
            self.position = "right"

    def draw(self, surface):
        # Learning point: the slide is larger than the panel; clip it to the
        # panel rect so its edges never show on the white background.
        shift = {"left": SPACING, "middle": 0, "right": -SPACING}[self.position]
        slide_x = self.rect.centerx - SLIDE_W // 2 + shift
        slide_y = self.rect.centery - SLIDE_H // 2

        surface.set_clip(self.rect)
        surface.blit(self.slide, (slide_x, slide_y))
        surface.set_clip(None)

        # Learning point: blit order is slide -> panel. The alpha hole in the
        # panel reveals the selected lamp.
        surface.blit(self.panel, self.rect.topleft)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PIP Cutout")
    clock = pygame.time.Clock()

    # Static layers, built once in the main program.
    slide = make_slide()
    panel = make_panel()
    traffic_light = TrafficLightPanel(panel, slide, PANEL_RECT)

    running = True
    while running:
        # ITC — interactive transitionals
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    traffic_light.shift_left()
                elif event.key == pygame.K_RIGHT:
                    traffic_light.shift_right()

        # Presentationals — pure drawing; no state changes here.
        screen.fill(WHITE)
        traffic_light.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
