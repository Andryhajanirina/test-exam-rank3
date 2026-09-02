#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   py_twist_sequence.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/09/02 15:35:54 by andry-ha            #+#    #+#            #
#   Updated: 2026/09/02 16:59:54 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Write a function that rotates an array to the right by k positions.
Rotating right by k means the last k elements move to the front.
"""


def twist_sequence(arr: list[int], k: int) -> list[int]:
    if not arr:
        return []
    shift = k % len(arr)
    return arr[-shift:] + arr[:-shift]


if __name__ == "__main__":
    print(twist_sequence([1, 2, 3, 4, 5], 2))
    print(twist_sequence([1, 2, 3], 1))
    print(twist_sequence([1, 2, 3, 4], 0))
    print(twist_sequence([1, 2, 3], 5))
    print(twist_sequence([], 3))
