from .Analyser import Analyse

CONST = {
    'title': 'Hash Analyser',
    'subtitle': 'A simple file analyser. made By ',
    'author': 'Zebrra ®',
    'bar': '------------------------------------------------------------------------------',
    'footer': "-----------------------------  FIN DE L'ANALYSE  -----------------------------"
}

def load() -> None:
    Analyse(**CONST).run()
