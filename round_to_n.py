def round_to_n(x, n):
  """ cunning/cheap way to round a number ('x') to a specified number of digits ('n')
  abusing variable reformating"""
  
    if n < 1:
        raise ValueError("number of significant digits must be >= 1")
    # Use %e format to get the n most significant digits, as a string.
    format = "%." + str(n-1) + "e"
    as_string = format % x
    return float(as_string)
