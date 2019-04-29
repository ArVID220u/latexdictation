"""
Defines the base layer interface to be used by all layers.
"""

from . import *

import re

class SaytexLayer:


    @classmethod
    def get_layer(cls, layer_id):
        """
        Creates a new layer of the layer_id subclass.
        :param layer_id: str, representing the layer to create.
        :return: a SaytexLayer object, representing a particular layer
        """
        return layer_id_to_class[layer_id]()
    

    def execute_layer(self, input_string):
        """
        To be overridden in a layer subclass.
        :param input_string: str, the input
        :return: str, the output of the layer
        """
        return NotImplementedError



    def replace_words(self, word_tuples, input_string):
        """
        Replaces words in input_string using the word_tuples.
        :param word_tuples: a list of tuples of two strings, where the first one
        is the word to be replaced and the second one is the word to replace it with
        :input_string: str
        :return: str, with words replaced
        """
        in_progress_string = input_string
        for word_tuple in word_tuples:
            s = r'\b' + word_tuple[0] + r'\b'
            in_progress_string = re.sub(s, word_tuple[1], in_progress_string)
        return in_progress_string
