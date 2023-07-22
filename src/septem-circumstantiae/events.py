# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""

# https://alxfed.github.io/blog/posts/2019/02/22/Septem-Circumstantiae.html


class Event:
    """"""
    who: str    = ''  # quis. Who did it or who is reporting a natural event?
    what: str   = ''  # quid. What happened and was observed?
    when: str   = ''  # quando. When did it happen or started happening? Does it still continue or can happen again?
    where: str  = ''  # ubi. Where did it take place?
    why: str    = ''  # cur (for the sake of what?). Is there a cause or reason for the event?
    how: str    = ''  # quem ad modum (in what way?). How did it happen?
    by_what_means: str = ''  # quibus adminiculis. How was it achieved? Were there any other factors involved?

    def __init__(self, *args, **kwargs):
        pass

    def answer_who(self, *args, **kwargs):
        pass

    def answer_what(self, *args, **kwargs):
        pass

    def answer_when(self, *args, **kwargs):
        pass

    def answer_where(self, *args, **kwargs):
        pass

    def answer_why(self, *args, **kwargs):
        pass

    def answer_how(self, *args, **kwargs):
        pass

    def answer_by_what_means(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        self.answer_who(self, *args, **kwargs)
        self.answer_what(self, *args, **kwargs)
        self.answer_how(self, *args, **kwargs)
        self.answer_when(self, *args, **kwargs)
        self.answer_where(self, *args, **kwargs)
        self.answer_why(self, *args, **kwargs)
        self.answer_how(self, *args, **kwargs)
        self.answer_by_what_means(self, *args, **kwargs)
        return self

    def __repr__(self, *args, **kwargs):
        return f"""Event(who={self.who},/n 
            what={self.what},/n /n
            when={self.when},/n /n
            where={self.where},/n /n
            why={self.why},/n /n
            how={self.how},/n /n
            by_what_means={self.by_what_means})/n /n"""
