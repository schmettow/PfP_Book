import pygame


def main():
    # --- What we are building ------------------------------------------------
    # A paper traffic light: a white slider strip with red, yellow, and green
    # circles. The strip is always fully drawn. A smaller black screen with a
    # round cutout sits in front of it; the selected circle shows through the
    # cutout, while the outer circles remain partially visible around the
    # screen. The window background is light blue sky, so the white strip and
    # the black screen read as separate layers.

    WIDTH, HEIGHT = 800, 600

    # The slider is wider than the screen and stays inside the window at all
    # three positions.
    SLIDE_W, SLIDE_H = 460, 220
    PANEL_W, PANEL_H = 260, 260
    CUTOUT_R = 65
    LAMP_R = 70
    SPACING = 150

    SKY = (170, 210, 240)
    WHITE = (255, 255, 255)
    RED = (230, 45, 45)
    YELLOW = (245, 210, 40)
    GREEN = (40, 200, 90)

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PIP Cutout")
    clock = pygame.time.Clock()

    # --- Lowest layer: sky ---------------------------------------------------
    # The sky is painted every frame in the presentational block below.

    # --- Middle layer: the slider -------------------------------------------
    # The white strip is a static surface. All three circles are drawn once;
    # the strip itself is moved by the panel class.
    slide = pygame.Surface((SLIDE_W, SLIDE_H))
    slide.fill(WHITE)
    for i, color in enumerate((RED, YELLOW, GREEN)):
        x = SLIDE_W // 2 + (i - 1) * SPACING
        pygame.draw.circle(slide, color, (x, SLIDE_H // 2), LAMP_R)

    # --- Top layer: the black screen ----------------------------------------
    # SRCALPHA means every pixel carries its own alpha. The panel is filled
    # opaque black; drawing a circle with alpha 0 punches a transparent hole.
    # There is no separate glass layer in this version: the cutout itself is
    # the alpha mask.
    panel = pygame.Surface((PANEL_W, PANEL_H), pygame.SRCALPHA)
    panel.fill((0, 0, 0, 255))
    pygame.draw.circle(
        panel,
        (0, 0, 0, 0),
        (PANEL_W // 2, PANEL_H // 2),
        CUTOUT_R,
    )
    panel_rect = pygame.Rect(
        (WIDTH - PANEL_W) // 2,
        (HEIGHT - PANEL_H) // 2,
        PANEL_W,
        PANEL_H,
    )

    traffic_light = TrafficLightPanel(panel, slide, panel_rect, SPACING)

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
        # Draw order: sky -> slider -> screen.
        screen.fill(SKY)
        traffic_light.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


class TrafficLightPanel:
    """The black screen and the white slider behind it."""

    def __init__(self, panel, slide, rect, spacing):
        self.panel = panel
        self.slide = slide
        self.rect = rect
        self.spacing = spacing
        self.state = 2  # 1 = left lamp, 2 = middle, 3 = right

    def shift_left(self):
        # Numerical states keep the transition simple. Clamp at 1.
        self.state = max(self.state - 1, 1)

    def shift_right(self):
        # Clamp at 3.
        self.state = min(self.state + 1, 3)

    def draw(self, surface):
        # State 2 is centred. State 1 moves the strip right so the left lamp
        # is under the cutout; state 3 moves it left for the right lamp.
        offset = (2 - self.state) * self.spacing
        slide_x = self.rect.centerx - self.slide.get_width() // 2 + offset
        slide_y = self.rect.centery - self.slide.get_height() // 2

        # The whole strip is drawn every frame. The black screen covers the
        # centre; the outer lamps remain partially visible around it.
        surface.blit(self.slide, (slide_x, slide_y))
        surface.blit(self.panel, self.rect.topleft)


if __name__ == "__main__":
    main()
