# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""

# https://alxfed.github.io/blog/posts/2019/02/22/Septem-Circumstantiae.html
circumstantiae = [
    'who', 'what', 'when', 'where', 'why', 'how', 'by_what_means'
]


class Event:
    """"""
    who: str            = ''  # quis. Who did it or who is reporting a natural event?
    what: str           = ''  # quid. What happened and was observed?
    when: str           = ''  # quando. When did it happen or started happening? Does it still continue or can happen again?
    where: str          = ''  # ubi. Where did it take place?
    why: str            = ''  # cur (for the sake of what?). Is there a cause or reason for the event?
    how: str            = ''  # quem ad modum (in what way?). How did it happen?
    by_what_means: str  = ''  # quibus adminiculis. How was it achieved? Were there any other factors involved?

    def __init__(self, **kwargs):
        for key,value in kwargs.items():
            setattr(self, key, value)

    def __call__(self, **kwargs):
        for key,value in kwargs.items():
            setattr(self, key, value)
        return self

    def __repr__(self, *args, **kwargs):
        return f"""     Event:
            who - {self.who},
            what - {self.what},
            when - {self.when},
            where - {self.where},
            why - {self.why},
            how - {self.how},
            by what means - {self.by_what_means}
            """


if __name__ == '__main__':
    keyword_arguments = {
        'who': 'I',
        'what': 'do',
        'when': 'now',
        'where': 'here',
        'why': 'because',
        'how': 'in a most simple way',
        'by_what_means': 'manually'
    }
    object = Event(**keyword_arguments)
    print(object)
    pass
