# -*- coding: utf-8 -*-

"""
spotifywebapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from spotifywebapi.models.chapter_object import ChapterObject


class ManyChapters(object):

    """Implementation of the 'ManyChapters' model.

    TODO: type model description here.

    Attributes:
        chapters (List[ChapterObject]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "chapters": 'chapters'
    }

    def __init__(self,
                 chapters=None):
        """Constructor for the ManyChapters class"""

        # Initialize members of the class
        self.chapters = chapters 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        chapters = None
        if dictionary.get('chapters') is not None:
            chapters = [ChapterObject.from_dictionary(x) for x in dictionary.get('chapters')]
        # Return an object of this model
        return cls(chapters)
