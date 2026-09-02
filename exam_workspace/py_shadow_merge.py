#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   py_shadow_merge.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/09/02 14:28:00 by andry-ha            #+#    #+#            #
#   Updated: 2026/09/02 14:32:23 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Write a function that merges two sorted lists into one sorted list."""


def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    return sorted(list1 + list2)


if __name__ == "__main__":
    print(shadow_merge([1, 3, 5], [2, 4, 6]))
    print(shadow_merge([1, 2, 3], [4, 5, 6]))
    print(shadow_merge([1], [2, 3, 4]))
    print(shadow_merge([], [1, 2, 3]))
    print(shadow_merge([1, 1, 2], [1, 3, 3]))
