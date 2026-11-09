import pygame

WIDTH, HEIGHT = 800, 600


def main():
    # --- What we are building ------------------------------------------------
    # A paper traffic light: three adjacent colored squares (red, yellow,
    # green) form the slider. There is no paper background; the squares are
    # drawn directly on the sky.
    #
    # A smaller black screen with a round cutout sits in front. The selected
    # square shows through the cutout; the outer squares remain partially
    # visible around the screen.
    #
    # All sizes are relative to the global WIDTH and HEIGHT.

    panel_w = round(WIDTH * 5/12)
    panel_h = round(HEIGHT * 5/12)
    cutout_r = round(min(WIDTH, HEIGHT) * 1/12)

    SKY = (170, 210, 240)

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PIP Cutout")
    clock = pygame.time.Clock()

    # --- Lowest layer: sky ---------------------------------------------------
    # Painted every frame in the presentational block below.

    # --- Top layer: the black screen ----------------------------------------
    # SRCALPHA means every pixel carries its own alpha. Fill the panel opaque
    # black, then punch a transparent circular hole with alpha 0.
    # No separate glass layer: the cutout itself is the alpha mask.
    panel = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA)
    panel.fill((0, 0, 0, 255))
    pygame.draw.circle(
        panel,
        (0, 0, 0, 0),
        (panel_w // 2, panel_h // 2),
        cutout_r,
    )

    traffic_light = TrafficLightPanel(panel)

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
        # Draw order: sky -> squares (inside TrafficLightPanel.draw) -> screen.
        screen.fill(SKY)
        traffic_light.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


class TrafficLightPanel:
    """The black screen and three adjacent colored squares behind it."""

    RED = (230, 45, 45)
    YELLOW = (245, 210, 40)
    GREEN = (40, 200, 90)

    def __init__(self, panel):
        self.panel = panel
        self.panel_w, self.panel_h = panel.get_size()

        # Center the panel relative to the global window size.
        self.panel_rect = pygame.Rect(
            (WIDTH - self.panel_w) // 2,
            (HEIGHT - self.panel_h) // 2,
            self.panel_w,
            self.panel_h,
        )

        # One parameter for the slider: square side = step size.
        self.square = round(WIDTH * 2/12)

        self.state = 2  # 1 = left square, 2 = middle, 3 = right

    def shift_left(self):
        # Numerical states keep the transition simple. Clamp at 1.
        self.state = max(self.state - 1, 1)

    def shift_right(self):
        # Clamp at 3.
        self.state = min(self.state + 1, 3)

    def draw(self, surface):
        # The three squares are adjacent: the next square starts exactly one
        # square-width to the right. The selected square is centred under the
        # cutout; state 2 is neutral, state 1 shifts right, state 3 left.
        offset = (2 - self.state) * self.square
        left = self.panel_rect.centerx - self.square * 3 // 2 + offset
        top = self.panel_rect.centery - self.square // 2

        for i, color in enumerate((self.RED, self.YELLOW, self.GREEN)):
            pygame.draw.rect(
                surface,
                color,
                (left + i * self.square, top, self.square, self.square),
            )

        # The alpha hole in the panel reveals the selected square.
        surface.blit(self.panel, self.panel_rect.topleft)


if __name__ == "__main__":
    main()
