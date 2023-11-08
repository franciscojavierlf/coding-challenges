# Spiral
# Prompt
# Write a program that prints a spiral of ASCII characters. The size of the spiral"s longest edge, n, should be configurable.

# Details
# The spiral"s first edge should go to the right and have length n. Each subsequent edge should be one unit shorter than the last.


# Example
# spiral(1)
# #

# spiral(2)
# # #

# spiral(3)
# # # #
#     #

# spiral(4)
# # # # #
#       #
#     # #

# spiral(5)
# # # # # #
#         #
#     #   #
#     # # #

# spiral(6)
# # # # # # #
#           #
#     # #   #
#     #     #
#     # # # #

# spiral(7)
# # # # # # # #
#             #
#     # # #   #
#     #   #   #
#     #       #
#     # # # # #

def print_spiral(n, chars):
  width = n
  height = max(n - 1, 1)

  for y in range(height):
    row = ""
    for x in range(width):
      row += "# " if chars[x + y * n] else "  "
    print(row)


def spiral_r(max_n, n, chars, x0, y0, direction):
  
  # Last case
  if not n:
    return chars
  
  match direction:
    # Right
    case "r":
      for x in range(x0, x0 + n):
        chars[x + y0 * max_n] = True
      x0 += n - 1
      direction = "d"
    # Left
    case "l":
      for x in range(x0, x0 - n, -1):
        chars[x + y0 * max_n] = True
      x0 -= n - 1
      direction = "u"
    # Up
    case "u":
      for y in range(y0, y0 - n, -1):
        chars[x0 + y * max_n] = True
      y0 -= n - 1
      direction = "r"
      pass
    # Down
    case "d":
      for y in range(y0, y0 + n):
        chars[x0 + y * max_n] = True
      y0 += n - 1
      direction = "l"

  # Another tail
  return spiral_r(max_n, n - 1, chars, x0, y0, direction)


def spiral(n):
  width = n
  height = max(n - 1, 1)
  chars = [False] * width * height
  chars = spiral_r(n, n, chars, 0, 0, "r")
  print_spiral(n, chars)


if __name__ == "__main__":

  for i in range(1, 8):
    print(f"----- Spiral {i} -----")
    spiral(i)