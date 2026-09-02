#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   py_string_permutation_checker.py                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/09/02 14:33:25 by andry-ha            #+#    #+#            #
#   Updated: 2026/09/02 14:40:43 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Write a function that determines if two strings are permutations
of each other.
Case sensitive. Whitespace and punctuation count as regular characters.
Empty strings are permutations of each other.
"""


def string_permutation_checker(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)


if __name__ == "__main__":
    print(string_permutation_checker("abc", "bca"))
    print(string_permutation_checker("abc", "def"))
    print(string_permutation_checker("listen", "silent"))
    print(string_permutation_checker("hello", "bello"))
    print(string_permutation_checker("", ""))
    print(string_permutation_checker("a", ""))
    print(string_permutation_checker("Abc", "abc"))
    print(string_permutation_checker("a gentleman", "elegant man"))
