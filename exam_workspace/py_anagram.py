#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   py_anagram.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/09/02 14:18:16 by andry-ha            #+#    #+#            #
#   Updated: 2026/09/02 14:27:25 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Write a function that checks if two strings are anagrams.
  They must contain exactly the same letters with the same quantity,
  ignoring case and spaces.
"""


def anagram(s1: str, s2: str) -> bool:
    clean_s1 = sorted("".join([c.lower().strip() for c in s1 if c.isalpha()]))
    clean_s2 = sorted("".join([c.lower().strip() for c in s2 if c.isalpha()]))
    return clean_s1 == clean_s2


if __name__ == "__main__":
    print(anagram("listen", "silent"))
    print(anagram("Triangle", "Integral"))
    print(anagram("Dormitory", "Dirty Room"))
    print(anagram("hello", "world"))
    print(anagram("", ""))
    print(anagram("abc", "abcc"))
