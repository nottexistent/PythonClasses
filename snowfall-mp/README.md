Please fix the snowfall_multiprocess.py file. You should NOT edit any other file. The problems are with the multiprocess code, and not other logic.

# Requirements (all must be satisfied)

* No code has been copied from elsewhere
* Find and fix the following problems:
    * `stop_event` is not created correctly                 X
    * `queue_left` should not raise an error if empty       X
    * `queue_right` should not raise an error if full       X
    * Fix how the processes are started                     X
    * Ensure the correct arguments are passed to `run_game` X
* Here is how the final program should work once you've fixed the above:
    * No errors are raised
    * Player can move left and right with `a` and `d` keys
    * Two piles of snow should slowly appear on the left side of the screen
    * A pile should slowly decrease if the player is near it
    * Pressing Ctrl+C should end the program without an error
    * Pressing Escape should end the program without an error (sometimes have to press multiple times)
    * See below for example output
* `snowfall_multiprocess.py` has a header with your name, date, CRN, and class name
* Include total debugging time

## Example Output (bottom left of screen)

    |
    |                  ...|
    |         ===      0 /
    |         ===      /
    |         ===     / \
    +===================================
