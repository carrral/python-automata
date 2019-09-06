# Nombre del Archivo: automata.py
#
# Descripción: Contiene la clase Automata(), necesaria para el análisis léxico de una línea.
#
# Autor: Carlos Carral Cortés
#
# Última modificación: 06/09/2019
#


class Automata:
    def __init__(self, estados_internos, alfabeto, f_trans, q0, estados_acept):
        """
        Autómata de aceptación para verificar si una línea es correcta.
        :param estados_internos: (Q) Lista de estados posibles en los que se puede encontrar el autómata.
        :param alfabeto: (Σ) Lista de símbolos pertenecientes al alfabeto.
        :param f_trans: (δ) Diccionario que determina las reglas de correspondencia Q x Σ -> Q
                            f_trans = {
                                        'q0':{'sim1': 'q1', 'sim2': 'q2',...},
                                        'q1':{'sim3: 'q3', 'sim4: 'q4',...},
                                        ...
                                        }
        :param q0: Estado inicial del autómata.
        :param estados_acept: (F) Lista de estados de aceptación del autómata (subconjunto de Q).
        """

        self.estados_internos = estados_internos
        self. alfabeto = alfabeto
        self.f_trans = f_trans
        self.estado_actual = q0
        self.estados_acept = estados_acept
        self.trazo = list()
        self.error_token = -1

    def procesar(self, tokens):
        """
        Determina si una cadena (lista de tokens) es válida o no de acuerdo a la función de aceptación.
        :param tokens: Lista de tokens que componen la cadena
        :return: Booleano (Acepta o No Acepta)
        """

        self.error_token = -1

        for i in range(len(tokens)):
            token = tokens[i]
            self.estado_actual = self.f(token)
            if self.estado_actual == 'X':
                break

        if self.estado_actual in self.estados_acept:
            return True
        else:
            self.registrar_error(i)
            return False

    def f(self, sim):
        """
        Retorna un estado de acuerdo al estado actual y a un  símbolo.
        En caso de que el estado NO esté definido bajo ese símbolo (o de que el símbolo no esté definido)
        retorna 'X'.

        :param sim: símbolo a analizar (elemento de tokens)
        :return: estado en (Q) o 'X'
        """
        q = 'X'

        # Si el símbolo está en el alfabeto
        if sim in self.alfabeto:

            # Si existe una definición para ese símbolo
            if sim in self.f_trans[self.estado_actual].keys():
                q = self.f_trans[self.estado_actual][sim]

        return q

    def registrar_error(self, index):
        """
        Registra el índice del token que generó la no aceptación de la línea.

        :param index: Índice del token que generó el error.
        :return: index
        """
        self.error_token = index
        return index
