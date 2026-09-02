#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   py_inter.py                                          :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/09/02 11:04:55 by andry-ha            #+#    #+#            #
#   Updated: 2026/09/02 11:20:32 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def inter(s1: str, s2: str) -> str:
    # result = []
    # for c in s1:
    #     if c not in result and c in s2:
    #         result.append(c)
    # return "".join(result)
    return "".join([c for c in dict.fromkeys(s1) if c in s2])


if __name__ == "__main__":
    print(inter("hello", "world"))
    print(inter("banana", "band"))
    print(inter("abcabc", "bc"))
    print(inter("abc", "xyz"))
    print(inter("", "abc"))
