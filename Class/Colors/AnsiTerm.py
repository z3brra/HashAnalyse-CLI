#! /usr/bin/python3
# -*- coding: utf-8 -*-

"""## ANSII Color formatting for output in terminal."""

import os

class AnsiColored:
    """## Classe AnsiColored
    
    ## ANSII Color formatting for output in terminal

    ### Colors available :
    ```
    STR_COLORS = [
        'black',
        'red',
        'green',
        'yellow',
        'blue',
        'magenta',
        'cyan',
        'white'
    ]
    
    STR_LIGHT_COLORS = [
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

    STR_COLORS = [
        'black',
        'red',
        'green',
        'yellow',
        'blue',
        'magenta',
        'cyan',
        'white'
    ]
    
    STR_LIGHT_COLORS = [
        'light_black',
        'light_red',
        'light_green',
        'light_yellow',
        'light_blue',
        'light_magenta',
        'light_cyan',
        'light_white'
    ]

    ATTRIBUTES = dict(
        list(
            zip([
                'bold',
                'dark',
                '',
                'underline',
                'blink',
                '',
                'reverse',
                'concealed'
            ],
            list(range(1, 9))
            )
        )
    )
    del ATTRIBUTES['']

    HIGHLIGHTS_COLORS = dict(
        list(
            zip(STR_COLORS,
            list(range(40, 48))
            )
        )
    )
    HIGHLIGHTS_LIGHT_COLORS = dict(
        list(
            zip(STR_LIGHT_COLORS,
            list(range(100, 108))
            )
        )
    )

    COLORS = dict(
        list(
            zip(STR_COLORS,
            list(range(30, 38))
            )
        )
    )

    LIGHT_COLORS = dict(
        list(
            zip(STR_LIGHT_COLORS,
            list(range(90, 98))
            )
        )
    )

    RESET = '\033[0m'

    @staticmethod
    def colored(text: str, color= None, on_color= None, attrs= None) -> str:
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
        if os.getenv('ANSI_COLORS_DISABLED') is None:
            fmt_str = '\033[%dm%s'
            if color is not None:
                if color in __class__.COLORS:
                    text = fmt_str % (__class__.COLORS[color], text)
                elif color in __class__.LIGHT_COLORS:
                    text = fmt_str % (__class__.LIGHT_COLORS[color], text)

            if on_color is not None:
                if on_color in __class__.HIGHLIGHTS_COLORS:
                    text = fmt_str % (__class__.HIGHLIGHTS_COLORS[on_color], text)
                
                elif on_color in __class__.HIGHLIGHTS_LIGHT_COLORS:
                    text = fmt_str % (__class__.HIGHLIGHTS_LIGHT_COLORS[on_color], text)
            
            if attrs is not None:
                for attr in attrs:
                    text = fmt_str % (__class__.ATTRIBUTES[attr], text)

            text += __class__.RESET
        return text

    @staticmethod
    def cprint(text, color=None, on_color=None, attrs=None, **kwargs) -> None:
        """Print colorize text.

        It accepts arguments of print function.
        """

        print((__class__.colored(text, color, on_color, attrs)), **kwargs)
