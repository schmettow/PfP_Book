import pygame

WIDTH, HEIGHT = 800, 600


def main():
    # --- What we are building ------------------------------------------------
    # A paper traffic light: a white slider strip with red, yellow, and green
    # circles. The strip is drawn by TrafficLightPanel.draw() at all times.
    # A smaller black screen with a round cutout sits in front of it; the
    # selected circle shows through the cutout, while the outer circles remain
    # partially visible around the screen. The window background is light blue
    # sky, so the white strip and the black screen read as separate layers.
    #
    # All sizes are relative to the global WIDTH and HEIGHT. Changing those two
    # values scales the layout instead of requiring new absolute coordinates.

    panel_w = round(WIDTH * 0.325)
    panel_h = round(HEIGHT * 0.4333)
    cutout_r = round(min(WIDTH, HEIGHT) * 0.1083)

    SKY = (170, 210, 240)

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PIP Cutout")
    clock = pygame.time.Clock()

    # --- Lowest layer: sky ---------------------------------------------------
    # The sky is painted every frame in the presentational block below.

    # --- Top layer: the black screen ----------------------------------------
    # SRCALPHA means every pixel carries its own alpha. The panel is filled
    # opaque black; drawing a circle with alpha 0 punches a transparent hole.
    # There is no separate glass layer in this version: the cutout itself is
    # the alpha mask.
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
        # Draw order: sky -> slider (inside TrafficLightPanel.draw) -> screen.
        screen.fill(SKY)
        traffic_light.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


class TrafficLightPanel:
    """The black screen and the white slider drawn behind it."""

    WHITE = (255, 255, 255)
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

        # Slider geometry, also relative to the global window size.
        self.slide_w = round(WIDTH * 0.575)
        self.slide_h = round(HEIGHT * 0.3667)
        self.spacing = round(WIDTH * 0.1875)
        self.lamp_r = round(min(WIDTH, HEIGHT) * 0.1167)

        self.state = 2  # 1 = left lamp, 2 = middle, 3 = right

    def shift_left(self):
        # Numerical states keep the transition simple. Clamp at 1.
        self.state = max(self.state - 1, 1)

    def shift_right(self):
        # Clamp at 3.
        self.state = min(self.state + 1, 3)

    def draw(self, surface):
        # The slider strip is built inside draw(), with all three circles.
        slide = pygame.Surface((self.slide_w, self.slide_h))
        slide.fill(self.WHITE)
        for i, color in enumerate((self.RED, self.YELLOW, self.GREEN)):
            x = self.slide_w // 2 + (i - 1) * self.spacing
            pygame.draw.circle(slide, color, (x, self.slide_h // 2), self.lamp_r)

        # State 2 is centred. State 1 moves the strip right so the left lamp
        # is under the cutout; state 3 moves it left for the right lamp.
        offset = (2 - self.state) * self.spacing
        slide_x = self.panel_rect.centerx - self.slide_w // 2 + offset
        slide_y = self.panel_rect.centery - self.slide_h // 2

        # The whole strip is blitted every frame. The black screen covers the
        # centre; the outer circles remain partially visible around it.
        surface.blit(slide, (slide_x, slide_y))
        surface.blit(self.panel, self.panel_rect.topleft)


if __name__ == "__main__":
    main()
