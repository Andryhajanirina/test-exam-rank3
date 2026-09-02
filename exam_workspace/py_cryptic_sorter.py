#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   py_cryptic_sorter.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/09/02 10:47:01 by andry-ha            #+#    #+#            #
#   Updated: 2026/09/02 11:03:31 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def cryptic_sorter(strings: list[str]) -> list[str]:
    return sorted(
        strings, key=lambda word: (
            len(word),
            word.lower(),
            word,
            sum(c.lower() in "aeiouy" for c in word),
        )
    )


if __name__ == "__main__":
    print(cryptic_sorter(["apple", "cat", "banana", "dog", "elephant"]))
    print(cryptic_sorter(["aaa", "bbb", "AAA", "BBB"]))
    print(cryptic_sorter(["hello", "world", "hi", "test"]))
    print(cryptic_sorter([]))
    print(cryptic_sorter([""]))
