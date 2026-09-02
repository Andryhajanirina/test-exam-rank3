#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   py_mirror_matrix.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/09/02 11:49:38 by andry-ha            #+#    #+#            #
#   Updated: 2026/09/02 11:57:24 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    return [grid[::-1] for grid in matrix]


if __name__ == "__main__":
    print(mirror_matrix([[1, 2, 3], [4, 5, 6]]))
    print(mirror_matrix([[1, 2], [3, 4], [5, 6]]))
    print(mirror_matrix([[7]]))
    print(mirror_matrix([[1, 2, 3, 4]]))
    print(mirror_matrix([[-1, -2], [-3, -4]]))
