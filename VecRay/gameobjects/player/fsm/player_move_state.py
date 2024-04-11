import logging

import pyray as rl
from pyray import Vector2

from finite_state_machine.state import State


class Move(State):

    PLAYER_SPEED = 5

    def __init__(self):
        super().__init__()
        self.current_segment_index = None
        self.is_open_segment = True

    def on_update(self):
        player = self.fsm.owner
        # if rl.is_key_down(rl.KeyboardKey.KEY_LEFT):
        #     player.x -= self.PLAYER_SPEED
        # if rl.is_key_down(rl.KeyboardKey.KEY_RIGHT):
        #     player.x += self.PLAYER_SPEED
        # if rl.is_key_down(rl.KeyboardKey.KEY_UP):
        #     player.y -= self.PLAYER_SPEED
        # if rl.is_key_down(rl.KeyboardKey.KEY_DOWN):
        #     player.y += self.PLAYER_SPEED

        if rl.is_key_down(rl.KeyboardKey.KEY_LEFT):
            self._move_constrained(player, "left", player.segments)
        elif rl.is_key_down(rl.KeyboardKey.KEY_RIGHT):
            self._move_constrained(player, "right", player.segments)

    def _move_constrained(self, game_object, direction, segments):
        # Get current position of the game object
        current_position = Vector2(game_object.x, game_object.y)

        # Find the segment that the game object is currently on

        for i, (start, end) in enumerate(segments):
            # print(f"{current_position.x} - {start.x}  ---- {current_position.y} - {start.y}")
            if self.are_points_equal(current_position, start):
                self.current_segment_index = i
                break

        if self.current_segment_index is not None:
            # If moving left and at the start of the segment, switch to the previous segment
            if direction == "left" and self.are_points_equal(current_position, segments[self.current_segment_index][0]):
                if self.is_open_segment and self.current_segment_index == 0:
                    return  # clamp if open
                else:
                    self.current_segment_index = (self.current_segment_index - 1) % len(segments)

            # If moving right and at the end of the segment, switch to the next segment
            elif direction == "right" and self.are_points_equal(current_position, segments[self.current_segment_index][1]):
                if self.is_open_segment and self.current_segment_index == len(segments) - 1:
                    return  # clamp if open
                else:
                    self.current_segment_index = (self.current_segment_index + 1) % len(segments)

            print(self.current_segment_index)
            # Calculate the next position based on the current segment
            start, end = segments[self.current_segment_index]
            x0 = start.x
            y0 = start.y
            x1 = end.x
            y1 = end.y

            # Calculate the slope of the segment
            if x0 != x1:
                slope = (y1 - y0) / (x1 - x0)
            else:
                slope = None

            # Move the game object to the next position along the segment
            if direction == "left":
                if slope is not None:
                    # Calculate the next x and y coordinates based on the slope
                    new_x = current_position.x - 1
                    new_y = int(y0 + slope * (new_x - x0))
                else:
                    # If the segment is vertical, only adjust the y coordinate
                    new_x = current_position.x
                    new_y = current_position.y - 1
            elif direction == "right":
                if slope is not None:
                    # Calculate the next x and y coordinates based on the slope
                    new_x = current_position.x + 1
                    new_y = int(y0 + slope * (new_x - x0))
                else:
                    # If the segment is vertical, only adjust the y coordinate
                    new_x = current_position.x
                    new_y = current_position.y + 1

            # Update the game object's position

            game_object.x = new_x
            game_object.y = new_y

    def are_points_equal(self, a, b):
        return a.x == b.x and a.y == b.y
