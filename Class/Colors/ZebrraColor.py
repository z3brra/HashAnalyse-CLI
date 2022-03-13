#! /usr/bin/python3
# -*- coding: utf-8 -*-

"""## ANSII Color formatting for output in terminal"""

from typing import Text

from art import text2art
from attr import attr
from .AnsiTerm import AnsiColored


class Colored(object):
    """# Class Colored

    ## ANSII Color formatting for output in terminal
    
    ### Colors available :

    ```
    COLORS = [
        'red',
        'green',
        'yellow',
        'blue',
        'magenta',
        'cyan',
        'white',
        'light_black',
        'light_red',
        'light_green',
        'light_yellow',
        'light_blue',
        'light_magenta',
        'light_cyan',
        'light_white'
    ]
    
    ```

    """
    COLORS = [
        'black',
        'red',
        'green',
        'yellow',
        'blue',
        'magenta',
        'cyan',
        'white',
        'light_black',
        'light_red',
        'light_green',
        'light_yellow',
        'light_blue',
        'light_magenta',
        'light_cyan',
        'light_white'
    ]

    @staticmethod
    def text2art(text: str, color: str, on_color= None, attrs= None) -> Text:
        colors_list = __class__.COLORS
        if on_color is not None:
            on_color = colors_list[colors_list.index(on_color)]
        return (AnsiColored().colored(text2art(text), colors_list[colors_list.index(color)], on_color, attrs))

    @staticmethod
    def colored(text: str, color: str, on_color= None, attrs= None) -> Text:
        """## Colorize text.

        ### Colors:
            - ``black, red, green, yellow, blue, magenta, cyan, white``.
        
        ### Light_colors :
            - ``light_black, light_red, light_green, light_yellow, light_blue, light_magenta, light_cyan, light_white``.

        ## --------------------------------------------------------------------------------------------------------------------

        ### Highlights colors:
            - ``black, red, green, yellow, blue, magenta, cyan, white``.

        ### Highlights light colors: 
            - ``light_black, light_red, light_green, light_yellow, light_blue, light_magenta, light_cyan, light_white``.

        ## --------------------------------------------------------------------------------------------------------------------

        ### Attributes:
            - ``bold, dark, underline, blink, reverse, concealed``.



        ### Example:
        ```
            colored('Hello, World !', 'red', 'on_grey', ['blink'])
            colored('Hello World !', 'light_red', None, ['underline', 'blink'])
            colored('Hello, World!', 'green')
        ```
        """
        colors_list = __class__.COLORS
        return (AnsiColored().colored(text, colors_list[colors_list.index(color)], on_color, attrs))

colorize = Colored()