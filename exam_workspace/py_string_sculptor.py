#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   py_string_sculptor.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/09/02 14:56:12 by andry-ha            #+#    #+#            #
#   Updated: 2026/09/02 15:34:46 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Write a function that transforms a string by alternating the case of
alphabetic characters only.
Non-alphabetic characters remain unchanged and are NOT counted in the
alternation index.
The first alphabetic character should be lowercase, the second uppercase, etc.
Spaces reset the alternation (next alpha after a space is lowercase again).
"""


def string_sculptor(text: str) -> str:
    result = []
    lower_case = True
    for char in text:
        if char.isalpha():
            if lower_case:
                result.append(char.lower())
            else:
                result.append(char.upper())
            lower_case = not lower_case
        else:
            result.append(char)
            if char.isspace():
                lower_case = True

    return "".join(result)


if __name__ == "__main__":
    print(string_sculptor("hello"))
    print(string_sculptor("Hello World"))
    print(string_sculptor("abc123def"))
    print(string_sculptor("Python3.9!"))
    print(string_sculptor(""))
